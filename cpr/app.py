from cpr.components.mook_list import MookList
from cpr.components.mook_roster import MookRoster

import urwid
from urwid import raw_display
screen = raw_display.Screen()

# Pallet tuple -> (name, foreground, background, mono, foreground_high, background_high)

pallete = [
    ('header', 'dark red', 'light gray',),
    ('footer', 'dark red', 'light gray',),
    ('body', 'dark red', 'light gray',),
    ('title', 'dark red', 'light gray'),
    ('mook_list', 'dark red', 'light gray'),
    ('button', 'dark red', 'light gray', 'standout'),
    ('card', 'dark red', 'black'),
    ('skill_button', 'white', 'black', 'standout'),
    ('box_button', 'dark red', 'white'),
    # ('hit_points',)
    # ('hit_points_serious',)
]
pallete_256 = [
    ('header', '', '', '', 'h196', 'g15'),
    ('footer', '', '', '', 'h196', 'g15'),
    ('body', 'dark red', 'light gray',),
    ('title', 'dark red', 'light gray'),
    ('mook_list', '', '', '', 'h196', 'g15'),
    ('button', 'dark red', 'light gray'),
    ('card', '', '', '', 'h196', 'g70'),
    ('card_alt', '', '', '', 'h196', 'g80'),
    ('skill_button', '', '', '', 'g100', 'g35'),
    ('box_button', '', '', '', 'g95', 'g15'),
    ('mook_list_text', '', '', '', 'g95', 'g15'),
    ('button_focus', '', '', 'bold', 'g0', 'h196'),
    ('card_focus', '', '', '', 'h15', 'h1'),
    ('edit_focus', '', '', 'bold', 'g100', 'g35')
    # ('hit_points',)
    # ('hit_points_serious',)
]

"""
'bold'
'underline'
'standout'
'blink'
'italics'
'strikethrough'
"""


class MainWidget(urwid.WidgetWrap, urwid.WidgetContainerMixin):

    def __init__(self):

        self.roster = MookRoster(self.handle_event, self.debug)
        self.mook_list = MookList(self.handle_event, self.debug)
        self.mook_list = urwid.AttrMap(self.mook_list, 'mook_list')

        self.header = urwid.LineBox(
            urwid.Pile([
                urwid.Padding(urwid.BigText('Mook Manager',
                                                  urwid.HalfBlock5x4Font()),
                                    "center", None),
                urwid.Divider('=')
            ]
            ))
        self.header = urwid.AttrMap(self.header, 'header')

        self.footer_text = urwid.Text('')
        self.footer = urwid.Pile([self.footer_text])
        self.footer = urwid.AttrMap(self.footer, 'footer')

        self.body = urwid.Columns([
            (19, self.mook_list),
            self.roster
        ])
        self.body = urwid.AttrMap(self.body, 'body')

        self.main_frame = urwid.Frame(
            body=self.body,
            header=self.header,
            footer=self.footer
        )
        super().__init__(self.main_frame)

    def unhandled_input(self, key):
        if key[0] in ['mouse release', 'mouse drag']:
            return
        self.debug(str(key))

    def handle_event(self, action, data):
        if action == 'add_mook_to_roster':
            self.roster.add_mook(data)

        if action == 'remove card':
            self.roster.remove_mook_card(data)

    def debug(self, msg, show_signals=False):
        def get_signals():
            text = ''
            for key, value in urwid.signals._signals.__dict__.items():
                text += f'{key}: {value}\n'
            return text

        if show_signals:
            self.footer_text.set_text(get_signals())

        orig_text = self.footer_text.get_text()[0]

        new_msg = f'>>> {msg}\n'

        footer_text = orig_text + new_msg
        messages = footer_text.split('\n')
        if len(messages) > 4:
            messages.pop(0)
        footer_text = '\n'.join(messages)
        self.footer_text.set_text(footer_text)


def start_app():
    main = MainWidget()
    loop = urwid.MainLoop(main, unhandled_input=main.unhandled_input, pop_ups=True, palette=pallete_256)
    loop.screen.set_terminal_properties(colors=256)
    loop.run()
