import sys
import logging
from logging import DEBUG

logger = logging.Logger('cpr')
logger.setLevel(DEBUG)

from cpr.components.mook_list import MookList
from cpr.components.mook_roster import MookRoster
from cpr.components.widget_pallete import pallete_256

import urwid
from urwid import raw_display
screen = raw_display.Screen()


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
            (20, self.mook_list),
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

        # if key[0] in ['q', 'Q']:
        #     sys.exit(1)
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
        while len(messages) > 4:
            messages.pop(0)
        footer_text = '\n'.join(messages)
        self.footer_text.set_text(footer_text)


def start_app():
    main = MainWidget()
    # tmux
    loop = urwid.MainLoop(main,
                          unhandled_input=main.unhandled_input,
                          palette=pallete_256)
    loop.screen.set_terminal_properties(colors=256)

    # from urwid.curses_display import Screen
    #
    # loop = urwid.MainLoop(main,
    #                       screen=Screen(),
    #                       unhandled_input=main.unhandled_input)

    loop.run()
