import ast
import copy
import pprint
from textwrap import dedent
from py3o.template.data_struct import (
    Py3oBuiltin,
    Py3oModule,
    Py3oName,
    Py3oArray,
    Py3oContainer,
    Py3oCall,
    Py3oDummy,
)


# This is used as global context key in the convertor
PY3O_MODULE_KEY = "__py3o_module__"


class Py3oConvertor(ast.NodeVisitor):
    """Provide the data extraction functionality."""

    def __call__(self, source):
        """
        When called, this class will unfold the ast, and for each node,
          try to represent its content in a simpler tree format.

        A local_context is created at the beginning, and is supposed to hold
         the defined variables in the form.
        When we find an Expression (visit_expr, visit_if), we search
         the context to find the related variable, and tell
         it that we have accessed it.
        The context is then returned to the user and can
         be converted into dict.

        The context can be considered as an instance of Py3oObject,
         containing other instances of Py3oObject, and so on.
        All Py3oObject classes inherit from dict, so the hierarchy is
         equivalent to a dict of dict, with specific functions.
        The main node is always a Py3oModule instance.
        For loops are represented as Py3oArray instances and can contain
         an array of Py3oObjects.
        Simple attributes calls are represented as Py3oName instances.


        Example of conversion:

          Python source:

          for i in mylist:
            i.foo
            for j in i.otherlist:
              i.bar.num
              j.egg

          Conversion:

          Py3oModule({
              'mylist': Py3oArray({
                  'foo': Py3oName({}),
                  'otherlist': Py3oArray({
                      'egg': Py3oName({}),
                  }),
                  'bar': Py3oName({
                      'num': Py3oName({}),
                  }),
              }),
          })
        """

        # Dedent the source before parsing it
        dedented_source = dedent(source)
        self._source = dedented_source
        self._ast = ast.parse(dedented_source)

        # Call the recursive visit function
        return self.visit(self._ast, Py3oDummy())

    @staticmethod
    def set_last_item(py3o_obj, inst):
        """Helper function that take a Py3oObject and set the first leaf found
          with inst.
        This should not be called with a leaf directly.
        """
        tmp = py3o_obj
        keys = tmp.keys()
        while keys:
            next_tmp = tmp[next(iter(keys))]
            next_keys = next_tmp.keys()
            if not next_keys:
                break
            tmp, keys = next_tmp, next_keys
        tmp[next(iter(keys))] = inst

    def bind_target(self, iterable, target, context, iterated=True):
        """Helper function to the For node.
        This function fill the context according to the iterable and
         target and return a new_context to pass through the for body
        The new context should contain the for loop declared variable
         as main key so our children can update their content without knowing
         where they come from.
        Example:
          python_code = 'for i in list'
          context = {
              'i': Py3oArray({}),
              '__py3o_module__': Py3oModule({'list': Py3oArray({})}),
          }
        In the above example, the two Py3oArray are the same instance.
        So if we later modify the context['i'] Py3oArray,
         we also modify the context['__py3o_module__]['list'] one.
        """
        # TODO: Implement some builtin decoding

        iter_key = iterable.get_key()
        found, rem_context, rem_iterable = context.rget(iterable)

        if found:
            target_name = rem_context
            self.set_last_item(iterable, target_name)
        else:
            target_name = Py3oArray() if iterated else Py3oName()
            self.set_last_item(rem_iterable, target_name)
            if rem_context is not context:
                # Update the related context with the new attribute access
                rem_context.rupdate(rem_iterable)
            else:
                context[PY3O_MODULE_KEY].rupdate(
                    {iter_key: iterable[iter_key]}
                )

        if target:
            target_key = target.get_key()
            context[target_key] = target_name

        return context

    def visit(self, node, local_context=None):
        """Call the node-class specific visit function,
         and propagate the context
        """
        method = "visit_" + node.__class__.__name__.lower()
        visitor = getattr(self, method, None)
        if visitor:
            return visitor(node, local_context)
        else:
            return self.generic_visit(node)

    def visit_module(self, node, local_context):
        """The main node, should be alone.
        Here we initialize the context and loop for all our children
        """
        module = Py3oModule()

        # Initialize the context with a specific key name to avoid duplicates
        # This key name should not be used as a variable name or
        #  unexpected behaviours will occur
        local_context[PY3O_MODULE_KEY] = module

        for n in node.body:
            res = self.visit(n, local_context)
            if res:
                local_context.rupdate(res)

        return module

    def visit_for(self, node, local_context):
        """Update the context so our chidren have access
         to the newly declared variable.
        """

        body_context = copy.copy(local_context)
        iterable = self.visit(node.iter, local_context)
        target = self.visit(node.target, local_context)

        # Bind iterable and target. Target variables are local to the loop ;
        # only the iterable and the body should impact the parent context.
        iter_names = Py3oDummy()
        escaped = []
        for target_name, iter_name in iterable.unpack(target):
            if iter_name:
                iterated = not any(
                    iter_name.rget(prev_iter)[0] for prev_iter in escaped
                )
                body_context = self.bind_target(
                    iter_name, target_name, body_context, iterated=iterated
                )
                iter_names.rupdate(iter_name)
                if target_name is None:
                    escaped.append(iter_name)
            elif target_name is not None:
                body_context[target_name.get_key()] = Py3oDummy()

        for n in node.body:
            self.visit(n, body_context)

        for value in iter_names.values():
            if value.get_size() == 0:
                value.direct_access = True

        return iter_names

    def visit_tuple(self, node, local_context):
        values = [self.visit(elt, local_context) for elt in node.elts]
        return Py3oContainer(values)

    visit_list = visit_tuple
    visit_set = visit_tuple

    def visit_name(self, node, local_context):
        """Simply return Py3oDummy equivalent"""
        return Py3oDummy({node.id: Py3oName()})

    def visit_attribute(self, node, local_context):
        """ Visit our children and return a Py3oDummy equivalent
        Example:
          i.egg.foo -> Py3oDummy({
              'i': Py3oName({
                  'egg': Py3oName({'foo': Py3oName()})
              }
          }
        """
        value = self.visit(node.value, local_context)
        if isinstance(value, Py3oDummy):
            self.set_last_item(value, Py3oName({node.attr: Py3oName()}))
            return value
        else:  # pragma: no cover
            raise NotImplementedError

    # TODO: Manage Tuple in for loop (for i, j in enumerate(list))
    # def visit_Tuple(self, node, local_context):
    #     pass

    def visit_expr(self, node, local_context):
        """An Expr is the way to express the will of printing a variable
         in a Py3oTemplate. So here we must update the context to map all
         attribute access.
        We only handle attribute access and simple name (i.foo or i)
        """
        # The value should be a Py3oDummy or a Py3oCall
        value = self.visit(node.value, local_context)
        if isinstance(value, Py3oDummy):
            key = value.get_key()
            if key in local_context:
                local_context[key].rupdate(value[key])
                if value.get_size() == 1:
                    # Tell the object that this is a direct access,
                    #  used mainly by Py3oArray instances
                    local_context[key].direct_access = True
            else:
                local_context[PY3O_MODULE_KEY].rupdate(value)

        elif isinstance(value, Py3oCall):
            for arg in value.values():
                if not arg:
                    continue
                key = arg.get_key()
                if key in local_context:
                    local_context[key].rupdate(arg[key])
                    if arg.get_size() == 1:
                        # Tell the object that this is a direct access,
                        #  used mainly by Py3oArray instances
                        local_context[key].direct_access = True
                else:
                    local_context[PY3O_MODULE_KEY].rupdate(arg)
        else:  # pragma: no cover
            raise NotImplementedError

    def visit_call(self, node, local_context):
        """Visit a function call.
        """
        # Get the name of the function and obtain its class
        name = self.visit(node.func, local_context)
        py3o_class = Py3oBuiltin.from_name(name)
        if py3o_class is None or not issubclass(py3o_class, Py3oCall):
            py3o_class = Py3oCall
        # For now, we just gather the args/kwargs to send to the function
        # Get the args
        args = [self.visit(arg, local_context) for arg in node.args]
        # Get the kwargs
        kwargs = {}
        for keyword in node.keywords:
            cut_keyword = self.visit(keyword, local_context)
            # Keywords are tuple in the form (key, val)
            kwargs[cut_keyword[0]] = cut_keyword[1]
        # Create the Py3oCall coresponding to those value
        call = py3o_class(name, {n: arg for n, arg in enumerate(args)})
        call.update({k: arg for k, arg in kwargs.items()})
        return call

    def visit_keyword(self, node, local_context):
        return node.arg, self.visit(node.value, local_context)

    def visit_str(self, node, local_context):
        """Do nothing
        """
        return Py3oDummy()

    def visit_if(self, node, local_context):
        tests = self.visit(node.test)
        if not isinstance(tests, list):
            tests = [tests]
        for test in tests:
            key = test.get_key()
            if key in local_context:
                local_context[key].rupdate(test[key])
                if test.get_size() == 1:
                    local_context[key].direct_access = True
            else:
                local_context[PY3O_MODULE_KEY].rupdate(test)

        for n in node.body:
            self.visit(n, local_context)

    def visit_compare(self, node, local_context):
        comparators = []
        for comparator in node.comparators:
            res = self.visit(comparator, local_context)
            if res:
                comparators.append(res)
        left = self.visit(node.left, local_context)
        if left:
            comparators.append(left)
        return comparators

    def visit_pass(self, node, local_context):
        pass


# Debug functions used to pretty print ast trees
def ast2tree(node, include_attrs=True):  # pragma: no cover
    def _transform(node):
        if isinstance(node, ast.AST):
            fields = ((a, _transform(b)) for a, b in ast.iter_fields(node))
            if include_attrs:
                attrs = (
                    (a, _transform(getattr(node, a)))
                    for a in node._attributes
                    if hasattr(node, a)
                )
                return node.__class__.__name__, dict(fields), dict(attrs)
            return node.__class__.__name__, dict(fields)
        elif isinstance(node, list):
            return [_transform(x) for x in node]
        elif isinstance(node, str):
            return repr(node)
        return node

    if not isinstance(node, ast.AST):
        raise TypeError("expected AST, got %r" % node.__class__.__name__)
    return _transform(node)


def pformat_ast(node, include_attrs=False, **kws):  # pragma: no cover
    return pprint.pformat(ast2tree(node, include_attrs), **kws)
