import urwid


class BoxButton(urwid.WidgetWrap):
    """ Taken from https://stackoverflow.com/a/65871001/778272
    """
    def __init__(self, label, on_press):
        label_widget = urwid.Text(label, align='center')
        self.widget = urwid.LineBox(label_widget)
        self.hidden_button = urwid.Button('hidden button', on_press)
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
#         self.padding_size = 2
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
#         border = self._border_char * (len(label) + self.padding_size * 2)
#         cursor_position = len(border) + self.padding_size
#
#         top = u'┌' + border + u'┐\n'
#         middle = u'│  ' + label + u'  │\n'
#         bottom = u'└' + border + u'┘'
#
#         box_widget = urwid.Pile([
#             urwid.Text(top[:-1]),
#             urwid.Text(middle[:-1]),
#             urwid.Text(bottom),
#         ])
#         return box_widget

