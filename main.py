import gobject
import gtk
from gestalt import Gestalt
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)
myservice = Gestalt()
gtk.main()
