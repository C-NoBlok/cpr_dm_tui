import urwid


class ChangeName(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self, mook, debug):
        self.mook = mook
        self.debug = debug
        self.name_edit = None
        super().__init__(self.build_widget())

    def build_widget(self):
        self.name_edit = urwid.Edit(
            caption='Mook Name: ',
            edit_text=self.mook.name
        )
        urwid.connect_signal(self.name_edit, 'change', self.update_mook_name)
        ok_button = urwid.Button('OK', on_press=lambda *args: self._emit('close', self))
        ok_button = urwid.Padding(ok_button, 'center', ('relative', 10), min_width=10)

        pile = urwid.Pile([self.name_edit, ok_button])
        pile = urwid.LineBox(pile)
        widget = urwid.Padding(pile, 'center', ('relative', 40), min_width=30)
        return widget

    def update_mook_name(self, button, text):
        self.mook.name = text


