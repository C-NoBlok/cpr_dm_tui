import urwid
from random import randint
import uuid

from cpr.components.mook_card.stats import Stats

from cpr.components.mook_card.combat import CombatZone
from cpr.components.mook_card.skills import SkillList
from cpr.components.box_button import BoxButton
from cpr.components.emoji_map import pencil, floppy_disk


class MookCard(urwid.WidgetWrap, urwid.WidgetContainerMixin):


    def __init__(self, mook_obj, event_handler, debug, alt_style=False):
        self.id = uuid.uuid1()
        self.event_handler = event_handler
        self.debug = debug
        # self.debug(urwid.signals.regiser)

        self.cell_width = 10
        self.h_sep = 1
        self.v_sep = 1
        self.align = 'center'

        self.is_collapsed = False

        self.delete_button = urwid.Button('X', on_press=self.close_card)
        self.min_max = urwid.Button('-', on_press=self.collapse)
        self.edit_save_button = urwid.Button('edit', on_press=self.toggle_editable)
        self.edit_save_button = urwid.AttrWrap(self.edit_save_button, 'button', 'button_focus')
        self.edit_save_button = urwid.AttrWrap(self.edit_save_button, 'center')

        self.mook = mook_obj
        self.stats = Stats(self.mook, self.event_handler, self.debug)
        self.combat_zone = CombatZone(self.mook, self.roll, debug=self.debug)
        self.skills = SkillList(self.mook, self.roll)

        self.special_widget = \
            urwid.Edit('Special: ' + ', '.join(self.mook.special))

        self.main_content = urwid.Pile([
            urwid.Divider('-'),
            self.combat_zone,
            urwid.Divider('-'),
            self.skills,
            urwid.Divider('-'),
            self.special_widget,
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
        if alt_style:
            self.line_box = urwid.AttrMap(self.line_box, 'card_alt', 'card_focus')
        else:
            self.line_box = urwid.AttrMap(self.line_box, 'card', 'card_focus')

        self.line_box._command_map['e'] = lambda *args: self.roll('evasion')
        self._selectable = True

        super().__init__(self.line_box)

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
        if self.stats.toggle_editable():
            self.edit_save_button._label.set_text('Save')
        else:
            self.edit_save_button._label.set_text('Edit')

    def keypress(self, size, key):
        self.debug(f'card key: {key}')
        card_key_funcs = {
            'e': lambda: self.roll('evasion'),
            'p': lambda: self.roll('perception'),
            'a': lambda: self.roll('athletics'),
            'b': lambda: self.roll('brawling'),
            'm': lambda: self.roll('melee weapon'),
            'h': lambda: self.roll('handgun'),
            's': lambda: self.roll('shoulder arms'),
            'H': lambda: self.roll('heavy weapons'),
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
            self.debug(f'No Item Equiped in Slot {key}')
            return

        return self.pile.keypress(size, key)

        # unhandled = self.stats.keypress(size, key)
        # if unhandled:
        #     unhandled = self.combat_zone.keypress(size, key)
        # if unhandled:
        #     unhandled = self.skills.keypress(size, key)
        # # if unhandled:
        # #     unhandled = self.special_widget.keypress(size, key)


    def collapse(self, button):
        self.debug('colapsing card.')
        if self.is_collapsed:
            self.main_placeholder.original_widget = self.main_content
            self.min_max._label.set_text('-')
            self.is_collapsed = False
        else:
            self.main_placeholder.original_widget = urwid.Divider('/')
            self.min_max._label.set_text('+')
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

        if skill_label in self.mook.skills:
            check = roll + self.mook.skills[skill_label]
            check_str = f'{skill_label} check: {check}'
            self.debug(check_str)
            return check_str

        elif skill_label in self.mook.weapons_by_name:
            weapon = self.mook.weapons_by_name[skill_label]
            check = roll + self.mook.skills[weapon.skill]

            dmg = 0
            roll_list = []
            for i in range(weapon.damage):
                roll = randint(1,6)
                dmg += roll
                roll_list.append(roll)

            check_str = f'{skill_label} attack: {check} || Damage: {roll_list} -> {dmg}'
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



