from cpr.components.mook_list import MookList
from cpr.components.mook_roster import MookRoster

import urwid
from urwid import raw_display
from urwid.listbox import ListBoxError
screen = raw_display.Screen()
from urwid import LineBox, Columns, Text, Frame, BigText, Padding


def unhandled_input(key):
    if key[0] in ['mouse release', 'mouse drag']:
        return
    footer_text.set_text(str(key))


def handle_event(action, data):
    if action == 'add_mook_to_roster':
        debug(f'add_mook_to_roster called {data.name}')
        roster.add_mook(data)

    if action == 'remove card':
        debug(f'Removing {data.mook.name} from list')
        roster.remove_mook_card(data)


def debug(msg):
    footer_text.set_text(msg)
    # footer_text.set_text(str(screen.get_cols_rows()))

    # text = ''
    # for key, value in urwid.signals._signals.__dict__.items():
    #     text += f'{key}: {value}\n'
    # footer_text.set_text(text)


roster = MookRoster(handle_event, debug)
mook_list = MookList(handle_event, debug)

header_text = Padding(
    BigText('Mook Manager', urwid.HalfBlock5x4Font()),
    "center",
    None
)
footer_text = Text('footer')

main_frame = Frame(
    body=Columns([
        (20, mook_list),
         roster
    ]),
    header=header_text,
    footer=footer_text
)

main_frame = LineBox(main_frame)
# urwid.register_signal(urwid.display_common.BaseScreen, 'input descriptors change')

def start_app():
    loop = urwid.MainLoop(main_frame, unhandled_input=unhandled_input, pop_ups=True)
    loop.run()


if __name__ == '__main__':
    loop = start_app()

