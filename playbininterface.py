import glib
import gobject
import gst

class PlaybinInterface:
    def __init__(self):
        self.idle = True # not playing at the moment
        # create a playbin2 pipe
        self.player = gst.element_factory_make("playbin2", "player")
        # toss out video, just in case
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)
        # connect a signal handler to it's bus
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)

    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.idle = True
        elif t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            print >> sys.stderr, "Error: {0} {1}".format(err, debug)
            self.player.set_state(gst.STATE_NULL)
            self.idle = True
        return self.idle

    def play(self, uri):
        # abort previous play if still busy
        if not self.idle:
            print >> sys.stderr, 'audio truncated'
            self.player.set_state(gst.STATE_NULL)
        self.player.set_property("uri", uri)
        self.player.set_state(gst.STATE_PLAYING)
        self.idle = False # now playing

