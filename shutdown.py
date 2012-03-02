import dbus

bus = dbus.SessionBus()
gestalt = bus.get_object('org.mpris.MediaPlayer2.Gestalt', '/org/mpris/MediaPlayer2/Gestalt')
gestalt_quit = gestalt.get_dbus_method('Quit', 'org.mpris.MediaPlayer2')
gestalt_quit()
