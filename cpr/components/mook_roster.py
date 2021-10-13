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

    def remove_mook_card(self, mook_card):
        self.debug(f'Removing {mook_card.mook.name} from roster')
        self.mook_roster.body.remove(mook_card)

