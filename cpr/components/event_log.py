from cpr.components.unicode_map import up_triangle, down_triangle
from cpr.components.buttons import UpDownButton
import urwid


class EventLog(urwid.WidgetWrap):

    def __init__(self, max_lines=5, debug=None, visible=True):

        self.max_lines = max_lines
        self.debug = debug

        self.bottom_msg_position = self.max_lines

        self.msgs = ['>>>' for lines in range(self.max_lines)]
        self.event_log = urwid.Text('')
        if visible:
            self.build_widget()
        else:
            version = urwid.Text('v0.0.1', align='right')
            version = urwid.AttrMap(version, 'footer')
            super().__init__(version)


    def event(self, msg):
        self.msgs.append(f'>>> {msg}')
        self.bottom_msg_position = len(self.msgs)
        self.build_view()

    def build_view(self):
        view_list = self.msgs[self.bottom_msg_position - self.max_lines:self.bottom_msg_position]
        view = '\n'.join(view_list)
        self.event_log.set_text(view)

    def build_scroll_pile(self):
        scroll_pile = [urwid.Text('| - |') for lines in range(self.max_lines - 2)]
        scroll_pile.insert(0, UpDownButton(up_triangle, on_press=self.up))
        scroll_pile.append(UpDownButton(down_triangle, on_press=self.down))
        button_pile = urwid.Pile(scroll_pile)
        return button_pile

    def build_widget(self):
        columns = urwid.Columns([
            self.event_log,
            (5, self.build_scroll_pile())
        ])
        columns = urwid.AttrMap(columns, 'footer')
        self.build_view()
        self._w = columns


    def up(self, btn):
        if self.bottom_msg_position < self.max_lines:
            self.debug(self.bottom_msg_position)
            return
        else:
            self.bottom_msg_position += -1
            self.debug(self.bottom_msg_position)
            self.build_view()
            return

    def down(self, btn):
        if self.bottom_msg_position > len(self.msgs) - 1:
            self.debug(self.bottom_msg_position)
            return
        else:
            self.bottom_msg_position += 1
            self.debug(self.bottom_msg_position)
            self.build_view()
            return
