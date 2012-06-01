import gtk

class TeamWidget(gtk.VBox):
    def __init__(self):
        gtk.VBox.__init__(self)
        groups = gtk.HBox()
        adj_teams = gtk.Adjustment(value=3, lower=3, upper=32,
            step_incr=1, page_incr= 1)
        adj_groups = gtk.Adjustment(value=1, lower=1, upper=16,
            step_incr=1, page_incr= 1)
        self.spinner_teams = gtk.SpinButton(adj_teams, climb_rate=1, digits=0)
        self.spinner_groups = gtk.SpinButton(adj_groups, 1, 0)
        groups.add(gtk.Label("Groups: "))
        groups.add(self.spinner_teams)
        groups.add(gtk.Label("Teams: "))
        groups.add(self.spinner_groups)
        self.add(groups)

        
