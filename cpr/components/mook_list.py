from cpr.components.mook_list_box import MookListBox
from cpr.components.unicode_map import ogre, plus, floppy_disk
from cpr.components.buttons import BoxButton
from cpr.components.util import find_signal_object
from cpr.mooks.mook import Mook
from cpr.mooks.skills import Skills
from cpr.mooks.stats import Stats
from cpr.weapons import heavy_pistol

import urwid


class MookList(urwid.WidgetWrap):

    signals = ['clicked']

    def __init__(self, event_handler, debug):

        self.debug = debug
        self.event_handler = event_handler
        self.frame = None
        self.title = ogre + ' Mook List ' + ogre
        self.main_placeholder = urwid.WidgetPlaceholder(urwid.Text(''))
        self.build_widget()
        super().__init__(self.main_placeholder)

    def build_widget(self):
        self.frame = urwid.Frame(
            body=self.body(),
            # header=self.header(),
            footer=self.footer(),
            focus_part='body'

        )
        linebox = urwid.LineBox(self.frame,
                                title=self.title,
                                title_align='left')

        self.main_placeholder.original_widget = linebox
        self.debug('Updated Mook List.')

    def body(self):
        list_box = MookListBox(self.event_handler, self.debug)
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
        self.debug('Creating New Mook...')
        new_stats = Stats(6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
        new_mook = Mook('unnamed', 'custom', new_stats, [heavy_pistol()], {'head': 4, 'body': 4}, Skills(), [])
        self.event_handler('add_mook_to_roster', new_mook)



    def save_mook(self, *args):
        self.debug('Saving Mook... (Not Implemented. What am I saving?)')

    def list_walker(self):
        contents = [
            urwid.Text('booster'),
            urwid.Text('security'),
            urwid.Text('netrunner')
        ]
        return urwid.SimpleFocusListWalker(contents)


