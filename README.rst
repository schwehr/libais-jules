============
Introduction
============

Library for decoding maritime Automatic Identification System messages.

See Also
========

`Automatic Identification System <http://en.wikipedia.org/wiki/Automatic_Identification_System>`_

Other open source AIS projects:

- `GPSd <http://en.wikipedia.org/wiki/Gpsd>`_
- `AisLib <https://github.com/dma-ais/AisLib>`_
- `noaadata <http://github.com/schwehr/noaadata>`_
- `ais-areanotice <https://github.com/schwehr/ais-areanotice-py>`_
- `OpenCPN <https://github.com/OpenCPN/OpenCPN>`_
- `aisparser <https://github.com/bcl/aisparser>`_
- `nmea_plus <https://github.com/ifreecarve/nmea_plus>`_

Building
========

Building with Python
--------------------

.. code-block:: console

    $ python setup.py build
    $ python setup.py install

Testing with Python
--------------------

.. code-block:: console

    $ virtualenv ve
    $ source ve/bin/activate
    $ python setup.py test

Building with CMake
-------------------

.. code-block:: console

    $ cmake -GNinja .
    $ TODO


Usage
=====


AIS Specification Documents
---------------------------

- ITU-1371, ITU-1371-{1,2,3,4]
- `e-Navigation <http://www.e-navigation.nl/asm>`_
- IMO Circ 236
- IMO Circ 289
- EU RIS

Developing
----------

