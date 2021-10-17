import urwid
from cpr.mooks import mooks
from cpr.components.skill_button import SkillButton


class MookListBox(urwid.ListBox):

    def __init__(self, event_handler, debug):
        self.debug_handler = debug
        self.event_handler = event_handler
        self.mooks = mooks
        body = urwid.SimpleFocusListWalker(self.get_mook_list())
        super().__init__(body)

    def create_mook_list_button(self, text):
        w = SkillButton(text, on_press=self.press_button)
        w.set_label_center()
        w = urwid.AttrWrap(w, 'mook_list_text', 'button_focus')
        return w

    def press_button(self, button):
        self.event_handler('add_mook_to_roster', mooks[button.label])

    def get_mook_list(self):
        mook_buttons = []
        for mook in self.mooks.keys():
            mook_buttons.append(
                self.create_mook_list_button(mook)
            )
        return mook_buttons

