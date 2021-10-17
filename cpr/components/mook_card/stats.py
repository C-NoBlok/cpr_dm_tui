import urwid


class Stats(urwid.WidgetWrap):
    def __init__(self, mook, event_handler, debug):
        self.event_handler = event_handler
        self.debug = debug
        self.mook = mook
        self.editable = False

        self.cell_width = 10
        self.h_seperation = 1
        self.v_seperation =1
        self.align = 'left'

        self.main_stats = [
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

        self.editable_stats = [
            urwid.IntEdit(f'INT: ', default=self.mook.stats.INT,),
            urwid.IntEdit(f'REF: ', default=self.mook.stats.REF),
            urwid.IntEdit(f'DEX: ', default=self.mook.stats.DEX),
            urwid.IntEdit(f'TECH: ', default=self.mook.stats.TECH),
            urwid.IntEdit(f'COOL: ', default=self.mook.stats.COOL),
            urwid.IntEdit(f'WILL: ', default=self.mook.stats.WILL),
            urwid.IntEdit(f'LUCK:', default=self.mook.stats.LUCK),
            urwid.IntEdit(f'MOVE: ', default=self.mook.stats.MOVE),
            urwid.IntEdit(f'BODY: ', default=self.mook.stats.BODY),
            urwid.IntEdit(f'EMP: ', default=self.mook.stats.EMP)
        ]

        for editable_item in self.editable_stats:
            urwid.connect_signal(editable_item, 'change', self.update_mook)

        self.stat_grid_flow = urwid.GridFlow(
            self.main_stats,
            self.cell_width,
            self.h_seperation,
            self.v_seperation,
            self.align
        )

        self.editable_stat_grid_flow = urwid.GridFlow(
            self.editable_stats,
            self.cell_width,
            self.h_seperation,
            self.v_seperation,
            self.align
        )
        self.secondary_stats_component = urwid.WidgetPlaceholder(self.generate_secondary_stats_contents())
        self.main_placeholder = urwid.WidgetPlaceholder(self.stat_grid_flow)
        super().__init__(self.main_placeholder)

    @property
    def main_stats_component(self):
        return self.main_placeholder

    def generate_secondary_stats_contents(self):
        secondary_stat_contents = [
            urwid.IntEdit(f'    Hit Points: ', default=self.mook.hp),

            urwid.Pile([urwid.Text(f'Seriously Wounded: {self.mook.seriously_wounded}'),
                        urwid.IntEdit('Death Save: ', self.mook.death_save)]),

            self.create_armor_widget()
        ]
        grid = urwid.GridFlow(secondary_stat_contents, 23, 1, 0, 'left')
        return grid


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
        return armor_elem

    def toggle_editable(self):
        if self.editable:
            self.main_placeholder.original_widget = self.stat_grid_flow
            self.editable = False

        else:
            self.main_placeholder.original_widget = self.editable_stat_grid_flow
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
            self.mook.stats.LUCK = int(num)
        if 'MOVE' in object.caption:
            self.mook.stats.MOVE = int(num)
        if 'BODY' in object.caption:
            self.mook.stats.BODY = int(num)
        if 'EMP' in object.caption:
            self.mook.stats.EMP = int(num)

        self.mook.hp = self.mook.stats.max_hp
        self.secondary_stats_component.original_widget = self.generate_secondary_stats_contents()

        self.debug(self.mook.__dict__)




