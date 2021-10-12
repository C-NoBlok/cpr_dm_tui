import urwid

def generate_stats_grid_contents(mook, callback=None):
    content = [
        urwid.Text(f'INT: {mook.stats.INT}', align='center'),
        urwid.Text(f'REF: {mook.stats.REF}', align='center'),
        urwid.Text(f'DEX: {mook.stats.DEX}', align='center'),
        urwid.Text(f'TECH: {mook.stats.TECH}', align='center'),
        urwid.Text(f'COOL: {mook.stats.COOL}', align='center'),
        urwid.Text(f'WILL: {mook.stats.WILL}', align='center'),
        urwid.Text(f'LUCK: {mook.stats.LUCK}', align='center'),
        urwid.Text(f'MOVE: {mook.stats.MOVE}', align='center'),
        urwid.Text(f'BODY: {mook.stats.BODY}', align='center'),
        urwid.Text(f'EMP: {mook.stats.EMP}', align='center')
    ]

    cell_width = 10
    h_seperation = 1
    v_seperation =1
    align = 'center'

    stat_grid_flow = urwid.GridFlow(
        content,
        cell_width,
        h_seperation,
        v_seperation,
        align
    )
    return stat_grid_flow


def generate_secondary_stats_grid_contents(mook, callback=None):
    contents = [
        urwid.IntEdit(f'    Hit Points: {mook.hp}'),

        urwid.Pile([urwid.Text(f'Seriously Wounded: {mook.seriously_wounded}'),
                    urwid.IntEdit('Death Save: ', mook.death_save)]),

        create_armor_widget(mook)
    ]
    contents = urwid.GridFlow(contents, 23, 1, 0, 'left')

    return contents


def create_armor_widget(mook):
    armor_elem = urwid.Columns([
        (9, urwid.Text("Armor: ")),
        (9, urwid.Pile(
            [
                urwid.IntEdit('Head: ', mook.armor[-1]),
                urwid.IntEdit('Body: ', mook.armor[0])
            ]
        ))
    ])
    return armor_elem
