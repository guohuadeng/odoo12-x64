"""Convert numbers from any base to any other base.

This is based on the work by wanyewon (PSF license):
    http://code.activestate.com/recipes/65212/#c9
"""


def decimal_to_n(
        num, base_to, numerals="0123456789abcdefghijklmnopqrstuvwxyz"
):
    """Convert a decimal integer to a string representing the same number in
    another base/radix.

    Special numerals need to be supplied to convert to any base or radix
    greater than 36.

    This function is essentially an inverse of int(s, base).

    @param num: the decimal integer to convert
    @type num: int

    @param base_to: the base to convert to
    @type base_to: int

    @param numerals: the list of symbols to use in the destination base
    @type numerals: string

    Usage examples:
    >>> decimal_to_n(-13, 4)
    '-31'
    >>> decimal_to_n(91321, 2)
    '10110010010111001'
    >>> decimal_to_n(91321, 2, numerals="ab")
    'babbaabaababbbaab'
    """
    if num == 0:
        return "0"

    if num < 0:
        return '-' + decimal_to_n((-1) * num, base_to, numerals)

    if not 2 <= base_to <= len(numerals):
        raise ValueError('Base must be between 2-%d' % len(numerals))

    left_digits = num // base_to
    if left_digits == 0:
        return numerals[num % base_to]
    else:
        return decimal_to_n(left_digits, base_to, numerals) + numerals[num % base_to]


def n_to_m(
        num, base_from, base_to,
        numerals_to="0123456789abcdefghijklmnopqrstuvwxyz"
):
    """Convert a string representing a number in any given base/radix to a
    string representing the same number in another base/radix.

    Special numerals need to be supplied to convert to any base or radix
    greater than 36.

    @param num: the number to convert in the base_from base
    @type num: string

    @param base_from: the base to convert from. For now, this parameter
                      can *not* have a value greater than 36
    @type base_from: int

    @param base_to: the base to convert to
    @type base_to: int

    @param numerals: the list of symbols to use in the destination base
    @type numerals: string

    Usage examples:
    >>> n_to_m("a1", 16, 2)
    '10100001'
    >>> n_to_m("231", 8, 2, numerals_to="ab")
    'baabbaab'
    """
    if not 2 <= base_from <= 36:
        raise ValueError(
            "The base_from parameter must be between 2 and 36"
        )

    if not 2 <= base_to <= len(numerals_to):
        raise ValueError(
            "The base_to parameter must be between 2 and %s" % len(numerals_to)
        )

    dec_num = int(num, base_from)

    return decimal_to_n(dec_num, base_to, numerals_to)
