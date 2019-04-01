"""This file contains all the data structures used by Py3oConvertor
See the docstring of Py3oConvertor.__call__() for further information
"""
from numbers import Number


class Py3oDataError(Exception):
    pass


class Py3oObject(dict):
    """ Base class to be inherited.
    """

    is_list = False

    def render(self, data):  # pragma: no cover
        raise NotImplementedError("This function should be overriden")

    def __repr__(self):  # pragma: no cover
        res = super(Py3oObject, self).__repr__()
        return "{}({})".format(self.__class__.__name__, res)

    def get_size(self):
        """Return the max depth of the object
        """
        sizes = [val.get_size() for val in self.values()]
        if not sizes:
            return 0
        return max(sizes) + 1

    def get_key(self):
        """Return the first key
        """
        return next(iter(self.keys()))

    def get_tuple(self):
        """Return the value of the Py3oObject as a tuple.
        As a default behavior, the object returns None.
        """
        return None

    def unpack(self, target):
        self_tup = self.get_tuple()
        target_tup = target.get_tuple()
        if target_tup is None:
            yield (target, self)
        elif self_tup is None:
            yield (None, self)
            array = self[self.get_key()]
            array.is_list = True
            for i, target_elem in enumerate(target_tup):
                self[self.get_key()] = tmpname = Py3oName({i: Py3oName()})
                yield (target_elem, self)
                array[i] = tmpname[i]
            self[self.get_key()] = array
        else:
            diff = len(target_tup) - len(self_tup)
            if diff != 0:  # pragma: no cover
                raise ValueError(
                    u"Unpack Error: {} != {}".format(target_tup, self_tup)
                )
            for t in zip(target_tup, self_tup):
                yield t

    def rupdate(self, other):
        """Update recursively the Py3oObject self with the Py3oObject other.
        Example:
        self = Py3oObject({
            'a': Py3oObject({}),
            'b': Py3oObject({
                'c': Py3oObject({}),
            }),
        })
        other = Py3oObject({
            'b': Py3oObject({
                'd': Py3oObject({}),
            }),
        })
        res = Py3oObject({
            'a': Py3oObject({}),
            'b': Py3oObject({
                'c': Py3oObject({}),
                'd': Py3oObject({}),
            }),
        })
        """
        for key, value in other.items():
            if key in self:
                self[key].rupdate(value)
            else:
                self[key] = value

    def rget(self, other):
        """Get the value for the path described by the other Py3oObject.

        Recursively checks that the values in other can be found in self.

        The method returns the values of self and other at the point where
        the search stopped.
        If other is a leaf, the search stops sucessfully. The method returns
        True, the value that corresponds to the path described by other, and
        the leaf in question.
        If other cannot be found in self, the search stops unsuccessfully.
        The method returns False, the value that corresponds to the deepest
        point reached in self, and the rest of the path.

        Example:
        self = Py3oObject({
            'a': Py3oObject({}),
            'b': Py3oObject({
                'c': Py3oObject({}),
            }),
        })
        other = Py3oObject({
            'b': Py3oObject({
                'd': Py3oObject({}),
            }),
        })
        res = (
            False,
            Py3oObject({'c': Py3oObject({})}),  # is self['b']
            Py3oObject({'d': Py3oObject({})}),  # is other['b']
        )
        if other['b'] was a leaf, res[0] would be True and res[2] the leaf.

        :return: A triple:
          - True if the search was successful, False otherwise
          - The active sub-element of self when the search stopped
          - The active sub-element of other when the search stopped
        """
        if not other:
            return True, self, other
        other_key = other.get_key()
        if other_key in self:
            return self[other_key].rget(other[other_key])
        else:
            return False, self, other

    def render_children(self, data):
        if self.is_list:
            res = [self[i].render(item) for i, item in enumerate(data)]
        else:
            res = {
                key: value.render(getattr(data, key))
                for key, value in self.items()
            }
        return res


class Py3oModule(Py3oObject):
    def render(self, data):
        """ This function will render the datastruct according
         to the user's data
        """
        res = {}
        for key, value in self.items():
            subdata = data.get(key, None)
            if subdata is None:
                raise Py3oDataError(
                    "The key '%s' must be present"
                    " in your data dictionary" % key
                )
            # Spread only the appropriate data to its children
            val = value.render(data.get(key))
            if val is not None:
                res[key] = val
        return res


