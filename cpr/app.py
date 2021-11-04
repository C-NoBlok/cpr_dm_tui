import sys
import logging
from logging import DEBUG

logger = logging.Logger('cpr')
logger.setLevel(DEBUG)

from cpr.components.mook_list import MookList
from cpr.components.mook_roster import MookRoster
from cpr.components.widget_pallete import pallete_256
from cpr.components.event_log import EventLog

import urwid
from urwid import raw_display
screen = raw_display.Screen()

DEBUG_MODE = True


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

        self.event_log = EventLog(debug=lambda *args: None, visible=DEBUG_MODE)

        self.body = urwid.Columns([
            (20, self.mook_list),
            self.roster
        ])
        self.body = urwid.AttrMap(self.body, 'body')

        self.main_frame = urwid.Frame(
            body=self.body,
            header=self.header,
            footer=self.event_log
        )
        super().__init__(self.main_frame)

    def unhandled_input(self, key):
        if key[0] in ['mouse release', 'mouse drag']:
            return

        if key == 'tab':
            self.debug('cycling mook.')
            current_position = self.roster.mook_roster.body.focus
            try:
                next_roster_position = self.roster.mook_roster.body.next_position(current_position)
            except IndexError:
                next_roster_position = 0
            self.debug(next_roster_position)
            self.roster.mook_roster.body.set_focus(next_roster_position)

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
        if not show_signals:
            self.event_log.event(msg)
            return
        else:
            self.event_log.event(get_signals())


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
