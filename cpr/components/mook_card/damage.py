import urwid


class TakeDamageDialog(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self):

        self.damage_amount = urwid.IntEdit('Damage Taken: ', default=0)
        self.ablate_by = urwid.IntEdit('Ablate Armor By: ', default=1)

        armor_group = []
        self.head = urwid.RadioButton(armor_group, 'Head', False)
        self.body = urwid.RadioButton(armor_group, 'Body', True)

        accept_button = urwid.Button('Accept', on_press=lambda btn: self._emit('close'))
        close_button = urwid.Button("Close", on_press=lambda btn: self._emit('close'))
        button_col = urwid.Columns([accept_button, close_button])

        self.grid = urwid.GridFlow([
            self.damage_amount, self.head,
            self.ablate_by, self.body,
            accept_button, close_button
        ],
            40, 1, 0, 'center')
        super().__init__(self.grid)

    def keypress(self, size, key):
        if key == 'enter':
            self._emit('close')

        return self.grid.keypress(size, key)
