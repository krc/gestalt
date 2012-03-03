import gobject
import gst
from playbininterface import PlaybinInterface
from collections import deque

class GestaltPlayer:
    def __init__(self):
        self.playbin = PlaybinInterface()
        # an empty deque structure to handle the playlist for now
        self.playQueue = deque([])

    def playFile(self, filepath):
        if self.playbin.idle:
            self.playbin.play(filepath)
        else:
            self.playQueue.append(filepath)

    def on_message(self, bus, message):
        if self.playbin.on_message(self, bus, message):
            try:
                self.playFile(self.playQueue.popleft())
            except IndexError:
                #empty queue
                pass



