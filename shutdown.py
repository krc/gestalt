import dbus

bus = dbus.SessionBus()
gestalt = bus.get_object('org.mpris.MediaPlayer2.gestalt', '/org/mpris/MediaPlayer2/gestalt')
gestalt_quit = gestalt.get_dbus_method('hello', 'org.mpris.MediaPlayer2.gestalt')
gestalt_quit()
