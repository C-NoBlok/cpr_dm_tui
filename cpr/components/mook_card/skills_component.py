import urwid

from cpr.components.mook_card.util import create_skill_buttons


class SkillList(urwid.Columns):

    def __init__(self, mook, callback):
        self.skills_visible = False
        skill_keys = sorted(mook.non_combat_skills.keys())
        skills_button_list = create_skill_buttons(mook, skill_keys, on_press=callback, col1_width=20)
        self.skill_grid = urwid.GridFlow(skills_button_list, 28, 1, 0, 'left')

        self.placeholder = urwid.WidgetPlaceholder(urwid.GridFlow([], 1,1,1,'left'))

        self.skills_button = urwid.Button('|-Skills-|', on_press=self.toggle_skills)
        super().__init__([
            (14, self.skills_button),
            self.placeholder
        ])

    def toggle_skills(self, obj):
        if self.skills_visible:
            self.widget_list = [
                self.skills_button,
                self.placeholder
            ]
            self.skills_visible = False
        else:
            self.widget_list = [
                self.skills_button,
                self.skill_grid
            ]
            self.skills_visible = True




