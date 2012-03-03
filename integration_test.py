import os, sys, inspect
import unittest
import dbus

class GestaltIntegration(unittest.TestCase):
    def test_gestalt(self):
        bus = dbus.SessionBus()
        gestalt = bus.get_object('org.mpris.MediaPlayer2.Gestalt',
                '/org/mpris/MediaPlayer2/Gestalt')
        gestalt_hello = gestalt.get_dbus_method('hello',
                'org.mpris.MediaPlayer2')
        assert gestalt_hello() == 'Gestalt!'

    def test_play(self):
        bus = dbus.SessionBus()
        gestalt = bus.get_object('org.mpris.MediaPlayer2.Gestalt',
                '/org/mpris/MediaPlayer2/Gestalt')
        gestalt_play = gestalt.get_dbus_method('play',
                'org.mpris.MediaPlayer2.Player')


