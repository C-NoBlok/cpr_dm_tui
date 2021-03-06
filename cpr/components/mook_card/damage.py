import urwid

from cpr.components.buttons import TakeDamageButton


class TakeDamageDialog(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self):

        self.damage_amount = urwid.IntEdit('Damage Taken: ', default=0)
        self.ablate_by = urwid.IntEdit('Ablate Armor By: ', default=1)

        armor_group = []
        self.head = urwid.RadioButton(armor_group, 'Head', False)
        self.body = urwid.RadioButton(armor_group, 'Body', True)

        self.half_sp_checkbox = urwid.CheckBox("Half SP", state=False)

        accept_button = TakeDamageButton('Accept', on_press=lambda btn: self._emit('close', True))
        close_button = TakeDamageButton("Close", on_press=lambda btn: self._emit('close', False))

        self.widget = urwid.GridFlow([
            urwid.Pile([self.damage_amount, self.ablate_by]),
            urwid.Pile([self.head, self.body])
        ], 25, 0, 1, 'center')
        self.pile = urwid.Pile([self.widget,
                                urwid.Padding(self.half_sp_checkbox, 'center', ('relative', 30), min_width=30),
                                urwid.GridFlow([accept_button, close_button], 15, 1, 2, 'center')
                                ])
        self.widget = urwid.LineBox(self.pile)
        self.widget = urwid.AttrMap(self.widget, 'take_damage')

        super().__init__(self.widget)

    def keypress(self, size, key):
        if key.lower() == 'y':
            self._emit('close', True)
        if key.lower() in ['n', 'q', 'c']:
            self._emit('close', False)

        return self.pile.keypress(size, key)
