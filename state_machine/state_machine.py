#     _________             .__
#    /   _____/____    _____|  |__ _____
#    \_____  \\__  \  /  ___/  |  \\__  \
#    /        \/ __ \_\___ \|   Y  \/ __ \_
#   /_______  (____  /____  >___|  (____  /
#           \/     \/     \/     \/     \/
#     _________       _____  __
#    /   _____/ _____/ ____\/  |_
#    \_____  \ /  _ \   __\\   __\
#    /        (  <_> )  |   |  |
#   /_______  /\____/|__|   |__|
#           \/
#   Copyright (c) 2021.

"""
all function for state machine
"""
from state_machine.exceptions import InvalidParentState


class Transition:
    def __init__(self, *states, **options):
        self.source = states[0]

class State:
    __do_by_entry = bool
    __do_by_exit = bool
    transition = list # type: list[Transition]
    __identifier = str

    def __init__(self, parent, do_by_entry=False, do_by_exit=False):
        self.do_by_entry = do_by_entry
        self.do_by_exit = do_by_exit
        self.transition = list()
        self.identifier = None
        if not isinstance(parent, State):
            raise InvalidParentState(parent)

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, value):
        self.__identifier = str(value)

    @property
    def do_by_entry(self):
        return self.__do_by_entry

    @do_by_entry.setter
    def do_by_entry(self, value):
        self.do_by_entry = value

    @property
    def do_by_exit(self):
        return self.__do_by_exit

    @do_by_exit.setter
    def do_by_exit(self, value):
        self.do_by_exit = value

    def _do(self):
        pass

    def _entry(self):
        if self.do_by_entry:
            self.do()
        self.entry()

    def _exit(self):
        if self.do_by_exit:
            self.do()
        self.exit()

    def _to(self, *states):
        transition = Transition(self, *states)
        self.transition.append(transition)
        return transition

    def do(self):
        pass

    def entry(self):
        pass

    def exit(self):
        pass

    @property
    def to(self):
        return self._proxy(self._to)


class BaseStateMachine:
    transitions = list
    states = list
    states_map = dict
    _current_state_value = str

    def __init__(self):
        self.transitions = list()
        self.states = list()
        self.states_map = dict()
        self.add_inherited()
        pass

    def add_inherited(cls, bases):
        for base in bases:
            for state in getattr(base, 'states', []):
                cls.add_state(state.identifier, state)
            for transition in getattr(base, 'transitions', []):
                cls.add_transition(transition.identifier, transition)

    def add_from_attributes(cls, attrs):
        for key, value in sorted(attrs.items(), key=lambda pair: pair[0]):
            if isinstance(value, State):
                cls.add_state(key, value)
            elif isinstance(value, Transition):
                cls.add_transition(key, value)

    def run(self):
        pass

    def add_state(self, identifier, state):
        pass

    def add_transition(self, identifier, transition):
        pass

    @property
    def current_state(self):
        # type: () -> State
        return self.states_map[self._current_state_value]

    @current_state.setter
    def current_state(self, value):
        pass
