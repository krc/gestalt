import gobject
from dbus.mainloop.glib import DBusGMainLoop
from gestaltbus import GestaltBus

def main():
    DBusGMainLoop(set_as_default=True)
    GestaltBus()
    loop = gobject.MainLoop()
    loop.run()

    #gtk.main()

if __name__ == '__main__':
    main()


