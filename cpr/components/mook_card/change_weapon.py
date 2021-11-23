import urwid

from cpr.weapons import light_melee_weapon, medium_melee_weapon, heavy_melee_weapon, very_heavy_melee_weapon,\
    medium_pistol, heavy_pistol, very_heavy_pistol, smg, heavy_smg, shotgun, assault_rifle, sniper_rifle, \
    grenade_launcher, rocket_launcher, flame_thrower, bows_and_crossbows
from cpr.components.buttons import SkillButton, CardButton


class ChangeWeapon(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self, original_weapon, debug):
        self.debug = debug
        self.original_weapon = original_weapon
        self.weapons_list = [
            light_melee_weapon(),
            medium_melee_weapon(),
            heavy_melee_weapon(),
            very_heavy_melee_weapon(),
            medium_melee_weapon(),
            medium_pistol(),
            heavy_pistol(),
            very_heavy_pistol(),
            smg(),
            heavy_smg(),
            shotgun(),
            assault_rifle(),
            sniper_rifle(),
            bows_and_crossbows(),
            grenade_launcher(),
            rocket_launcher(),
            flame_thrower()
        ]
        name_default = original_weapon.name if original_weapon is not None else ''
        self.name_edit = urwid.Edit('Name: ', name_default)

        weapon_radio_group = []
        self.weapon_radio_buttons = []
        for weapon in self.weapons_list:
            if self.original_weapon is not None and weapon.name == self.original_weapon.name:
                    self.weapon_radio_buttons.append(
                        urwid.RadioButton(weapon_radio_group, weapon.name, state=True)),
            else:
                self.weapon_radio_buttons.append(
                    urwid.RadioButton(weapon_radio_group, weapon.name)
                )

        if original_weapon is None:
            self.weapon_radio_buttons.append(urwid.RadioButton(weapon_radio_group, 'empty', state=True))
        else:
            self.weapon_radio_buttons.append(urwid.RadioButton(weapon_radio_group, 'empty'))

        self.grid = urwid.GridFlow(self.weapon_radio_buttons, 20, 1, 0, 'left')

        ok_button = CardButton('ok', on_press=self.accept_change)
        cancel_button = CardButton('Cancel', on_press=lambda *args: self._emit('close', None))

        quality_radio_group = []
        self.poor_quality_radio = urwid.RadioButton(quality_radio_group, 'Poor')
        self.standard_quality_radio = urwid.RadioButton(quality_radio_group, 'Standard', state=True)
        self.excellent_quality_radio = urwid.RadioButton(quality_radio_group, 'Excellent')

        self.radio_button_grid = urwid.GridFlow([
            self.poor_quality_radio,
            self.standard_quality_radio,
            self.excellent_quality_radio,
        ], 25, 1, 0, 'center')

        self.widget_buttons = urwid.GridFlow(
            [ok_button, cancel_button],
            25, 1, 1, 'center'
        )

        self.pile = urwid.Pile([
            self.name_edit,
            self.grid,
            urwid.Divider('-'),
            self.radio_button_grid,
            urwid.Divider('-'),
            self.widget_buttons
        ])
        super().__init__(self.pile)

    def accept_change(self, button):
        selected_weapon = None
        for btn in self.weapon_radio_buttons:
            if btn.state:
                selected_weapon = btn.label
                break

        self.change_weapon(selected_weapon)

    def set_weapon_properties(self, weapon):
        custom_name = self.name_edit.get_edit_text()
        if custom_name != '':
            weapon.name = custom_name

    def change_weapon(self, weapon_name: str):
        if weapon_name == 'empty':
            self._emit('close', weapon_name)
            return
        for weapon in self.weapons_list:
            if weapon_name == weapon.name:
                self.set_weapon_properties(weapon)
                if self.standard_quality_radio.get_state():
                    self.debug("Weapon Quality Standard")
                    self._emit('close', weapon)
                elif self.poor_quality_radio.get_state():
                    weapon.make_poor_quality()
                    self.debug("Weapon Quality Poor")
                    self._emit('close', weapon)
                elif self.excellent_quality_radio.get_state():
                    self.debug("Weapon Quality Excellent")
                    weapon.make_excellent_quality()
                    self._emit('close', weapon)


