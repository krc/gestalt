import gobject
import gtk
import gestaltbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject

def main():
    DBusGMainLoop(set_as_default=True)
    GestaltBus()
    loop = gobject.MainLoop()
    loop.run()

    #gtk.main()

if __name__ == '__main__':
    main()


