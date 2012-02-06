import gobject
import gtk
from gestaltbus import GestaltBus
from dbus.mainloop.glib import DBusGMainLoop

def main():
    DBusGMainLoop(set_as_default=True)
    GestaltBus()
    gtk.main()

if __name__ == '__main__':
    main()


