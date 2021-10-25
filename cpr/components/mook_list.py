from cpr.components.mook_list_box import MookListBox
from cpr.components.emoji_map import ogre, plus, floppy_disk
from cpr.components.buttons import BoxButton
from cpr.components.util import find_signal_object

import urwid

class MookList(urwid.LineBox, urwid.WidgetContainerMixin):

    signals = ['clicked']

    def __init__(self, event_handler, debug):

        self.debug_handler = debug
        self.event_handler = event_handler
        frame = urwid.Frame(
            body=self.body(),
            #header=self.header(),
            footer=self.footer(),
            focus_part='body'

        )

        title = ogre + ' Mook List ' + ogre
        title_align = 'left'
        super().__init__(frame,
                         title=title,
                         title_align=title_align)

    def body(self):
        list_box = MookListBox(self.event_handler, self.debug_handler)
        return list_box

    def header(self):
        text = urwid.Text('Mook List')
        text = urwid.AttrMap(text, 'mook_list_text'),
        return urwid.Pile([
            text,
            urwid.Divider()
        ])

    def footer(self):
        add_button = BoxButton('New', on_press=self.new_mook)
        add_button = urwid.AttrMap(add_button, 'box_button')
        save_mook = BoxButton('Save', on_press=self.save_mook)
        save_mook = urwid.AttrMap(save_mook, 'box_button')
        button_layout = urwid.Pile([add_button, save_mook])
        return button_layout

    def new_mook(self, *args):
        self.debug_handler('Editing Mook...')
        self.debug_handler('', show_signals=True)


    def save_mook(self, *args):
        self.debug_handler('Saving Mook... (Not Implemented. What am I saving?)')

    def list_walker(self):
        contents = [
            urwid.Text('booster'),
            urwid.Text('security'),
            urwid.Text('netrunner')
        ]
        return urwid.SimpleFocusListWalker(contents)


