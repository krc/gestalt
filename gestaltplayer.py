#import pygst
#pygst.require("0.10")
import gst
import gobject
import gio

class GestaltPlayer:
    def __init__(self):
        Playbin2.__init__(self)
        # toss out video, just in case
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)
        # an empty deque structure to handle the playlist for now
        self.playQueue = deque([])

    def playFile(self, filepath):
        if self.idle:
            Playbin2.play(self, uri)
        else:
            self.playQueue.append(uri)

    def onMessage(self, bus, message):
        if Playbin2.onMessage(self, bus, message):
            try:
                self.play(self.playQueue.popleft())
            except IndexError:
                #empty queue
                pass



