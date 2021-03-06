import urwid

from cpr.components.buttons import SkillLabelButton
from cpr.components.mook_card.util import create_skill_buttons


class SkillList(urwid.WidgetWrap):

    def __init__(self, card_widget, mook, callback):
        self.card_widget = card_widget
        self.skills_visible = False
        skill_obj = list(mook.non_combat_skills.values())
        skills_button_list = create_skill_buttons(mook, skill_obj, on_press=callback, col1_width=20)
        self.skill_grid = urwid.GridFlow(skills_button_list, 28, 1, 0, 'left')
        self.fill = urwid.Divider('/')
        self.placeholder = urwid.WidgetPlaceholder(self.fill)

        self.skills_button = SkillLabelButton('--Skills--', on_press=self.toggle_skills)
        self.skills_button = urwid.AttrMap(self.skills_button, 'expander_button', 'button_focus')

        self.widget = urwid.Columns([
            (14, self.skills_button),
            (1, urwid.Text(' ')),
            self.placeholder
        ])

        super().__init__(self.widget)

    def toggle_skills(self, obj):
        if self.skills_visible:
            self.placeholder.original_widget = self.fill
            self.skills_visible = False
        else:
            self.placeholder.original_widget = self.skill_grid
            self.skills_visible = True





