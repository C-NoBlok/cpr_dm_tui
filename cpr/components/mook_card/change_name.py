import urwid
from copy import copy
from cpr.components.buttons import CardButton


class ChangeName(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self, mook, debug):
        self.mook = mook
        self.debug = debug
        self.name_edit = None
        self.mook_type_edit = None
        self.pile = None
        self.original_name = copy(self.mook.name)
        super().__init__(self.build_widget())

    def build_widget(self):
        self.name_edit = urwid.Edit(
            caption='Mook Name: ',
            edit_text=self.mook.name
        )
        self.mook_type_edit = urwid.Edit(
            caption='Mook Type: ',
            edit_text=self.mook.mook_type
        )
        urwid.connect_signal(self.name_edit, 'change', self.update_mook_name)
        urwid.connect_signal(self.mook_type_edit, 'change', self.update_mook_type)
        ok_button = CardButton('OK', on_press=lambda *args: self._emit('close', True))
        cancel_button = CardButton('Cancel', on_press=self.cancel_name_change)
        button_grid = urwid.GridFlow([ok_button, cancel_button],
                                     20, 1, 1, 'center')
        # button_grid = urwid.Padding(button_grid, 'center', ('relative', 10), min_width=10)


        self.pile = urwid.Pile([self.name_edit, self.mook_type_edit, button_grid])
        widget = urwid.LineBox(self.pile)
        widget = urwid.Padding(widget, 'center', ('relative', 40), min_width=30)
        return widget

    def update_mook_name(self, button, text):
        self.mook.name = text

    def update_mook_type(self, button, text):
        self.mook.mook_type = text

    def cancel_name_change(self):
        self.mook.name = self.original_name
        self._emit('close', False)

    def keypress(self, size, key):
        widget_key_commands = {
            'enter': lambda *args: self._emit('close', self),
            'esc': self.cancel_name_change
        }
        if key in widget_key_commands:
            widget_key_commands[key]()
            return

        return self.pile.keypress(size, key)





