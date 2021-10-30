import urwid
from copy import deepcopy

from cpr.components.mook_card.util import create_skill_buttons
from cpr.components.buttons import SkillLabelButton, CardButton
from cpr.components.mook_card.change_weapon import ChangeWeapon

cell_width = 24
h_seperation = 1
v_seperation = 0
align = 'left'


class CombatZone(urwid.WidgetWrap):

    def __init__(self, card_widget, mook, roll_function, event_log, debug=None):
        self.card_widget = card_widget
        self.mook = mook
        self.roll = roll_function
        self.event_log = event_log
        self.debug = debug
        self.editable = False

        self.weapon_widget_placeholder = urwid.WidgetPlaceholder(self.create_weapon_widget())
        self.combat_skills_placeholder = urwid.WidgetPlaceholder(self.create_combat_widget())

        super().__init__(self.create_widget())

    def create_widget(self):
        return urwid.Pile([
            self.weapon_widget_placeholder,
            self.combat_skills_placeholder
        ])

    def create_weapon_widget(self, editable=False):
        weapon_names = [weapon.name for weapon in self.mook.weapons]
        weapon_buttons = create_skill_buttons(self.mook,
                                              weapon_names,
                                              on_press=self.roll,
                                              is_weapon=True,
                                              include_place_holder=editable,
                                              place_holder_width=10
                                              )
        if editable:
            swap_btns = self.create_edit_weapons_buttons()
            for btn_columns, swap_btn in zip(weapon_buttons, swap_btns):
                btn_columns.contents[-1][0].original_widget = swap_btn

            add_button = CardButton('Add', on_press=self.swap_add_weapon)
            add_button = urwid.Padding(add_button, 'left', ('relative', 20), min_width=15)
            weapon_buttons.append(add_button)

        _contents = urwid.GridFlow(weapon_buttons, 50, 1, 0, 'center')
        return urwid.LineBox(_contents, 'Weapons')

    def create_edit_weapons_buttons(self):
        # swap_buttons = [
        #     CardButton('Swap', on_press=lambda *args: self.swap_add_weapon(weapon))
        #     for weapon in self.mook.weapons
        # ]
        swap_buttons = []
        for weapon in self.mook.weapons:
            btn = CardButton('Swap')
            urwid.connect_signal(btn.button, 'click', self.swap_add_weapon, weapon)
            swap_buttons.append(btn)
        return swap_buttons

    def swap_add_weapon(self, button, weapon_obj=None):
        change_weapon_widget = ChangeWeapon(weapon_obj, self.debug)
        self.card_widget.card_placeholder.original_widget = change_weapon_widget
        urwid.connect_signal(change_weapon_widget, 'close', self.close_change_weapon_widget)

    def close_change_weapon_widget(self, change_weapon_widget, new_weapon):
        self.debug(new_weapon)
        if new_weapon is None:
            self.card_widget.build_card()
            return

        if change_weapon_widget.original_weapon is None:
            self.mook.weapons.append(new_weapon)

        else:
            for i, mook_weapon in enumerate(self.mook.weapons):
                if mook_weapon is change_weapon_widget.original_weapon:
                    self.debug(f'Changing weapon {i} ...')
                    self.mook.weapons.remove(change_weapon_widget.original_weapon)
                    self.mook.weapons.insert(i, new_weapon)

        self.weapon_widget_placeholder.original_widget = self.create_weapon_widget(editable=True)
        self.card_widget.build_card()
        self.debug(self.mook.weapons)

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

        return self.combat_elem

    def toggle_combat_skills(self, obj):
        if self.c_skills_visible:
            self.c_skill_placeholder.original_widget = self.empty_grid
            self.c_skills_visible = False
        else:
            self.c_skill_placeholder.original_widget = self.skills_elem
            self.c_skills_visible = True

    def enable_editing(self):
        self.editable = True
        self.weapon_widget_placeholder.original_widget = self.create_weapon_widget(editable=True)

    def disable_editing(self):
        self.editable = False
        self.weapon_widget_placeholder.original_widget = self.create_weapon_widget(editable=False)



