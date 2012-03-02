# consumeservice.py
# consumes a method in a service on the dbus
 
import dbus
  
bus = dbus.SessionBus()
helloservice = bus.get_object('org.mpris.MediaPlayer2.Gestalt', '/org/mpris/MediaPlayer2/Gestalt')
hello = helloservice.get_dbus_method('hello', 'org.mpris.MediaPlayer2')
print hello()
