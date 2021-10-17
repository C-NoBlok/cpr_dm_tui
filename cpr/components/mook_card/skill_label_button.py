import urwid


class SkillLabelButton(urwid.Button):

    def __init__(self, label, on_press=None):
        self.button_left = urwid.Text('|')
        self.button_right = urwid.Text('|')
        super().__init__(label=label, on_press=on_press)