#This file is part of vatnumber.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Check the VAT number depending of the country based on formula from
http://sima-pc.com/nif.php (dead link, was http://web.archive.org/web/20120118023804/http://sima-pc.com/nif.php)
http://en.wikipedia.org/wiki/Vat_number
'''
__version__ = '1.2'


def _posint(x):
    value = int(x)
    if value < 0:
        raise ValueError('not a positive integer')
    return value


def countries():
    '''
    Return the list of country's codes that have check function
    '''
    res = [x.replace('check_vat_', '').upper() for x in globals()
        if x.startswith('check_vat_')]
    res.sort()
    return res


def mult_add(i, j):
    '''
    Sum each digits of the multiplication of i and j.
    '''
    mult = i * j
    res = 0
    for i in range(len(str(mult))):
        res += int(str(mult)[i])
    return res


def mod1110(value):
    '''
    Compute ISO 7064, Mod 11,10
    '''
    t = 10
    for i in value:
        c = int(i)
        t = (2 * ((t + c) % 10 or 10)) % 11
    return (11 - t) % 10


def check_vat_at(vat):
    '''
    Check Austria VAT number.
    '''
    import stdnum.at.uid
    return stdnum.at.uid.is_valid(vat)


def check_vat_al(vat):
    '''
    Check Albania VAT number.
    '''
    if len(vat) != 10:
        return False
    if vat[0] not in ('J', 'K'):
        return False
    try:
        _posint(vat[1:9])
    except ValueError:
        return False
    if ord(vat[9]) < 65 or ord(vat[9]) > 90:
        return False
    return True


def check_vat_ar(vat):
    '''
    Check Argentina VAT number.
    '''
    if len(vat) != 11:
        return False
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in xrange(10):
        aux += int(vat[i]) * base[i]
    aux = 11 - (aux - (int(aux / 11) * 11))
    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9
    return aux == int(vat[10])


def check_vat_be(vat):
    '''
    Check Belgium VAT number.
    '''
    import stdnum.be.vat
    return stdnum.be.vat.is_valid(vat)


def check_vat_bg(vat):
    '''
    Check Bulgaria VAT number.
    '''
    import stdnum.bg.vat
    return stdnum.bg.vat.is_valid(vat)


def check_vat_cl(rut):
    '''
    Check Chile RUT number.
    '''
    try:
        _posint(rut[:-1])
    except ValueError:
        return False
    sum = 0
    for i in range(len(rut) - 2, -1, -1):
        sum += int(rut[i]) * (((len(rut) - 2 - i) % 6) + 2)
    check = 11 - (sum % 11)
    if check == 11:
        return rut[-1] == '0'
    elif check == 10:
        return rut[-1].upper() == 'K'
    else:
        return check == int(rut[-1])


def check_vat_co(rut):
    '''
    Check Colombian RUT number.
    '''
    if len(rut) != 10:
        return False
    try:
        _posint(rut)
    except ValueError:
        return False
    nums = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
    sum = 0
    for i in range(len(rut) - 2, -1, -1):
        sum += int(rut[i]) * nums[len(rut) - 2 - i]
    if sum % 11 > 1:
        return int(rut[-1]) == 11 - (sum % 11)
    else:
        return int(rut[-1]) == sum % 11


def check_vat_cy(vat):
    '''
    Check Cyprus VAT number.
    '''
    import stdnum.cy.vat
    return stdnum.cy.vat.is_valid(vat)


def check_vat_cz(vat):
    '''
    Check Czech Republic VAT number.
    '''
    import stdnum.cz.dic
    return stdnum.cz.dic.is_valid(vat)


def check_vat_de(vat):
    '''
    Check Germany VAT number.
    '''
    import stdnum.de.vat
    return stdnum.de.vat.is_valid(vat)


def check_vat_dk(vat):
    '''
    Check Denmark VAT number.
    '''
    import stdnum.dk.cvr
    return stdnum.dk.cvr.is_valid(vat)


def check_vat_ee(vat):
    '''
    Check Estonia VAT number.
    '''
    import stdnum.ee.kmkr
    return stdnum.ee.kmkr.is_valid(vat)


def check_vat_es(vat):
    '''
    Check Spain VAT number.
    '''
    import stdnum.es.nif
    return stdnum.es.nif.is_valid(vat)


def check_vat_fi(vat):
    '''
    Check Finland VAT number.
    '''
    import stdnum.fi.alv
    return stdnum.fi.alv.is_valid(vat)


def check_vat_fr(vat):
    '''
    Check France VAT number.
    '''
    import stdnum.fr.tva
    return stdnum.fr.tva.is_valid(vat)


def check_vat_gb(vat):
    '''
    Check United Kingdom VAT number.
    '''
    import stdnum.gb.vat
    return stdnum.gb.vat.is_valid(vat)


def check_vat_gr(vat):
    '''
    Check Greece VAT number.
    '''
    import stdnum.gr.vat
    return stdnum.gr.vat.is_valid(vat)


def check_vat_el(vat):
    '''
    Check Greece VAT number.
    '''
    return check_vat_gr(vat)


def check_vat_hr(vat):
    '''
    Check Croatia VAT number.
    '''
    import stdnum.hr.oib
    return stdnum.hr.oib.is_valid(vat)


def check_vat_hu(vat):
    '''
    Check Hungary VAT number.
    '''
    import stdnum.hu.anum
    return stdnum.hu.anum.is_valid(vat)


def check_vat_ie(vat):
    '''
    Check Ireland VAT number.
    '''
    import stdnum.ie.vat
    return stdnum.ie.vat.is_valid(vat)


def check_vat_it(vat):
    '''
    Check Italy VAT number.
    '''
    import stdnum.it.iva
    return stdnum.it.iva.is_valid(vat)


def check_vat_lt(vat):
    '''
    Check Lithuania VAT number.
    '''
    import stdnum.lt.pvm
    return stdnum.lt.pvm.is_valid(vat)


def check_vat_lu(vat):
    '''
    Check Luxembourg VAT number.
    '''
    import stdnum.lu.tva
    return stdnum.lu.tva.is_valid(vat)


def check_vat_lv(vat):
    '''
    Check Latvia VAT number.
    '''
    import stdnum.lv.pvn
    return stdnum.lv.pvn.is_valid(vat)


def check_vat_mt(vat):
    '''
    Check Malta VAT number.
    '''
    import stdnum.mt.vat
    return stdnum.mt.vat.is_valid(vat)


def check_vat_nl(vat):
    '''
    Check Netherlands VAT number.
    '''
    import stdnum.nl.btw
    return stdnum.nl.btw.is_valid(vat)


def check_vat_pl(vat):
    '''
    Check Poland VAT number.
    '''
    import stdnum.pl.nip
    return stdnum.pl.nip.is_valid(vat)


def check_vat_pt(vat):
    '''
    Check Portugal VAT number.
    '''
    import stdnum.pt.nif
    return stdnum.pt.nif.is_valid(vat)


def check_vat_ro(vat):
    '''
    Check Romania VAT number.
    '''
    import stdnum.ro.cf
    return stdnum.ro.cf.is_valid(vat)


def check_vat_se(vat):
    '''
    Check Sweden VAT number.
    '''
    import stdnum.se.vat
    return stdnum.se.vat.is_valid(vat)


def check_vat_si(vat):
    '''
    Check Slovenia VAT number.
    '''
    import stdnum.si.ddv
    return stdnum.si.ddv.is_valid(vat)


def check_vat_sk(vat):
    '''
    Check Slovakia VAT number.
    '''
    import stdnum.sk.dph
    return stdnum.sk.dph.is_valid(vat)


def check_vat_sm(vat):
    '''
    Check San Marino VAT number.
    '''
    if len(vat) != 5:
        return False
    try:
        _posint(vat)
    except ValueError:
        return False
    return True


def check_vat_ua(vat):
    '''
    Check Ukraine VAT number.
    '''
    if len(vat) != 8:
        return False
    try:
        _posint(vat)
    except ValueError:
        return False
    return True


def check_vat_uk(vat):
    '''
    Check United Kingdom VAT number.
    '''
    return check_vat_gb(vat)


def check_vat_ru(vat):
    '''
    Check Russia VAT number.
    '''
    if len(vat) != 10 and len(vat) != 12:
        return False
    try:
        _posint(vat)
    except ValueError:
        return False

    if len(vat) == 10:
        check_sum = 2 * int(vat[0]) + 4 * int(vat[1]) + 10 * int(vat[2]) + \
            3 * int(vat[3]) + 5 * int(vat[4]) + 9 * int(vat[5]) + \
            4 * int(vat[6]) + 6 * int(vat[7]) + 8 * int(vat[8])
        check = check_sum % 11
        if check % 10 != int(vat[9]):
            return False
    else:
        check_sum1 = 7 * int(vat[0]) + 2 * int(vat[1]) + 4 * int(vat[2]) + \
            10 * int(vat[3]) + 3 * int(vat[4]) + 5 * int(vat[5]) + \
            9 * int(vat[6]) + 4 * int(vat[7]) + 6 * int(vat[8]) + \
            8 * int(vat[9])
        check = check_sum1 % 11

        if check != int(vat[10]):
            return False
        check_sum2 = 3 * int(vat[0]) + 7 * int(vat[1]) + 2 * int(vat[2]) + \
            4 * int(vat[3]) + 10 * int(vat[4]) + 3 * int(vat[5]) + \
            5 * int(vat[6]) + 9 * int(vat[7]) + 4 * int(vat[8]) + \
            6 * int(vat[9]) + 8 * int(vat[10])
        check = check_sum2 % 11
        if check != int(vat[11]):
            return False
    return True


def check_vat(vat):
    '''
    Check VAT number.
    '''
    code = vat[:2].lower()
    number = vat[2:]
    try:
        checker = globals()['check_vat_%s' % code]
    except KeyError:
        return False
    return checker(number)


def check_vies(vat):
    '''
    Check VAT number for EU member state using the SOAP Service
    '''
    import stdnum.eu.vat
    return bool(stdnum.eu.vat.check_vies(vat)['valid'])
