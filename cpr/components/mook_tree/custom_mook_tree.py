import urwid

from cpr.components.mook_tree import custom_mooks
from cpr.components.mook_tree.mook_tree_widgets import MookNode, StartCollapsedWidget


# I really don't like this here


def mook_type_filter(mook_type, mook_list):
    filtered_mooks = [mook for mook in mook_list if mook.mook_type == mook_type]
    return filtered_mooks


class CustomMookTypeNode(urwid.ParentNode):
    def __init__(self, value, parent=None, key=None):
        super().__init__(value, parent, key)
        self.expanded = False

    def load_child_keys(self):
        types = sorted(list(set([mook.mook_type for mook in custom_mooks])))
        return types

    def load_child_node(self, key):
        return CustomMookNode('', parent=self, key=key)


class CustomMookNode(urwid.ParentNode):
    def __init__(self, value, parent=None, key=None):
        super().__init__(value, parent, key)
        self.expanded = False
        self.mooks = mook_type_filter(key, custom_mooks)

    def load_child_keys(self):
        mooks = sorted(list([mook.name for mook in self.mooks]))
        return mooks

    def load_child_node(self, key):
        return MookNode('', parent=self, key=key)

    def load_widget(self):
        return StartCollapsedWidget(self)








