import urwid
from random import randint
import uuid

from cpr.components.mook_card.stats import Stats

from cpr.components.mook_card.combat import CombatZone
from cpr.components.mook_card.skills import SkillList
from cpr.components.buttons import BoxButton, CardButton
from cpr.components.unicode_map import pencil, floppy_disk, right_arrow_with_tail, double_lines_horizontal
from cpr.components.event_log import EventLog


class MookCard(urwid.WidgetWrap, urwid.WidgetContainerMixin):

    def __init__(self, mook_obj, event_handler, debug, alt_style=False):
        self.id = uuid.uuid1()
        self.editable = False
        self.event_handler = event_handler
        self.debug = debug
        self.event_log = EventLog(debug=debug)
        self.alt_style = alt_style
        # self.debug(urwid.signals.regiser)

        self.cell_width = 10
        self.h_sep = 1
        self.v_sep = 1
        self.align = 'center'

        self.is_collapsed = False

        # Define components
        self.card_placeholder = urwid.WidgetPlaceholder(urwid.Text(''))
        self.main_content = None
        self.main_placeholder = None
        self.pile = None
        self.line_box = None

        self.delete_button = CardButton('X', on_press=self.close_card)
        self.min_max = CardButton('-', on_press=self.collapse)
        self.edit_save_button = CardButton('edit', on_press=self.toggle_editable)

        self.mook = mook_obj
        self.stats = Stats(self.mook, self.event_handler, self.event_log, self.debug)

        self.combat_zone = CombatZone(self,
                                      self.mook, self.roll,
                                      self.event_log, debug=self.debug)

        self.skills = SkillList(self.mook, self.roll)

        self.special_widget = \
            urwid.Edit('Special: ' + ', '.join(self.mook.special))

        self.build_card()
        super().__init__(self.card_placeholder)

    def build_card(self):
        self.main_content = urwid.Pile([
            urwid.Divider(double_lines_horizontal),
            self.combat_zone,
            urwid.Divider(double_lines_horizontal),
            self.skills,
            urwid.Divider(double_lines_horizontal),
            self.special_widget,
            urwid.Divider(double_lines_horizontal),
            self.event_log
        ])

        self.main_placeholder = urwid.WidgetPlaceholder(self.main_content)

        self.pile = urwid.Pile([
            urwid.Columns([
                self.stats,
                (12, self.create_min_max_delete_buttons())
            ]
            ),
            self.main_placeholder
        ])
        self.line_box = urwid.LineBox(self.pile,
                                      title=self.mook.name,
                                      title_align='left')
        if self.alt_style:
            self.line_box = urwid.AttrMap(self.line_box, 'card_alt', 'card_focus')
        else:
            self.line_box = urwid.AttrMap(self.line_box, 'card', 'card_focus')

        self._selectable = True

        self.card_placeholder.original_widget = self.line_box


    def create_min_max_delete_buttons(self):
        return urwid.Pile(
            [urwid.Columns([
                (5, self.min_max),
                (5, self.delete_button)
            ]),
                urwid.Padding(self.edit_save_button, align='center', width=('relative', 65))]
        )

    def toggle_editable(self, button):
        self.debug('making_editable')
        if not self.editable:
            self.stats.enable_editing()
            self.combat_zone.enable_editing()
            self.edit_save_button.button._label.set_text('Save')
            self.editable = True
        else:
            self.stats.disable_editing()
            self.combat_zone.disable_editing()
            self.edit_save_button.button._label.set_text('Edit')
            self.editable = False

    def keypress(self, size, key):
        self.debug(f'card key: {key}')
        card_key_funcs = {
            'e': lambda: self.roll('Evasion'),
            'p': lambda: self.roll('Perception'),
            'a': lambda: self.roll('Athletics'),
            'b': lambda: self.roll('Brawling'),
            'm': lambda: self.roll('Melee Weapon'),
            'h': lambda: self.roll('Handgun'),
            's': lambda: self.roll('Shoulder Arms'),
            'H': lambda: self.roll('Heavy Weapons'),
            'meta 1': lambda: self.roll(self.mook.weapons[0].name),
            'meta 2': lambda: self.roll(self.mook.weapons[1].name),
            'meta 3': lambda: self.roll(self.mook.weapons[2].name),
            'meta 4': lambda: self.roll(self.mook.weapons[3].name),
        }
        try:
            if key in card_key_funcs:
                card_key_funcs[key]()
                return
        except IndexError:
            self.event_log.event(f'No Item Equiped in Slot {key}')
            return

        if self.card_placeholder.original_widget == self.line_box:
            return self.pile.keypress(size, key)
        else:
            return self.card_placeholder.original_widget.keypress(size, key)

    def collapse(self, button):
        self.debug('colapsing card.')
        if self.is_collapsed:
            self.main_placeholder.original_widget = self.main_content
            self.min_max.button._label.set_text('-')
            self.event_log.max_lines = 5
            self.event_log.build_widget()
            self.is_collapsed = False
        else:
            self.main_placeholder.original_widget = urwid.Pile([
                urwid.Divider('/'),
                self.event_log
                ])
            self.min_max.button._label.set_text('+')
            self.event_log.max_lines = 2
            self.event_log.build_widget()
            self.is_collapsed = True

    def close_card(self, button):
        self.debug('Closing Card...')
        self.event_handler('remove card', self)

    def roll(self, button):
        roll = randint(1, 10)
        if roll == 10:
            roll += randint(1, 10)
        if roll == 1:
            roll -= randint(1, 10)

        if isinstance(button, urwid.Widget):
            skill_label = button.label
        elif isinstance(button, str):
            skill_label = button
        else:
            raise TypeError('button is not of type: String, urwid.Button')

        if skill_label in self.mook.skills.skills_by_name:
            skill = self.mook.skills.skills_by_name[skill_label]
            check = roll + skill.rank + self.mook.stats.to_dict()[skill.base_stat]
            check_str = f'{skill_label} check: {check}'

        elif skill_label in self.mook.weapons_by_name:
            weapon = self.mook.weapons_by_name[skill_label]
            weapon_modifier = weapon.modifier
            skill = self.mook.skills.to_dict()[weapon.skill]
            skill_rank = skill['rank']
            skill_stat = self.mook.stats.to_dict()[skill['base_stat']]
            self.debug(f'skill: {skill}\n {roll} + {skill_rank} + {skill_stat}')
            check = roll + skill_rank + skill_stat + weapon_modifier

            dmg = 0
            roll_list = []
            for i in range(weapon.damage):
                dmg_roll = randint(1, 6)
                dmg += dmg_roll
                roll_list.append(dmg_roll)

            check_str = f'{skill_label} attack: {check} || Damage: {roll_list} -> {dmg}'

        else:
            self.debug(f'Could not find instances of: {skill_label}')
            self.debug(f'{self.mook.skills} -> \n by_name: {self.mook.skills.skills_by_name}')
            return ''

        check_str = f'Roll: {roll} || {check_str}'
        self.event_log.event(check_str)
        return check_str
