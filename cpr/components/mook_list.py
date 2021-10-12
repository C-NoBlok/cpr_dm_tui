from cpr.components.mook_list_box import MookListBox

import urwid

class MookList(urwid.LineBox):

    def __init__ (self, event_handler, debug):

        self.debug_handler = debug
        self.event_handler = event_handler
        frame = urwid.Frame(
            body=self.body(),
            #header=self.header(),
            footer=self.footer(),
            focus_part='body'

        )
        title = 'Mook List'
        title_align = 'left'
        super().__init__(frame,
                         title=title,
                         title_align=title_align)

    def body(self):
        # list_box = urwid.ListBox(self.list_walker())
        list_box = MookListBox(self.event_handler, self.debug_handler)
        return list_box

    def header(self):
        return urwid.Pile([
            urwid.Text('Mook List'),
            urwid.Divider()
        ])

    def footer(self):
        return urwid.Text('save | remove ')

    def list_walker(self):
        contents = [
            urwid.Text('booster'),
            urwid.Text('security'),
            urwid.Text('netrunner')
        ]
        return urwid.SimpleFocusListWalker(contents)


