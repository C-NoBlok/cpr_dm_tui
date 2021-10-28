import urwid

from cpr.components.mook_card.util import create_skill_buttons
from cpr.components.buttons import SkillLabelButton

cell_width = 24
h_seperation = 1
v_seperation = 0
align = 'left'


class CombatZone(urwid.WidgetWrap):

    def __init__(self, mook, roll_function, event_log, debug=None):
        self.mook = mook
        self.roll = roll_function
        self.event_log = event_log
        self.debug = debug

        super().__init__(self.create_grid_component())

    def create_grid_component(self):
        return urwid.GridFlow([
            self.create_weapon_widget(),
            self.create_combat_widget()
        ], 50, 1, 1, 'center')

    def create_weapon_widget(self):
        weapon_names = [weapon.name for weapon in self.mook.weapons]
        weapon_buttons = create_skill_buttons(self.mook,
                                              weapon_names,
                                              on_press=self.roll,
                                              is_weapon=True)
        _contents = urwid.Columns([
            (10, urwid.Text('Weapons: ')),
            urwid.GridFlow(weapon_buttons, 60, 1, 0, 'left')
        ])
        return urwid.LineBox(_contents)

    def create_combat_widget(self):
        self.c_skills_visible = False
        keys = list(self.mook.combat_skills.values())
        self.skill_buttons = create_skill_buttons(self.mook,
                                                  keys,
                                                  on_press=self.roll,
                                                  col1_width=18, )
        self.empty_grid = urwid.Divider('/')
        self.c_skill_placeholder = urwid.WidgetPlaceholder(self.empty_grid)

        self.skills_elem = urwid.GridFlow(self.skill_buttons,
                                          cell_width,
                                          h_seperation,
                                          v_seperation,
                                          align)

        self.c_skills_button = SkillLabelButton('Combat Skills', on_press=self.toggle_combat_skills)
        self.c_skills_button = urwid.AttrMap(self.c_skills_button, 'expander_button', 'button_focus')

        self.combat_elem = urwid.Columns([
            (17, self.c_skills_button),
            (1, urwid.Text(' ')),
            self.c_skill_placeholder
        ])

        return urwid.LineBox(self.combat_elem)

    def toggle_combat_skills(self, obj):
        if self.c_skills_visible:
            self.c_skill_placeholder.original_widget = self.empty_grid
            self.c_skills_visible = False
        else:
            self.c_skill_placeholder.original_widget = self.skills_elem
            self.c_skills_visible = True



