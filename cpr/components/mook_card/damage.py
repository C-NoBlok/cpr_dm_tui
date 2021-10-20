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

        accept_button = TakeDamageButton('Accept', on_press=lambda btn: self._emit('close', True))
        close_button = TakeDamageButton("Close", on_press=lambda btn: self._emit('close', False))

        self.grid = urwid.GridFlow([
            self.damage_amount, self.head,
            self.ablate_by, self.body,
            accept_button, close_button
        ],
            40, 1, 0, 'center')


        self.widget = urwid.Columns([
            urwid.Pile([self.damage_amount, self.ablate_by]),
            urwid.Pile([self.head, self.body])
        ])
        self.pile = urwid.Pile([self.widget,
                                  urwid.Padding(urwid.Columns([
                                      (15, accept_button),
                                      (15, close_button),
                                      ]), align='center', width=('relative', 75))
                                  ])

        self.widget = urwid.Padding(self.pile, align='center', width=('relative', 50))

        self.widget = urwid.LineBox(self.widget)
        self.widget = urwid.AttrMap(self.widget, 'take_damage')

        super().__init__(self.widget)

    def keypress(self, size, key):
        if key.lower() == 'y':
            self._emit('close', True)
        if key.lower() == 'n':
            self._emit('close', False)

        return self.pile.keypress(size, key)
