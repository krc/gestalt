# consumeservice.py
# consumes a method in a service on the dbus
 
import dbus
import sys 

arg = sys.argv[1]

bus = dbus.SessionBus()
service = bus.get_object('org.mpris.MediaPlayer2.Gestalt', '/org/mpris/MediaPlayer2/Gestalt')

hello = service.get_dbus_method('hello', 'org.mpris.MediaPlayer2')
quit = service.get_dbus_method('Quit', 'org.mpris.MediaPlayer2' )
Play = service.get_dbus_method('Play', 'org.mpris.MediaPlayer2.Player')

if arg == "hello":
    print hello()
elif arg == "bye":
    quit()
else:
    Play(arg)


