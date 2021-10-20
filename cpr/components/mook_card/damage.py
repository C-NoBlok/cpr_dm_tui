import urwid


class TakeDamageDialog(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self):

        self.damage_amount = urwid.IntEdit('Damage Taken: ', default=0)
        self.ablate_by = urwid.IntEdit('Ablate Armor By: ', default=1)

        armor_group = []
        self.head = urwid.RadioButton(armor_group, 'Head', False)
        self.body = urwid.RadioButton(armor_group, 'Body', True)

        accept_button = urwid.Button('Accept', on_press=lambda btn: self._emit('close', True))
        close_button = urwid.Button("Close", on_press=lambda btn: self._emit('close', False))
        button_col = urwid.Columns([accept_button, close_button])

        self.grid = urwid.GridFlow([
            self.damage_amount, self.head,
            self.ablate_by, self.body,
            accept_button, close_button
        ],
            40, 1, 0, 'center')
        self.line_box = urwid.LineBox(self.grid)
        self.widget = urwid.AttrMap(self.line_box, 'take_damage')

        super().__init__(self.widget)

    def keypress(self, size, key):
        if key == 'enter':
            self._emit('close', True)

        return self.grid.keypress(size, key)
