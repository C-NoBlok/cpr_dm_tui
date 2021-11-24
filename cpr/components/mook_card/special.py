import urwid

from cpr.mooks.mook import Mook


class SpecialWidget(urwid.WidgetWrap):

    def __init__(self, event_handler, debug, mook: Mook):
        self.event_hanlder = event_handler
        self.debug = debug
        self.mook = mook

        self.main_placeholder = None
        self.build_widget()
        super().__init__(self.main_placeholder)


    def build_widget(self):
        weapons = self.mook.weapons
        ammo_edit_widgets = []
        for weapon in weapons:
            if not hasattr(weapon, 'total_ammo'):
                continue
            weapon_edit = urwid.IntEdit(weapon.name + ': ', weapon.total_ammo)
            urwid.connect_signal(weapon_edit, 'change', self.update_ammo)
            weapon_edit = urwid.AttrMap(weapon_edit, '', 'edit_focus')
            ammo_edit_widgets.append(weapon_edit)

        ammo_widget = urwid.Columns(
            [
                (8, urwid.Text('Ammo: ')),
                urwid.GridFlow(ammo_edit_widgets, 25, 1, 1, 'left')
            ]
        )
        # gear_cyberware =

        gear = urwid.LineBox(ammo_widget)

        if self.main_placeholder is None:
            self.main_placeholder = urwid.WidgetPlaceholder(gear)
        else:
            self.main_placeholder.original_widget = gear

    def update_ammo(self, widget, data):
        self.debug(widget.caption)
        self.debug(data)
        for name, weapon in self.mook.weapons_by_name.items():
            if name in widget.caption:
                self.debug(f'updated {widget.caption} ammo to {data}')
                weapon.total_ammo = data


