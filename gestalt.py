import dbus
import dbus.service
import dbus.glib

class Gestalt(dbus.service.Object):
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
        gtk.main_quit()

   # def StringifyVariant(self, var):
   #     self.LastInputChanged(var)      # emits the signal
   #     return str(var)

   # @dbus.service.signal(INTERFACE,
   #                      signature='v')
   # def LastInputChanged(self, var):
   #     # run just before the signal is actually emitted
   #     # just put "pass" if nothing should happen
   #     self._last_input = var

   #  @dbus.service.method(INTERFACE,
   #                      in_signature='', out_signature='v')
   # def GetLastInput(self):
   #     return self._last_input
