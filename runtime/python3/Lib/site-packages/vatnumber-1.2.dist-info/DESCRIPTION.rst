vatnumber
=========

Python module to validate VAT numbers.

Nutshell
--------

Here a simple example to validate VAT numbers format::

    >>> import vatnumber
    >>> vatnumber.check_vat('BE0123456749')
    True

Here a simple example to validate European VAT through VIES service::

    >>> import vatnumber
    >>> vatnumber.check_vies('BE0897290877')
    True


For more information please visit the `vatnumber website`_.

.. _vatnumber website: http://code.google.com/p/vatnumber/


