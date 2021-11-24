import urwid

from cpr.mooks.mook import Mook


class SpecialWidget(urwid.WidgetWrap):

    def __init__(self, event_handler, debug, mook: Mook):
        self.event_hanlder = event_handler
        self.debug = debug
        self.mook = mook
        self.edits = None
        self.grid = None

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

        ammo_widget = urwid.GridFlow(ammo_edit_widgets, 25, 1, 1, 'left')
        ammo_widget = urwid.LineBox(ammo_widget, title='Ammo')

        equipment = urwid.LineBox(self.generate_editable_equipment(),
                                  title='Gear')
        gear = urwid.Pile([
            ammo_widget,
            equipment
        ])

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

    def generate_editable_equipment(self):
        self.edits = [urwid.Edit('', item) for item in self.mook.special]
        self.edits.append(urwid.Edit('', ''))
        wrapped_edits = [self.wrap_edit(edit) for edit in self.edits]
        self.grid = urwid.GridFlow(wrapped_edits, 25, 1, 1, 'left')
        return self.grid

    def wrap_edit(self, edit):
        urwid.connect_signal(edit, 'change', self.update_special)
        edit._selectable = True
        return urwid.AttrMap(edit, '', 'edit_focus')

    def update_special(self, widget, data):
        widget_index = self.edits.index(widget)
        if widget_index == len(self.edits) - 1:
            self.mook.special.append(data)
            edit = urwid.Edit('', '')
            self.edits.append(edit)
            self.grid.contents.append((self.wrap_edit(edit), self.grid.options()))
        self.mook.special.pop(widget_index)
        self.mook.special.insert(widget_index, data)

