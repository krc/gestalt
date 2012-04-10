import gobject
from dbus.mainloop.glib import DBusGMainLoop
from gestaltbus import GestaltBus
from gestaltplayer import GestaltPlayer

def main():
    DBusGMainLoop(set_as_default=True)
    player = GestaltPlayer()
    GestaltBus(player)
    loop = gobject.MainLoop()
    loop.run()


if __name__ == '__main__':
    main()


