import urwid

class SkillButton(urwid.Button):
    def __init__(self, *args, **kwargs):
        self.button_left = urwid.Text('[')
        self.button_right = urwid.Text(']')
        super().__init__(*args, **kwargs)

