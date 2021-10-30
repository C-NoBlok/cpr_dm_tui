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
        weapon_buttons = []
        for weapon in self.weapons_list:
            weapon_buttons.append(
                SkillButton(weapon.name, on_press=self.change_weapon)
            )

        self.grid = urwid.GridFlow(weapon_buttons, 20, 1, 0, 'left')

        cancel_button = CardButton('Cancel', on_press=lambda *args: self._emit('close', None))

        quality_radio_group = []
        self.poor_quality_radio = urwid.RadioButton(quality_radio_group, 'Poor')
        self.standard_quality_radio = urwid.RadioButton(quality_radio_group, 'Standard', state=True)
        self.excellent_quality_radio = urwid.RadioButton(quality_radio_group, 'Excellent')

        self.radio_button_grid = urwid.GridFlow([
            self.poor_quality_radio,
            self.standard_quality_radio,
            self.excellent_quality_radio
        ], 25, 1, 0, 'center')


        self.pile = urwid.Pile([
            self.grid,
            urwid.Divider('-'),
            self.radio_button_grid,
            urwid.Divider('-'),
            urwid.Padding(cancel_button, 'center', width=('relative', 10))
        ])
        super().__init__(self.pile)

    def change_weapon(self, button):
        for weapon in self.weapons_list:
            if button.label == weapon.name:
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


