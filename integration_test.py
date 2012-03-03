import os, sys, inspect
import unittest
import dbus

class GestaltIntegration(unittest.TestCase):
  def testGestalt(self):
    bus = dbus.SessionBus()
    gestalt = bus.get_object('org.mpris.MediaPlayer2.Gestalt',
            '/org/mpris/MediaPlayer2/Gestalt')
    gestalt_hello = gestalt.get_dbus_method('hello',
            'org.mpris.MediaPlayer2')
    assert gestalt_hello() == 'Gestalt!'
