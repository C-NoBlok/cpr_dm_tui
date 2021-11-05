import os
from pathlib import Path
import json

import urwid
from cpr.mooks import mooks as built_in_mooks
from cpr.components.buttons import MookListButton
from cpr.mooks.mook import Mook


class MookListBox(urwid.ListBox):

    def __init__(self, event_handler, debug):
        self.debug_handler = debug
        self.event_handler = event_handler
        self.custom_mooks = {}
        body = urwid.SimpleFocusListWalker(self.get_mook_list())
        super().__init__(body)

    def create_mook_list_button(self, text):
        w = MookListButton(text, on_press=self.press_button)
        return w

    def press_button(self, button):
        if button.label in built_in_mooks:
            self.event_handler('add_mook_to_roster', built_in_mooks[button.label])
        elif button.label in self.custom_mooks:
            self.event_handler('add_mook_to_roster', self.custom_mooks[button.label])

    def get_mook_list(self):
        mook_list = self.get_built_in_mooks() + self.get_custom_mooks()
        return mook_list

    def get_built_in_mooks(self):
        mook_buttons = []
        for mook in built_in_mooks.keys():
            mook_buttons.append(
                self.create_mook_list_button(mook)
            )
        return mook_buttons

    def get_custom_mooks(self):
        usr_data_folder = Path.home() / '.cpr'
        if not usr_data_folder.exists():
            usr_data_folder.mkdir()
        custom_mook_files = usr_data_folder.glob('*.mook')

        mook_buttons = []
        for custom_mook_file in custom_mook_files:
            with open(custom_mook_file, 'r') as f:
                custom_mook_json = json.load(f)
            custom_mook = Mook.from_dict(custom_mook_json)

            self.custom_mooks[custom_mook.name] = custom_mook
            button = self.create_mook_list_button(custom_mook.name)
            mook_buttons.append(button)
        return mook_buttons





