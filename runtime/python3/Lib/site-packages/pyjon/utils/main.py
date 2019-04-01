"""utilities for pyjon
"""

import tempfile
import os
import re


def indent(elem, root_level=0):
    i = "\n" + root_level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, root_level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if root_level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def get_secure_filename(prefix="tmp", suffix=""):
    """creates a tempfile in the most secure manner possible,
    make sure is it closed and return the filename for
    easy usage.
    """
    file_handle, filename = tempfile.mkstemp(suffix=suffix, prefix=prefix)
    tmpfile = os.fdopen(file_handle, "r")
    tmpfile.close()
    return filename


class Singleton(type):
    """
    This is a neat singleton pattern. This was found in
     a comment on this page:
    http://www.garyrobinson.net/2004/03/python_singleto.html

    to use this, example :
    >>> class C(object):
    ...     __metaclass__ = Singleton
    ...     def __init__(self, foo):
    ...         self.foo = foo

    >>> C('bar').foo
    'bar'

    >>> C().foo
    'bar'

    and your class C is now a singleton, and it is safe to use the
     __init__ method as you usually do...
    """

    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    def __call__(mcs, *args, **kw):
        if mcs.instance is None:
            mcs.instance = super(Singleton, mcs).__call__(*args, **kw)

        return mcs.instance


def create_function(current_function, **options):
    """ This is an utility function that creates functions based on others.

    Examples :

    >>> range_5 = create_function(range, args=[5])
    >>> range_5()
    [0, 1, 2, 3, 4]

    >>> def argument_returner(*args):
    ...     ''' a function that just returns its args as a list '''
    ...     return list(args)
    >>> my_func = create_function(argument_returner, args=[1, '2'])
    >>> my_func()
    [1, '2']

    >>> my_other_func = create_function(argument_returner, args=[1, '2'],
    ...                                 caller_args_count=2)
    >>> my_other_func()
    Traceback (most recent call last):
        ...
    TypeError: function takes exactly 2 arguments (0 given)

    >>> my_other_func('foo', 'bar')
    ['foo', 'bar', 1, '2']
    """
    if options is None:
        options = dict()

    def composite_function(*args, **kwargs):
        out_args = list()
        args = list(args)
        given_args_length = len(args)

        opt = options.copy()

        if 'in_class' in opt:
            self = args.pop(0)
            out_args.append(self)
            del opt['in_class']

        if 'before_args' in opt:
            for arg in options['before_args']:
                out_args.append(arg)
            del opt['before_args']

        if 'caller_args_count' in opt:
            if not isinstance(options['caller_args_count'], int):
                raise ValueError('caller_args_count should be an integer')
            for i in range(options['caller_args_count']):
                try:
                    out_args.append(args.pop(0))
                except IndexError:
                    raise TypeError(
                        'function takes exactly %d arguments (%d given)' % (
                            options['caller_args_count'], given_args_length
                        )
                    )
            del opt['caller_args_count']

        if 'args' in opt:
            for arg in options['args']:
                out_args.append(arg)
            del opt['args']

        if 'kwargs' in options:
            out_kwargs = dict(kwargs, **options['kwargs'])
            del opt['kwargs']
        else:
            out_kwargs = kwargs

        if len(opt) >= 1:
            raise TypeError(
                "Arguments %s are not supported" % (
                    ', '.join(opt.keys())
                )
            )

        return current_function(*out_args, **out_kwargs)

    return composite_function


def substitute(string, callback, default='', regex=r"\{([^{}]+?)\}", sub_if_none=True):
    """Substitute keywords in a string using a callback function.
    Removes undefined keywords.

    :param string: the string in which keywords must be replaced
    :param callback: a keyword will be replaced by the return value of
                     callback(keyword)
    :param default: when the callback returns None, replace by default instead
    :param regex: the regex used to find the keywords
    :param sub_if_none: if True, try substituting by the default value when the
                        callback returns None

    Examples :

    >>> s = "foo {key1} baz {key2}"
    >>> d = dict(key1="bar", key2="toto", key3="plouf")
    >>> substitute(s, d.get)
    'foo bar baz toto'
    """
    result = string[:]

    try:
        # python 2.x
        if not isinstance(default, basestring):
            raise ValueError(
                "The default value must be a basestring, not a %s" % type(
                    default
                )
            )

    except NameError:

        # python 3.x
        if not isinstance(default, str):
            raise ValueError(
                "The default value must be a basestring, not a %s" % type(
                    default
                )
            )

    pattern = re.compile(regex)

    for match in pattern.finditer(string):
        rep = callback(match.group(1))

        try:
            # python 2.x
            rep_is_base = isinstance(rep, basestring)
        except NameError:
            # python 3.x
            rep_is_base = isinstance(rep, str)

        if rep is not None and not rep_is_base:
            raise ValueError(
                "The callback must return a basestring, not a %s" % type(rep)
            )

        if rep is not None or sub_if_none:
            if rep is None:
                rep = default

            result = result.replace(match.group(), rep)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
