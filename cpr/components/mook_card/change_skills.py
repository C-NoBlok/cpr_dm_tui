import urwid
from copy import deepcopy

from cpr.components.buttons import SkillButton, CardButton


class SkillEdit(urwid.IntEdit):

    def valid_char(self, ch):
        """
        Overwrites IntEdit valid_char method to check to make sure the string,
        self.value(), cannot be 3 characters long.
        """
        return len(ch) == 1 and ch in '0123456789' and int(self.edit_text + ch) <= 10


class ChangeSkillsWidget(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self, mook, debug):
        self.caption_len = 39
        self.debug = debug
        self.mook = mook
        self.original_skills = deepcopy(self.mook.skills)
        self.grid = None
        self.pile = None
        self.total_ranks_text = urwid.Text('')

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

        self.update_total_rank_text()

        self.grid = urwid.GridFlow(skill_edits, 42, 1, 0, 'left')

        cancel_button = CardButton('Cancel', on_press=self.cancel)
        accept_button = CardButton('Accept', on_press=lambda *args: self._emit('close', self))
        self.pile = urwid.Pile([
            self.grid,
            urwid.Divider('-'),
            self.total_ranks_text,
            urwid.GridFlow([accept_button, cancel_button], 20, 1, 1, 'center')
        ])
        return self.pile

    def update_total_rank_text(self):
        total_ranks = self.mook.skills.total_ranks
        self.debug(f'Updating Mook Total Ranks to {total_ranks}')
        self.total_ranks_text.set_text(f'Total Ranks: {total_ranks}'),

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
        self.debug(f'New Rank: {new_rank}')
        if new_rank > 10:
            new_rank = 10

        skill_obj.rank = new_rank
        self.update_total_rank_text()

    def cancel(self, button):
        self.debug('Canceling Skill Change...')
        self.mook.skills = self.original_skills
        self._emit('close', None)



