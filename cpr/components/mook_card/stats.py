import urwid

from cpr.components.mook_card.damage import TakeDamageDialog
from cpr.components.buttons import TakeDamageButton
from cpr.components.emoji_map import shield, mechanical_arm, explosion, cowboy


class Stats(urwid.WidgetWrap, urwid.WidgetContainerMixin):
    def __init__(self, mook, event_handler, debug):
        self.event_handler = event_handler
        self.debug = debug
        self.mook = mook
        self.editable = False

        self.cell_width = 10
        self.h_seperation = 1
        self.v_seperation =1
        self.align = 'left'

        self.secondary_stats_component = urwid.WidgetPlaceholder(self.generate_secondary_stats_contents())
        self.main_placeholder = urwid.WidgetPlaceholder(self.generate_primary_stats_content())

        super().__init__(urwid.Pile([
            self.main_placeholder,
            urwid.Divider('-'),
            self.secondary_stats_component,
            ])
        )

    @property
    def main_stats_component(self):
        return self.main_placeholder

    def generate_primary_stats_content(self):
        main_stats = [
            urwid.Text(f'INT: {self.mook.stats.INT}', align='center'),
            urwid.Text(f'REF: {self.mook.stats.REF}', align='center'),
            urwid.Text(f'DEX: {self.mook.stats.DEX}', align='center'),
            urwid.Text(f'TECH: {self.mook.stats.TECH}', align='center'),
            urwid.Text(f'COOL: {self.mook.stats.COOL}', align='center'),
            urwid.Text(f'WILL: {self.mook.stats.WILL}', align='center'),
            urwid.Text(f'LUCK: {self.mook.stats.LUCK}', align='center'),
            urwid.Text(f'MOVE: {self.mook.stats.MOVE}', align='center'),
            urwid.Text(f'BODY: {self.mook.stats.BODY}', align='center'),
            urwid.Text(f'EMP: {self.mook.stats.EMP}', align='center')
        ]
        grid = urwid.GridFlow(main_stats, self.cell_width, self.h_seperation, self.v_seperation, self.align)
        return grid

    def generate_editable_primary_stats_content(self):

        editable_stats = [
            self.wrap_int_edit(urwid.IntEdit(f'INT: ', default=self.mook.stats.INT,)),
            self.wrap_int_edit(urwid.IntEdit(f'REF: ', default=self.mook.stats.REF)),
            self.wrap_int_edit(urwid.IntEdit(f'DEX: ', default=self.mook.stats.DEX)),
            self.wrap_int_edit(urwid.IntEdit(f'TECH: ', default=self.mook.stats.TECH)),
            self.wrap_int_edit(urwid.IntEdit(f'COOL: ', default=self.mook.stats.COOL)),
            self.wrap_int_edit(urwid.IntEdit(f'WILL: ', default=self.mook.stats.WILL)),
            self.wrap_int_edit(urwid.IntEdit(f'LUCK:', default=self.mook.stats.LUCK)),
            self.wrap_int_edit(urwid.IntEdit(f'MOVE: ', default=self.mook.stats.MOVE)),
            self.wrap_int_edit(urwid.IntEdit(f'BODY: ', default=self.mook.stats.BODY)),
            self.wrap_int_edit(urwid.IntEdit(f'EMP: ', default=self.mook.stats.EMP))
        ]

        editable_stat_grid_flow = urwid.GridFlow(
            editable_stats,
            self.cell_width,
            self.h_seperation,
            self.v_seperation,
            self.align
        )

        return editable_stat_grid_flow

    def wrap_int_edit(self, edit):
        urwid.connect_signal(edit, 'change', self.update_mook)
        edit._selectable = True
        return urwid.AttrMap(edit, '', 'edit_focus')

    def generate_secondary_stats_contents(self):
        hp_edit = self.wrap_int_edit(urwid.IntEdit(f'    Hit Points: ', default=self.mook.hp))
        take_damage_button = TakeDamageButton(f'{explosion} Take Damage {explosion}', on_press=self.take_damage_dialog)
        secondary_stat_contents = [
            urwid.Pile([hp_edit, take_damage_button]),
            urwid.Pile([urwid.Text(f'Seriously Wounded: {self.mook.seriously_wounded}'),
                        self.wrap_int_edit(urwid.IntEdit('Death Save: ', self.mook.death_save))]),
            self.create_armor_widget()
        ]
        grid = urwid.GridFlow(secondary_stat_contents, 23, 1, 0, 'left')
        return grid

    def create_armor_widget(self):
        armor_elem = urwid.Columns([
            (9, urwid.Text("Armor: ")),
            (12, urwid.Pile(
                [
                    self.wrap_int_edit(urwid.IntEdit(f'{cowboy}Head: ', self.mook.armor['head'])),
                    self.wrap_int_edit(urwid.IntEdit(f'{mechanical_arm}Body: ', self.mook.armor['body']))
                ]
            ))
        ])
        return armor_elem

    def toggle_editable(self):
        if self.editable:
            self.main_placeholder.original_widget = self.generate_primary_stats_content()
            self.editable = False

        else:
            self.main_placeholder.original_widget = self.generate_editable_primary_stats_content()
            self.editable = True

        self.debug(f'Mook Editable: {self.editable}')
        return self.editable

    def update_mook(self, object, num):
        self.debug(f'{object.caption}: {num}')
        if num == '':
            return
        if 'INT' in object.caption:
            self.mook.stats.INT = int(num)
        if 'REF' in object.caption:
            self.mook.stats.REF = int(num)
        if 'DEX' in object.caption:
            self.mook.stats.DEX = int(num)
        if 'TECH' in object.caption:
            self.mook.stats.TECH = int(num)
        if 'COOL' in object.caption:
            self.mook.stats.COOL = int(num)
        if 'WILL' in object.caption:
            self.mook.stats.WILL = int(num)
        if 'LUCK' in object.caption:
            self.mook.hp = self.mook.stats.max_hp
            self.mook.stats.LUCK = int(num)
        if 'MOVE' in object.caption:
            self.mook.stats.MOVE = int(num)
        if 'BODY' in object.caption:
            self.mook.stats.BODY = int(num)
            self.mook.hp = self.mook.stats.max_hp
        if 'EMP' in object.caption:
            self.mook.stats.EMP = int(num)

        if 'Hit Points' in object.caption:
            if int(num) > self.mook.stats.max_hp:
                self.mook.hp = self.mook.stats.max_hp
            else:
                self.mook.hp = int(num)

        self.secondary_stats_component.original_widget = self.generate_secondary_stats_contents()

        self.debug(self.mook.__dict__)

    def take_damage_dialog(self, button):
        self.debug('OUCH!!!')
        dmg_dialog = TakeDamageDialog()
        self.main_placeholder.original_widget = dmg_dialog
        urwid.connect_signal(dmg_dialog, 'close', self.close_take_damage_dialog)
        self._w.set_focus(0)

    def close_take_damage_dialog(self, dmg_dialog: TakeDamageDialog, accept):
        self.debug(f'Accept Damage: {accept}')
        if accept:
            piece_ablated = 'body' if dmg_dialog.body.state else 'head'
            damage = dmg_dialog.damage_amount.value()
            ablate_by = dmg_dialog.ablate_by.value()

            damage_taken = damage - self.mook.armor[piece_ablated]
            if damage_taken > 0:
                if piece_ablated == 'head':
                    self.debug("Head Shot! Brutal Double Damage.")
                    damage_taken = damage_taken * 2
                self.mook.hp -= damage_taken
                self.mook.armor[piece_ablated] -= ablate_by

                self.debug(f'Damage Taken: {damage_taken}\n... '
                           f'{piece_ablated} armor ablated by: {ablate_by}')
            else:
                self.debug("Armor Stopped all Damage. Lucky!")

        self.main_placeholder.original_widget = self.generate_primary_stats_content()
        self.secondary_stats_component.original_widget = self.generate_secondary_stats_contents()






