import urwid

from cpr.components.buttons import SkillButton, CardButton


class SkillEdit(urwid.IntEdit):

    def valid_char(self, ch):
        return len(ch) == 1 and ch in '0123456789' and self.value() + 1 < 3


class ChangeSkillsWidget(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self, mook, debug):
        self.caption_len = 39
        self.debug = debug
        self.mook = mook
        self.grid = None
        self.pile = None

        super().__init__(self.build_widget())

    def build_widget(self):
        skill_edits = []
        for skill_name, skill_info in self.mook.skills.skills_by_name.items():
            caption = f'{skill_name} ({skill_info.base_stat}: {self.mook.stats.to_dict()[skill_info.base_stat]})'
            caption = caption + (self.caption_len - len(caption)) * ' '
            # edit = urwid.IntEdit(caption, default=skill_info.rank)
            edit = SkillEdit(caption, default=skill_info.rank)
            edit = self.wrap_edit(edit)
            skill_edits.append(edit)

        self.grid = urwid.GridFlow(skill_edits, 42, 1, 0, 'left')

        cancel_button = CardButton('Cancel', on_press=lambda *args: self._emit('close', None))
        accept_button = CardButton('Accept', on_press=lambda *args: self._emit('close', self))
        self.pile = urwid.Pile([
            self.grid,
            urwid.Divider('-'),
            urwid.GridFlow([accept_button, cancel_button], 20, 1, 1, 'center')
        ])
        return self.pile

    def wrap_edit(self, edit):
        urwid.connect_signal(edit, 'change', self.update_skill)
        edit = urwid.AttrMap(edit, '', 'edit_focus')
        return edit

    def update_skill(self, changed_skill, num):
        self.debug(f'updating skill {changed_skill}')
        skill = changed_skill.caption.split('(')[0].strip()
        skill_obj = self.mook.skills.skills_by_name[skill]
        if num == '':
            num = 0
        new_rank = int(num)
        if new_rank > 10:
            new_rank = 10
            changed_skill._edit_text = str(new_rank)

        skill_obj.rank = new_rank
        # self._w = self.build_widget()




