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
package with exception
"""


class StateMachineError(Exception):
    """Base exception for this project, all exceptions that can be raised inherit from this class"""

class InvalidParentState(Exception):
    """todo"""
