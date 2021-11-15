import urwid


class MookTree(urwid.WidgetWrap):

    def __init__(self):
        self.tree = urwid.TreeWidget