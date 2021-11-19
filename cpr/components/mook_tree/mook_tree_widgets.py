import urwid


class StartCollapsedWidget(urwid.TreeWidget):
    def __init__(self, node):
        super().__init__(node)
        self.expanded = False
        self.update_expanded_icon()
        self._w = urwid.AttrMap(self._w, 'mook_list', 'focus')


class MookTreeWidget(urwid.TreeWidget):
    def __init__(self, node):
        super().__init__(node)
        self._w = urwid.AttrMap(self._w, 'mook_list', 'focus')

    def selectable(self):
        return True

    def get_display_text(self):
        return self._node.get_key()


class MookNode(urwid.TreeNode):

    def load_widget(self):
        return MookTreeWidget(self)