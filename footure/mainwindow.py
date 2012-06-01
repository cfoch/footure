import gtk
from teams import TeamWidget

APPNAME = "Footure"
VERSION = "0.01"
DEVELOPER = "cfoch"

class FootureMainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self._createUI()

    def _createUI(self):
        teams = TeamWidget()
        self.add(teams)
        self.set_title(APPNAME)
        self.connect("delete-event", self._deleteCb)
        self.show_all()

    def _deleteCb(self, widget, data=None):
        gtk.main_quit()
        return False

