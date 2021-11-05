import urwid
from cpr.components.mook_card import MookCard
from cpr.mooks.mook import Mook


class MookRoster(urwid.WidgetWrap, urwid.WidgetContainerMixin):

    def __init__(self, event_handler, debug):
        self.debug = debug
        self.event_handler = event_handler

        self.mook_roster = urwid.ListBox(
            urwid.SimpleFocusListWalker([])
        )
        super().__init__(self.mook_roster)

    def create_mook_card(self, mook_obj):
        if len(self.mook_roster.body) % 2 == 0:
            card = MookCard(mook_obj, self.event_handler, self.debug, alt_style=True)
            self.debug('mapping alt card')
            card = urwid.AttrMap(card, 'card_alt')
        else:
            card = MookCard(mook_obj, self.event_handler, self.debug)
        return card

    def add_mook(self, mook):
        if callable(mook):
            mook = mook()
        self.debug(f'Adding {mook.name} to roster.')
        self.mook_roster.body.append(self.create_mook_card(mook))

    def remove_mook_card(self, mook_card: MookCard):
        self.debug(f'Removing {mook_card.mook.name} from roster')
        # self.debug(self.mook_roster.body)
        for card in self.mook_roster.body:
            try:
                if card.original_widget.id == mook_card.id:
                    self.mook_roster.body.remove(card)
            except AttributeError:
                if card.id == mook_card.id:
                    self.mook_roster.body.remove(card)


