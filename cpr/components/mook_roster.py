import urwid
from cpr.components.mook_card import MookCard


class MookRoster(urwid.LineBox):

    def __init__(self, event_handler, debug):
        self.debug = debug
        self.event_handler = event_handler

        self.mook_roster = urwid.ListBox(
            urwid.SimpleFocusListWalker([])
        )
        super().__init__(self.mook_roster)

    def create_mook_card(self, mook_obj):
        card = MookCard(mook_obj, self.event_handler, self.debug)
        return card

    def add_mook(self, mook_data):
        self.debug(f'Adding {mook_data.name} to roster.')
        self.mook_roster.body.append(self.create_mook_card(mook_data))

    def remove_mook_card(self, mook_obj):
        self.debug(f'Removing card from mook_list.body. {mook_obj in self.mook_roster.body}')
        self.debug(f'{mook_obj, self.mook_roster.body}')
        self.mook_roster.body.remove(mook_obj)

