import urwid
from random import randint
import uuid

from cpr.components.mook_card.stats_component import generate_stats_grid_contents,\
    generate_secondary_stats_grid_contents
from cpr.components.mook_card.combat_component import CombatZone
from cpr.components.mook_card.skills_component import SkillList


class MookCard(urwid.WidgetWrap):

    def __init__(self, mook_obj, event_handler, debug, alt_style=False):
        self.id = uuid.uuid1()
        self.event_handler = event_handler
        self.debug = debug
        # self.debug(urwid.signals.regiser)

        self.cell_width = 10
        self.h_sep = 1
        self.v_sep = 1
        self.align = 'center'

        self.mook = mook_obj

        # self.weapons_armor_cols = urwid.Columns(
        #     self.generate_weapons_armor_combat_content()
        # )

        self.special_widget = \
            urwid.Text('Special: ' + ', '.join(self.mook.special))

        self.pile = urwid.Pile([
            urwid.Columns([
                generate_stats_grid_contents(self.mook),
                (5, urwid.Button('X', on_press=self.close_card))
                ]
            ),
            urwid.Divider('-'),
            generate_secondary_stats_grid_contents(self.mook),
            urwid.Divider('-'),
            CombatZone(self.mook, self.roll, debug=self.debug),
            urwid.Divider('-'),
            SkillList(self.mook, self.roll),
            urwid.Divider('-'),
            self.special_widget,
        ])
        self.line_box = urwid.LineBox(self.pile,
                                      title=self.mook.name,
                                      title_align='left')
        if alt_style:
            self.line_box = urwid.AttrMap(self.line_box, 'card_alt')
        else:
            self.line_box = urwid.AttrMap(self.line_box, 'card')

        super().__init__(self.line_box)

    def close_card(self, button):
        self.debug('Closing Card...')
        self.event_handler('remove card', self)

    def roll(self, button):
        roll = randint(1, 10)
        if roll == 10:
            roll += randint(1, 10)
        if roll == 1:
            roll -= randint(1, 10)

        if button.label in self.mook.skills:
            check = roll + self.mook.skills[button.label]
            check_str = f'{button.label} check: {check}'
            self.debug(check_str)
            return check_str

        elif button.label in self.mook.weapons_by_name:
            weapon = self.mook.weapons_by_name[button.label]
            check = roll + self.mook.skills[weapon.skill]

            dmg = 0
            roll_list = []
            for i in range(weapon.damage):
                roll = randint(1,6)
                dmg += roll
                roll_list.append(roll)

            check_str = f'{button.label} attack: {check} || Damage: {roll_list} -> {dmg}'
            self.debug(check_str)
            return check_str

    def take_damage(self, button):
        self.debug("I've Been Hit...")
        damage_taken = urwid.IntEdit('Damage_taken: ', default=0)
        ablate_by = urwid.IntEdit('Ablate By: ', default=1)
        contents = urwid.Pile([
            damage_taken,
            ablate_by
        ])

        # TODO Maybe try using urwid.Overlay with overlay being self (card)
        pop_up = urwid.PopUpLauncher(contents)
        pop_up.create_pop_up = lambda *args: contents
        pop_up.get_pop_up_parameters = lambda *args: {'left': 0,
                                                     'top':1,
                                                     'overlay_width':10,
                                                     'overlay_height': 10}
        pop_up.open_pop_up()
        self.debug('is there a pop up?')



