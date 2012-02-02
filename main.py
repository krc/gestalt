import dbus
import dbus.service
import dbus.glib
import gobject
import gtk
from dbus.mainloop.glib import DBusGMainLoop

class Gestalt(dbus.service.Object):
    GESTALT_INTERFACE = 'org.mpris.MediaPlayer2.gestalt'

    def __init__(self):
        bus_name = dbus.service.BusName('org.mpris.MediaPlayer2.gestalt', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/mpris/MediaPlayer2/gestalt')

    @dbus.service.method('org.mpris.MediaPlayer2.gestalt')
    def hello(self):
        return "Gestalt!"

   # def StringifyVariant(self, var):
   #     self.LastInputChanged(var)      # emits the signal
   #     return str(var)

   # @dbus.service.signal(GESTALT_INTERFACE,
   #                      signature='v')
   # def LastInputChanged(self, var):
   #     # run just before the signal is actually emitted
   #     # just put "pass" if nothing should happen
   #     self._last_input = var

   #  @dbus.service.method(GESTALT_INTERFACE,
   #                      in_signature='', out_signature='v')
   # def GetLastInput(self):
   #     return self._last_input

DBusGMainLoop(set_as_default=True)
myservice = Gestalt()
gtk.main()
