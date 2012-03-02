import dbus
import dbus.service
import dbus.glib
import sys

ROOT_IFACE = 'org.mpris.MediaPlayer2'
PLAYER_IFACE = 'org.mpris.MediaPlayer2.Player'
PLIST_IFACE = 'org.mpris.MediaPlayer2.Playlist'
BUS_NAME =  'org.mpris.MediaPlayer2.Gestalt'
OBJECT_PATH = '/org/mpris/MediaPlayer2/Gestalt'


class GestaltBus(dbus.service.Object):

    
    def __init__(self):

        bus_name = dbus.service.BusName(BUS_NAME, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name=bus_name, object_path=OBJECT_PATH)

    def mset(self, interface_name, properties):
        self.props[interface_name].update(properties)
        self.PropertiesChanged(interface_name, properties, [])

    # root interface (org.mpris.MediaPlayer2)
    
    @dbus.service.method(dbus_interface=ROOT_IFACE)
    def hello(self):
        return "Gestalt!"
    
    @dbus.service.method(dbus_interface=ROOT_IFACE)
    def Quit(self):
        # not sure how to make this work, sys.exit will quit (with errors)
        #gtk.main_quit()
        sys.exit()
    
    @dbus.service.method(dbus_interface=ROOT_IFACE)
    def Raise(self):
        # Do nothing (CanRaise is false)
        pass

    # player interface (org.mpris.MediaPlayer2.Player)

    @dbus.service.method(dbus_interface=PLAYER_IFACE)
    def Play(self):
        #gestalt.play()
        pass


