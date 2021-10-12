import urwid

from urwid import raw_display

from cpr.components.mook_card.util import create_skill_buttons, unpack_into_cols

screen = raw_display.Screen()

cell_width = 24
h_seperation = 1
v_seperation = 0
align = 'left'


class CombatZone(urwid.WidgetWrap):

    def __init__(self, mook, roll_function, debug=None):
        self.mook = mook
        self.roll = roll_function
        self.debug = debug

        # TODO Is it better to instantiate once or re-create?
        # self.weapon_widget = self.create_weapon_widget()
        # self.armor_widget = self.create_armor_widget()
        # self.combat_widget = self.create_combat_widget()

        cols = screen.get_cols_rows()[0]
        # super().__init__(self.create_dynamic_component(cols))
        super().__init__(self.create_grid_component())

    # def render(self, size, *args, **kwargs):
    #     self._set_w(self.create_dynamic_component(size[0]))
    #     return super().render(self.pack(size)[:1], *args, **kwargs)

    def on_resize(self):
        # self.debug(f'screen resizing {screen.get_cols_rows()}')
        self._set_w(self.create_dynamic_component(screen.get_cols_rows()[0]))

    def create_dynamic_component(self, cols):
        if cols >= 134:
            contents = [
                (50, self.create_weapon_widget()),
                (21, self.create_armor_widget()),
                self.create_combat_widget()
            ]
            component = urwid.Columns(contents)

        elif 91 < cols < 134:
            contents = [
                (50, self.create_weapon_widget()),
                (21, self.create_armor_widget()),
            ]
            contents = urwid.Columns(contents)
            component = urwid.Pile([contents, self.create_combat_widget()])

        else:
            contents = [self.create_weapon_widget(), self.create_armor_widget(), self.create_combat_widget()]
            component = urwid.Pile(contents)
        return component

    def create_grid_component(self):
        return urwid.GridFlow([
            self.create_weapon_widget(),
            # self.create_armor_widget(),
            self.create_combat_widget()
        ], 50, 1, 1, 'left'
        )

    def create_weapon_widget(self):
        weapon_names = [weapon.name for weapon in self.mook.weapons]
        weapon_buttons = create_skill_buttons(self.mook,
                                              weapon_names,
                                              on_press=self.roll,
                                              is_weapon=True)
        # weapon_buttons.insert(0, urwid.Text('Weapons: '))
        # _contents = urwid.Pile(weapon_buttons)
        _contents = urwid.Columns([
            (10, urwid.Text('Weapons: ')),
            urwid.Pile(weapon_buttons)
        ])
        return urwid.LineBox(_contents)

    def create_armor_widget(self):
        armor_elem = urwid.Columns([
            (9, urwid.Text("Armor: ")),
            (9, urwid.Pile(
                [
                    urwid.IntEdit('Head: ', self.mook.armor[-1]),
                    urwid.IntEdit('Body: ', self.mook.armor[0])
                ]
            ))
        ])
        return urwid.LineBox(armor_elem)

    def create_combat_widget(self):
        self.c_skills_visible = False
        keys = sorted(self.mook.combat_skills.keys())
        self.skill_buttons = create_skill_buttons(self.mook,
                                             keys,
                                             on_press=self.roll,
                                             col1_width=18, )
        # skill_cols = unpack_into_cols(skill_buttons,
        #                               items_per_col=3)
        self.c_skill_placeholder = urwid.WidgetPlaceholder(urwid.GridFlow([], 1, 1, 1, 'left'))

        self.skills_elem = urwid.GridFlow(self.skill_buttons,
                                     cell_width,
                                     h_seperation,
                                     v_seperation,
                                     align)

        self.c_skills_button = urwid.Button('Combat Skills', on_press=self.toggle_combat_skills)
        self.combat_elem = urwid.Columns([
            (17, self.c_skills_button),
            self.c_skill_placeholder
        ])

        return urwid.LineBox(self.combat_elem)

    def toggle_combat_skills(self, obj):
        if self.c_skills_visible:
            self.combat_elem.widget_list = [
                self.c_skills_button,
                self.c_skill_placeholder
            ]
            self.c_skills_visible = False
        else:
            self.combat_elem.widget_list = [
                self.c_skills_button,
                self.skills_elem
            ]
            self.c_skills_visible = True



