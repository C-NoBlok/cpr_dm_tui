import urwid

from cpr.components.mook_tree.mook_tree_widgets import StartCollapsedWidget, MookNode
from cpr.mooks import grunts as core_grunts, lieutenants as core_lieutenants, mini_bosses as core_mini_bosses, \
    bosses as core_bosses


class CoreMookTypeNode(urwid.ParentNode):
    def __init__(self, value, parent=None, key=None):
        super().__init__(value, parent, key)
        self.expanded = False
        self._child_keys = [
            'Grunts',
            'Lieutenants',
            'Mini Boss',
            'Boss'
        ]

    def load_widget(self):
        return StartCollapsedWidget(self)

    def load_child_node(self, key):
        children = {
            'Grunts': CoreMookListNode('', parent=self, key='Grunts'),
            'Lieutenants': CoreMookListNode('', parent=self, key='Lieutenants'),
            'Mini Boss': CoreMookListNode('', parent=self, key='Mini Boss'),
            'Boss': CoreMookListNode('', parent=self, key='Boss')
        }
        return children[key]


class CoreMookListNode(urwid.ParentNode):
    def __init__(self, value, parent=None, key=None):
        super().__init__(value, parent, key)
        if parent.get_key() == 'Core':
            if key == 'Grunts':
                self._child_keys = list(core_grunts.keys())
            elif key == 'Lieutenants':
                self._child_keys = list(core_lieutenants.keys())
            elif key == 'Mini Boss':
                self._child_keys = list(core_mini_bosses.keys())
            elif key == 'Boss':
                self._child_keys = list(core_bosses.keys())
            else:
                self._child_keys = ['such empty...']
        else:
            self._child_keys = ['such empty...']

    def load_child_node(self, key):
        return MookNode('', parent=self, key=key)

    def load_widget(self):
        return StartCollapsedWidget(self)