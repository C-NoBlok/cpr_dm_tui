import urwid
from cpr.components.buttons import SkillButton


def create_skill_buttons(mook, skills, col1_width=25, col2_width=6, on_press=None, is_weapon=False):
    contents = []
    for skill in skills:

        if not is_weapon:
            button_side_text = f' : {mook.skills[skill]}'
        else:
            button_side_text = f' : {mook.weapons_by_name[skill].damage}D6'

        skill_button = SkillButton(f'{skill}', on_press=on_press)
        skill_value = urwid.Text(button_side_text)
        # skill_value = urwid.AttrMap(skill_value, 'highlight')
        skill_cols = urwid.Columns([
            (col1_width, skill_button),
            (col2_width, skill_value)
        ])
        # skill_cols = urwid.AttrMap(skill_cols, 'skill_button')
        contents.append(skill_cols)
    return contents


def unpack_into_cols(elem_list, items_per_col=4):
    partitioned_list = []
    for i, item in enumerate(elem_list):
        if i % items_per_col == 0:
            if i != 0:
                partitioned_list.append(temp_list)
            temp_list = [item]
        else:
            temp_list.append(item)
    partitioned_list.append(temp_list)

    piles = []
    for item in partitioned_list:
        piles.append(urwid.Pile(item))

    return urwid.Columns(piles)