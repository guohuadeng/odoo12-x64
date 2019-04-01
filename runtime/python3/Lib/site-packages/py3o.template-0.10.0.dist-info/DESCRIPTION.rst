py3o.template
*************

.. image:: https://drone-ci.xcg.io/api/badges/faide/py3o.template/status.svg
  :target: https://drone-ci.xcg.io/faide/py3o.template
  :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/ambv/black
  :alt: Code Style: Black

Introduction
============

py3o is an elegant and scalable solution to design reports using LibreOffice.
py3o.template is the templating component that takes care of
merging your data sets with a corresponding templated OpenOffice document.

It is plateform independent and does not require LibreOffice/OpenOffice itself
to generate an ODF file.

Supported Python versions: 2.7, >= 3.5.

This work was originally inspired by `relatorio`_ and diverged in
implementation, scope and ambitions. Relatorio has many more features
when py3o.template is mainly focused on ODT, ODS and text output.

If you want to generate a PDF or any other supported output format you will then
need to have a server with either LibreOffice or OpenOffice and to install
the `py3o.renderserver`_ on it. We also provide a docker image on
the `docker hub`_

If you want to have templating fusion & document conversion in one
single web service usable from any language with just HTTP/POST you can install
`py3o.fusion`_ server. Which also exists as a `docker image`_

Full Documentation
==================

We `provide a documentation`_ for this package. If anything is not correctly
explained, please! create a ticket `in our ticketing system`_

Docs also contain a "Hacking" part for contributors (how tests are run, code
style...).

Example Usage
=============

Below is an example that you can find in the source code inside the examples
directory.

::

    from py3o.template import Template

    t = Template("py3o_example_template.odt", "py3o_example_output.odt")

    t.set_image_path('staticimage.logo', 'images/new_logo.png')


    class Item(object):
        pass

    items = list()

    item1 = Item()
    item1.val1 = 'Item1 Value1'
    item1.val2 = 'Item1 Value2'
    item1.val3 = 'Item1 Value3'
    item1.Currency = 'EUR'
    item1.Amount = '12345.35'
    item1.InvoiceRef = '#1234'
    items.append(item1)

    for i in xrange(1000):
        item = Item()
        item.val1 = 'Item%s Value1' % i
        item.val2 = 'Item%s Value2' % i
        item.val3 = 'Item%s Value3' % i
        item.Currency = 'EUR'
        item.Amount = '6666.77'
        item.InvoiceRef = 'Reference #%04d' % i
        items.append(item)

    document = Item()
    document.total = '9999999999999.999'

    data = dict(items=items, document=document)
    t.render(data)


Changelog
=========


0.10.0 2019-03-15
-----------------

  - Save embedded images into "Pictures" directory to work with lowriter>=6.0

  - Rely on `babel`_ to format dates & numbers from now on.

    -> ``format_date`` has been deprecated in favor of the new
       ``format_datetime``. Format specifiers change as well; see the
       "templating" doc. Example (more in docs)::

        function="format_datetime('2015-08-02 17:05:06', format='full', locale='fr_FR')"
            -> dimanche 2 août 2015 à 17:05:06 Temps universel coordonné

    -> ``format_amount`` & ``format_locale`` have been deprecated in favor of
       the new ``format_currency``. Example (more in the "templating" doc)::

        function="format_currency(123456789.4242, 'EUR', locale='fr_FR')"
            -> 123 456 789,42 €

  - Re-enable Python 3 in our test suite now that a recent ``genshi`` has been
    released.


0.9.13 2018-07-03
-----------------
  - Added a new format_locale function to supersed the format_amount
  - Keep aspect ratio of image if no width or height is given (thanks to
    Tom Gottfried)
  - fix generated VALUE formula, If the Genshi expressions generates a number
    value (float or integer), the generated formula will be `=VALUE("1.1")`
    which is problematic if the user machine is configured to use a decimal
    separator different than the `.`. With this fix the generated formula will
    be `=VALUE(1.1)` (without the quotes) which is correctly handled with
    by the `.ods` format. (thanks to Zakaria Makrelouf)
  - Improve error message 'We handle urls in tables or text paragraph only'
    (thanks to Alexis de Lattre)
  - Add format_multiline for support of new lines (thanks to John Asplin)


