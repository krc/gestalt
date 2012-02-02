import dbus
import dbus.service
import dbus.glib
import gobject
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

class Gestalt(dbus.service.Object):
    GESTALT_INTERFACE = 'org.mpris.MediaPlayer2.gestalt'

    def __init__(self, object_path):
        dbus.service.Object.__init__(self, dbus.SessionBus(), path)
        self._last_input = None

    @dbus.service.method(GESTALT_INTERFACE,
                         in_signature='v', out_signature='s')
    def StringifyVariant(self, var):
        self.LastInputChanged(var)      # emits the signal
        return str(var)

    @dbus.service.signal(GESTALT_INTERFACE,
                         signature='v')
    def LastInputChanged(self, var):
        # run just before the signal is actually emitted
        # just put "pass" if nothing should happen
        self._last_input = var

    @dbus.service.method(GESTALT_INTERFACE,
                         in_signature='', out_signature='v')
    def GetLastInput(self):
        return self._last_input


loop = gobject.MainLoop()
loop.run()



loop.quit()
