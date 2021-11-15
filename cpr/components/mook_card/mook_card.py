import urwid
from random import randint
import uuid
import json
from pathlib import Path
import os

from cpr.components.mook_card.stats import Stats

from cpr.components.mook_card.combat import CombatZone
from cpr.components.mook_card.skills import SkillList
from cpr.components.buttons import BoxButton, CardButton
from cpr.components.unicode_map import pencil, floppy_disk, right_arrow_with_tail, double_lines_horizontal
from cpr.components.event_log import EventLog
from cpr.components.mook_card.change_skills import ChangeSkillsWidget
from cpr.components.mook_card.change_name import ChangeName


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
        self.widget_side_buttons = None

        self.delete_button = CardButton('X', on_press=self.close_card)
        self.min_max = CardButton('-', on_press=self.collapse)
        self.edit_save_button = CardButton('edit', on_press=self.toggle_editable)

        self.stats = None
        self.combat_zone = None
        self.skills = None
        self.special_widget = None

        self.mook = mook_obj

        self.build_card()
        super().__init__(self.card_placeholder)

    def build_card(self):
        self.stats = Stats(self.mook, self.event_handler, self.event_log, self.debug)
        self.combat_zone = CombatZone(self,
                                      self.mook, self.roll,
                                      self.event_log, debug=self.debug)
        self.skills = SkillList(self, self.mook, self.roll)
        self.special_widget = \
            urwid.Edit('Special: ' + ', '.join(self.mook.special))

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

        self.widget_side_buttons = self.create_min_max_delete_buttons()
        self.pile = urwid.Pile([
            urwid.Columns([
                self.stats,
                (12, self.widget_side_buttons)
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

        if self.editable:
            self.enable_editing()

        self.card_placeholder.original_widget = self.line_box

    def build_update_skills_widget(self, button):
        self.debug(button)
        change_skills_widget = ChangeSkillsWidget(self.mook, self.debug)
        self.card_placeholder.original_widget = change_skills_widget
        urwid.connect_signal(change_skills_widget, 'close', self.close_update_skill_widget)

    def close_update_skill_widget(self, widget, data):
        self.debug('Closing update skills widget')
        self.debug(f'widget: {widget}')
        self.debug(f'data: {data}')
        self.debug(self.mook.skills)
        self.build_card()

    def create_min_max_delete_buttons(self):
        return urwid.Pile(
            [urwid.Columns([
                (5, self.min_max),
                (5, self.delete_button)
            ]),
                urwid.Columns([(10, self.edit_save_button)]),
            ],
        )

    def enable_editing(self):
        self.stats.enable_editing()
        self.combat_zone.enable_editing()
        save_as_button = urwid.Columns(
            [(10, CardButton('Save As', on_press=self.save_mook))])
        edit_skills_button = urwid.Columns(
            [(10, CardButton('Edit Skills', on_press=self.build_update_skills_widget))])
        self.debug(self.widget_side_buttons.contents)
        self.widget_side_buttons.contents.append((save_as_button, self.widget_side_buttons.options()))
        self.widget_side_buttons.contents.append((edit_skills_button, self.widget_side_buttons.options()))

        if self.mook.custom:
            delete_mook = urwid.Columns(
                [(10, CardButton('Delete', on_press=self.delete_mook))])
            self.widget_side_buttons.contents.append((delete_mook,
                                                      self.widget_side_buttons.options()))

        self.edit_save_button.button._label.set_text('Stop Edit')
        self.editable = True

    def disable_editing(self):
        self.stats.disable_editing()
        self.combat_zone.disable_editing()
        self.widget_side_buttons.contents = self.widget_side_buttons.contents[:2]
        self.edit_save_button.button._label.set_text('Edit')
        self.editable = False

    def toggle_editable(self, button):
        self.debug('making_editable')
        if not self.editable:
            self.enable_editing()
        else:
            self.disable_editing()

    def save_mook(self, button):
        self.debug('Exporting Mooks')
        change_name_widget = ChangeName(self.mook, self.debug)
        urwid.connect_signal(change_name_widget, 'close', self.close_name_change_widget)
        self.card_placeholder.original_widget = change_name_widget

    def delete_mook(self, button):
        self.debug('Deleting Mook...')
        user_folder = Path().home() / '.cpr'
        file_path = user_folder / f'{self.mook.name}.mook'
        if file_path.exists():
            os.remove(file_path)
        self.event_handler('refresh_mook_list', None)

    def close_name_change_widget(self, widget, accept_changes):
        if not accept_changes:
            self.build_card()
            return

        user_folder = Path().home() / '.cpr'
        file_path = user_folder / f'{self.mook.name}.mook'
        self.mook.custom = True

        with open(file_path, 'w') as f:
            json.dump(self.mook.to_dict(), f)

        self.event_handler('refresh_mook_list', None)
        self.build_card()

    def keypress(self, size, key):
        self.debug(f'card key: {key}')

        if isinstance(self.card_placeholder.original_widget, ChangeName):
            return self.card_placeholder.original_widget.keypress(size, key)

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
