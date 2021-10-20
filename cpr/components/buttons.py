import urwid


class SqrBrkButton(urwid.Button):

    def __init__(self, *args, **kwargs):
        self.button_left = urwid.Text('[')
        self.button_right = urwid.Text(']')
        super().__init__(*args, **kwargs)


class PipeButton(urwid.Button):

    def __init__(self, *args, **kwargs):
        self.button_left = urwid.Text('|')
        self.button_right = urwid.Text('|')
        super().__init__(*args, **kwargs)

class SkillLabelButton(urwid.WidgetWrap):

    def __init__(self, label, on_press=None):
        button = PipeButton(label, on_press=on_press)
        button = urwid.AttrMap(button, 'expander_button')
        super().__init__(button)


class TakeDamageButton(urwid.WidgetWrap):

    def __init__(self, label, on_press=None):
        button = SqrBrkButton(label, on_press=on_press)
        button._label.set_align_mode('center')
        button = urwid.AttrMap(button, 'take_damage_button', 'take_damage_button_focus')
        super().__init__(button)


class SkillButton(urwid.WidgetWrap):

    def __init__(self, label, on_press=None):
        button = SqrBrkButton(label, on_press=on_press)
        button._label.set_align_mode('center')
        button = urwid.AttrMap(button, 'skill_button', 'button_focus')
        super().__init__(button)


class MookListButton(urwid.WidgetWrap):

    def __init__(self, label, on_press=None):
        button = SqrBrkButton(label, on_press=on_press)
        button = urwid.AttrMap(button, 'mook_list_text', 'button_focus')
        super().__init__(button)


class CardButton(urwid.WidgetWrap):

    def __init__(self, label, on_press=None):
        self.button = urwid.Button(label, on_press=on_press)
        self.button._label.set_align_mode('center')
        self.widget_wrap = urwid.AttrWrap(self.button, 'card_options', 'button_focus')
        super().__init__(self.widget_wrap)


class BoxButton(urwid.WidgetWrap):
    """ Taken from https://stackoverflow.com/a/65871001/778272
    """
    def __init__(self, label, on_press):
        self.label = urwid.Text(label, align='center')
        self.widget = urwid.LineBox(self.label)
        self.hidden_button = urwid.Button('hidden button', on_press)
        self.widget._selectable = True
        super(BoxButton, self).__init__(self.widget)

    def selectable(self):
        return True

    def keypress(self, *args, **kwargs):
        return self.hidden_button.keypress(*args, **kwargs)

    def mouse_event(self, *args, **kwargs):
        return self.hidden_button.mouse_event(*args, **kwargs)

#
# class BoxButton(urwid.Button):
#     _border_char = u'─'
#
#     def __init__(self, label, on_press=None, user_data=None):
#         self.padding_size = 1
#         label = self.draw_box(label)
#
#         if on_press:
#             urwid.connect_signal(self, 'click', on_press, user_data)
#
#         self._w = label
#
#         super(urwid.WidgetWrap, self).__init__()
#
#     def draw_box(self, label):
#         border = self._border_char * (len(label) + self.padding_size * 1)
#         cursor_position = len(border) + self.padding_size
#
#         top = u'┌' + border + u'┐\n'
#         middle = u'│  ' + label + u'  │\n'
#         bottom = u'└' + border + u'┘'
#
#         box_widget = urwid.Pile([
#             urwid.Text(top[:-2]),
#             urwid.Text(middle[:-2]),
#             urwid.Text(bottom),
#         ])
#         return box_widget

