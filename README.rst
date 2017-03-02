Vortex
======

Jump to directories.

Installation (with epm)
-----------------------

Just run

.. code::

   epm install vortex

Installation (without epm)
--------------------------

Download :code:`vortex.py` and place it in :code:`~/.ergo/packages`.


Usage
-----

Vortexing to a point
~~~~~~~~~~~~~~~~~~~~

To vortex to point :code:`point`, run

.. code::

   vortex point

Setting vortex points
~~~~~~~~~~~~~~~~~~~~~

To set points :code:`p1,p2,...` to directories :code:`d1,d2,...`, run

.. code::

   vortex_set {p1:d1,p2:d2,...}

Listing vortex points
~~~~~~~~~~~~~~~~~~~~~

Just use the :code:`vortex_list` command, like so

.. code::

   $ vortex_list
   i3 -> /home/lschumm/.config/i3/
   e -> /home/lschumm/mtklabs/ergonomica/ergonomica
   t -> /home/lschumm/teenmade
   w -> /home/lschumm/Pictures/Wallpapers
   
Removing vortex points
~~~~~~~~~~~~~~~~~~~~~~

To remove vortex points :code:`p1,p2,...`, run

.. code::

   vortex_remove p1 p2,...

For example,

.. code::

   $ vortex_list
   i3 -> /home/lschumm/.config/i3/
   e -> /home/lschumm/mtklabs/ergonomica/ergonomica
   t -> /home/lschumm/teenmade
   w -> /home/lschumm/Pictures/Wallpapers
   $ vortex_remove i3
   $ vortex_list
   e -> /home/lschumm/mtklabs/ergonomica/ergonomica
   t -> /home/lschumm/teenmade
   w -> /home/lschumm/Pictures/Wallpapers


Credits
=======

This project was inspired by `@mfaerevaag`_ 's `wd`_.

.. _@mfaerevaag: https://github.com/mfaerevaag

.. _wd: https://github.com/mfaerevaag/wd