class Py3oArray(Py3oObject):
    """ A class representing an iterable value in the data structure.
    The attribute direct_access will tell if this class should be considered
     as a list of dict or a list of values.
    """

    def __init__(self):
        super(Py3oArray, self).__init__()
        self.direct_access = False

    def render(self, data):
        """ This function will render the datastruct according
        to the user's data
        """
        if self.direct_access:
            res = data
        elif not self:  # pragma: no cover
            res = None
        else:
            res = [self.render_children(d) for d in data]
        return res


class Py3oName(Py3oObject):
    """ This class holds information of variables.
    Keys are attributes and values the type of this attribute
     (another Py3o class or a simple value)
    i.e.: i.egg -> Py3oName({'i': Py3oName({'egg': Py3oName({})})})
    """

    def render(self, data):
        """ This function will render the datastruct according
        to the user's data
        """
        if not self:
            # We only send False values if the value is a number
            # otherwise we convert the False into an empty string
            res = data if data or isinstance(data, Number) else u""
        else:
            res = self.render_children(data)
        return res


class Py3oCall(Py3oObject):
    """This class holds information of function call.
    'name' holds the name of function as a Py3oName
    The keys are the arguments as:
        - numeric keys are positional arguments ordered ascendently
        - string keys are keywords arguments
    """

    return_format = None

    def __init__(self, name, dict):
        super(Py3oCall, self).__init__(dict)
        self.name = name

    def get_tuple(self):  # pragma: no cover
        raise SyntaxError(u"Can't assign to function call")

    def unpack(self, target):
        target_tup = target.get_tuple()
        args = set(self.keys())

        if self.return_format is None:
            # Generic/unknown function, do not make assumptions about targets
            res = [(target_it, None) for target_it in target_tup]
            res += [(None, self[arg]) for arg in args]

        elif isinstance(self.return_format, tuple):
            # Bind targets to function arguments according to return_format
            return_value = []
            for return_var in self.return_format:
                if return_var is None:
                    return_value.append(Py3oDummy())
                else:
                    return_value.append(self.get(return_var, None))

            if len(return_value) == len(target_tup):
                res = zip(target_tup, return_value)

            # TODO: Manage Py3oContainer values inside for loop body
            # elif len(target_tup) == 1:
            #     res = [(target_tup[0], Py3oContainer(return_value))]
            #     res += [(self[arg], None) for arg in args]

            else:  # pragma: no cover
                raise ValueError(u"Unpack Error")

        else:
            # Single return value is bound to one of the arguments.
            res = [(target, self.get(self.return_format, None))]

        for tup in res:
            yield tup


class Py3oEnumerate(Py3oCall):
    """Represent an enumerate call"""

    return_format = (None, 0)


class Py3oContainer(Py3oObject):
    """Represent a container defined in the template.
    This container can be:
    _ A literal list, tuple, set or dict definition
    _ A tuple of variables that are the target of an unpack assignment
    """

    def __init__(self, values):
        super(Py3oContainer, self).__init__()
        self.values = values

    def get_tuple(self):
        """Return the container's values in a tuple"""
        return tuple(self.values)


class Py3oDummy(Py3oObject):
    """ This class holds temporary dict, or unused attribute
     such as counters from enumerate()
    """

    pass


class Py3oBuiltin(Py3oObject):
    """ This class holds information about builtins
    """

    builtins = {"enumerate": Py3oEnumerate}

    @classmethod
    def from_name(cls, name=None):
        """Return the Py3oObject subclass for the given built-in name
        Return None if the name does not correspond to a builtin.

        :param name: A Py3oObject instance that represent a name/attribute path
        :return: A Py3oObject subclass or None
        """
        name_key = name.get_key()
        builtin = cls.builtins.get(name_key)
        # TODO: uncomment to implement standard modules in cls.builtins
        # if builtin and name.get_size() > 1:
        #     if isinstance(builtin, Py3oBuiltin):
        #         builtin = builtin.from_name(name[name_key])
        #     else:
        #     builtin = None
        return builtin
