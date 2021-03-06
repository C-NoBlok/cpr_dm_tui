from copy import deepcopy

import urwid

from cpr.components.mook_tree.core_mook_tree import CoreMookTypeNode
from cpr.components.mook_tree.custom_mook_tree import CustomMookTypeNode
from cpr.components.mook_tree import load_custom_mooks
from cpr.components.mook_tree.mook_tree_widgets import MookTreeWidget
from cpr.mooks import grunts as core_grunts
from cpr.mooks import lieutenants as core_lieutenants
from cpr.mooks import mini_bosses as core_mini_bosses
from cpr.mooks import bosses as core_bosses
from cpr.mooks.grunts.bodyguards import Bodyguard
from cpr.mooks.grunts.booster_ganger import BoosterGanger
from cpr.mooks.grunts.security_operative import SecurityOperative

core_grunt_list = [Bodyguard, BoosterGanger, SecurityOperative]


class MookTreeMainWidget(urwid.WidgetWrap):

    def __init__(self, event_handler, debug):
        self.event_handler = event_handler
        self.debug = debug
        self.custom_mook_list = None
        self.tree = None
        self.tree_walker = None
        self.top_node = None
        self.main_placeholder = None
        self.build_widget()

        super().__init__(self.main_placeholder)

    def build_widget(self):
        self.debug('Building Mook Tree...')
        self.custom_mook_list = load_custom_mooks()
        self.top_node = TopNode(self.custom_mook_list)
        self.tree_walker = urwid.TreeWalker(
            self.top_node
        )
        self.tree = urwid.TreeListBox(
            self.tree_walker
        )
        if self.main_placeholder is None:
            self.main_placeholder = urwid.WidgetPlaceholder(self.tree)
        else:
            self.debug('Replacing')
            self.main_placeholder.original_widget = self.tree

    def keypress(self, size, key):
        if key in ['enter', 'mouse_press']:
            self.add_selected_mook()
        else:
            return self.tree.keypress(size, key)

    def mouse_event(self, size, event, button, col, row, focus):
        self.tree.mouse_event(size, event, button, col, row, focus)
        if button == 1:
            self.add_selected_mook()

    def add_selected_mook(self):
        focus_node = self.tree_walker.get_focus()[1]
        self.debug(focus_node.get_key())
        self.debug(f'Depth: {focus_node.get_depth()}')
        if focus_node.get_depth() > 2:
            node_parent =focus_node.get_parent()
            mook_type = node_parent.get_key()
            self.debug(mook_type)
            if node_parent.get_parent().get_key() == 'Core':
                if mook_type == 'Grunts':
                    self.event_handler('add_mook_to_roster', core_grunts[focus_node.get_key()])
                elif mook_type == 'Lieutenants':
                    self.event_handler('add_mook_to_roster', core_lieutenants[focus_node.get_key()])
                elif mook_type == 'Mini Boss':
                    self.event_handler('add_mook_to_roster', core_mini_bosses[focus_node.get_key()])
                elif mook_type == 'Boss':
                    self.event_handler('add_mook_to_roster', core_bosses[focus_node.get_key()])
                else:
                    self.debug(f'Unable to find mook type {mook_type}')
            elif node_parent.get_parent().get_key() == 'Custom':
                self.debug('Adding Custom Mook')
                mook_name = focus_node.get_key()
                mook = list(filter(lambda x: x.name == mook_name, self.custom_mook_list))[0]
                self.event_handler('add_mook_to_roster', deepcopy(mook))


class TopNode(urwid.ParentNode):
    def __init__(self, custom_mook_list=[]):
        super().__init__('', parent=None, key='Mooks')
        self._child_keys = ['Core', 'Custom']
        self.custom_mook_list = custom_mook_list

    def load_child_node(self, key):
        if key == 'Core':
            return CoreMookTypeNode('', parent=self, key=key)
        elif key == 'Custom':
            return CustomMookTypeNode('', parent=self, key=key, custom_mooks=self.custom_mook_list)

    def load_widget(self):
        return MookTreeWidget(self)


