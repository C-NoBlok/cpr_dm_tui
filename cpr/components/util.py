import urwid


def find_signal_object(cls_string):
    for signal_class, signals in urwid.signals._signals.__dict__.items()['_supported']:
        if cls_string in signal_class:
            return signal_class, signals

