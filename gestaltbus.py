import dbus
import dbus.service
import dbus.glib
import sys

class GestaltBus(dbus.service.Object):
    INTERFACE = 'org.mpris.MediaPlayer2.gestalt'
    BUS = '/org/mpris/MediaPlayer2/gestalt'

    def __init__(self):
        bus_name = dbus.service.BusName(self.INTERFACE, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, self.BUS)

    @dbus.service.method(INTERFACE)
    def hello(self):
        return "Gestalt!"

    @dbus.service.method(INTERFACE)
    def quit(self):
        # not sure how to make this work, sys.exit will quit (with errors)
        #gtk.main_quit()
        sys.exit()