0.9.12 2018-04-11
-----------------

  - Better error reporting for cases when the link is not positionned
    on its own line.
  - Better error reporting for cases when an instruction link does not contain
    the equal sign.
  - Correct handling of images in odf 1.2 (thanks to Ari Caldeira)
  - Now support text:span in functions (thanks to John Asplin)

0.9.11 Dec. 16 2016
-------------------

  - Added support for escaping False values. Values evaluated as False are
    replaced with an empty string during template rendering. This
    functionality is disabled by default and can be enabled with a new
    parameter on the Template object.


0.9.10 Oct. 3 2016
------------------

  - Fixed a packaging issue (genshi requirement was unintentionally
    dropped in last release)
  - Added more tests
  - Added more support for types formatting

0.9.9 Apr. 13 2016
------------------

  - Template parser: fix multiple loops on the same list of objects
  - Template parser: fix multiple for loops on a variable that corresponds to a
    name (and not an attribute) in the data source.
  - Template parser: when parsing for loops, extract the iterator even when the
    assigned variables are not used anywhere in the body.
  - Template parser: now works with ODS templates.
  - Template parser: fix a bug when parsing an unknown ast expression.
  - Template parser: manage tuple, list and set literals.
  - Template parser: improve the parsing of loops where the iterator is a
    function.
  - Template parser: implement specific iteration behavior for enumerate.
    The second unpacked variable is linked to the function argument, as if
    the latter was used as the iterable object for the loop.
  - Image injection: fix an exception that was raided when the image is
    not present in the data dictionary, even when it shouldn't
    (template initialized with ignore_undefined_variables=True)
  - 100 % coverage, with many new unit tests and fixes on the old ones.

0.9.7.1 Feb. 19 2016
~~~~~~~~~~~~~~~~~~~~

  - This release fix a bug in the formatting function format_date where
    unicode date strings were not correctly managed.

0.9.7 Dec. 8 2015
~~~~~~~~~~~~~~~~~

  - This release focuses on the parser. If you
    don't use the template parser you can skip this release as it does not
    change anything else.
  - Fix a bug where the body of the if blocks were not evaluated
    by the parser
  - Refactoring tests for clearer reading
  - fix some missing/untested functions
  - remove NotImplementedError from coverage

0.9.6 Nov. 20 2015
~~~~~~~~~~~~~~~~~~

  - Fixed formatting function
  - Fixed if="" functionality that was not correctly parsed
  - Display empty string instead of "False" when browsing relational field
  - Code formatting in the ast parser

0.9.5 Oct. 30 2015
~~~~~~~~~~~~~~~~~~

  - 0.9.5 is just a rerelease of 0.9.4 with this README correctly
    amended...

  - Added support for formatting functions in the template in
    order to control date number localization
  - Added reference to original inspiration in the README
  - Added example source code for ODS output.
  - Fixed a memory usage in case of big output file size that
    was introduced by the dynamic image feature.
  - Introduced an experimental TextTemplate
  - Fixed support for special cases where page breaks removals
    removed trailing text (thanks to agix)

0.9.3 Jun. 26 2015
~~~~~~~~~~~~~~~~~~

  - Introduced dynamic image support (ie: pass in image data in the input
    iterator) and use it to insert images on the fly in the report)

0.9.2 Jun. 26 2015
~~~~~~~~~~~~~~~~~~

  - WARNING: if you used the old image replacement system, you
    need to update your code to set static image from this::

      # old way
      t.set_image_path('logo', 'images/new_logo.png')

      # You should now set it like this instead

      # new way. Note the 'staticimage.' prefix added just before 'logo'
      t.set_image_path('staticimage.logo', 'images/new_logo.png')

  - WARNING: after updating your code you must also update your template
    to prefix your static images names with the 'staticimage.' prefix.

  - Added dynamic images support. You can now add images instructions inside
    for loops or anywhere in your templates and pass the image data
    inside your objects attributes.
  - Added support for image data (dynamic ones) being passed-in as base64
    data. This is useful for some clients like `Odoo's report_py3o`_ because
    they store image data as base64 encoded fields.

