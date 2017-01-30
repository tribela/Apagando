Apagando
========

Simple Smart Switch for lights.

*Apagando* means *Turning off* in Spanish.
I named it this because inpired by *Sombra* in *Overwatch*. Their ultimate
voiceline is "¡Apagando las luces!" which means "Turning off the lights".


Hardware requirements
---------------------

I use `Onion Omega 2 Plus`_ to make this.

- `Onion Omega 2 Plus`_.
- 2 relay switch.
- 3 way light switch (for manually control).

.. _Onion Omega 2 Plus: https://onion.io/


Software requirements
---------------------

.. code-block:: console

   $ opkg install python-light python-pip pyOnionGpio
   $ pip install -r requirements.txt
   # Run apagando on boot
   $ ln -sf $PWD/start.sh /etc/rc.d/S99apagando


Configuration
-------------

Edit ``.env`` to configuration

.. code-block:: sh

   # Relay's GPIO ports.
   RELAY0=17
   RELAY1=15

   # Physical switch's GPIO ports.
   SWITCH0=0
   SWITCH1=1