.. _Odoo's report_py3o: https://bitbucket.org/xcg/report_py3o

0.9.1 Jun. 3 2015
~~~~~~~~~~~~~~~~~

  - Fixed parser to read from the var name instead of its description,
    if you dont use the helper tool to introspect your reports this release
    is of no importance to you as it only fixes this particular point.

0.9 Jan. 8 2015
~~~~~~~~~~~~~~~~

  - Added support for soft page breaks


0.8 Nov. 19 2014
~~~~~~~~~~~~~~~~

  - Added better unit tests
  - Fixed corner cases in the variable introspection mechanism
  - Better handling of "ignore_undefined" that now also allows undefined images

0.7 Oct. 15 2014
~~~~~~~~~~~~~~~~

  - Added Python3 support
  - Fixed a problem with validity of output in case the template contains
    a text:list inside a for loop
  - Added new public methods to help report servers introspect the template
    data dictionary
  - Added real unit tests (96% coverage ATM, way to go test team!)

Contributors
============

By order of contribution date:

  - `Florent Aide`_
  - `Emmanuel Cazenave`_
  - `jon1012`_
  - `Eugene Morozov`_
  - `Houzéfa Abbasbay`_
  - `Torsten Irländer`_
  - `Sergey Fedoseev`_
  - `Vincent Lhote-Hatakeyama`_
  - `Anael Lorimier`_
  - `Björn Ricks`_
  - `Agix`_
  - `Jérémie Gavrel`_
  - `Laurent Mignon`_
  - `Alexis de Lattre`_
  - `JosDeGraeve`_
  - `Antoine Nguyen`_
  - `Ari Caldeira`_
  - `John Asplin`_
  - `Zakaria Makrelouf`_
  - `Tom Gottfried`_

.. _Florent Aide: https://bitbucket.org/faide
.. _Emmanuel Cazenave: https://bitbucket.org/cazino
.. _jon1012: https://bitbucket.org/jon1012
.. _Eugene Morozov: https://bitbucket.org/mojo
.. _Houzéfa Abbasbay: https://bitbucket.org/houzefa-abba
.. _Torsten Irländer: https://bitbucket.org/ti
.. _Sergey Fedoseev: https://bitbucket.org/sir_sigurd
.. _Vincent Lhote-Hatakeyama: https://bitbucket.org/vincent_lhote
.. _Anael Lorimier: https://bitbucket.org/alorimier
.. _Björn Ricks: https://bitbucket.org/bjoernricks
.. _Agix: https://bitbucket.org/agix
.. _Jérémie Gavrel: https://bitbucket.org/gavrelj
.. _Laurent Mignon: https://bitbucket.org/lmi
.. _Alexis de Lattre: https://github.com/alexis-via
.. _JosDeGraeve: https://bitbucket.org/JosDeGraeve
.. _Antoine Nguyen: https://github.com/tonioo
.. _Ari Caldeira: https://bitbucket.org/ari_tauga
.. _John Asplin: https://bitbucket.org/asplinsolutions
.. _Zakaria Makrelouf https://bitbucket.org/z_makrelouf/
.. _Tom Gottfried https://bitbucket.org/tfried/

.. _py3o.renderserver: https://bitbucket.org/faide/py3o.renderserver/
.. _provide a documentation: http://py3otemplate.readthedocs.org
.. _in our ticketing system: https://bitbucket.org/faide/py3o.template/issues?status=new&status=open
.. _docker hub: https://registry.hub.docker.com/u/xcgd/py3oserver-docker/
.. _py3o.fusion: https://bitbucket.org/faide/py3o.fusion
.. _docker image: https://registry.hub.docker.com/u/xcgd/py3o.fusion
.. _relatorio: http://relatorio.tryton.org/
.. _babel: http://babel.pocoo.org


