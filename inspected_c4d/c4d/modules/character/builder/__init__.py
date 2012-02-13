# Functions --------------------------------------------------

def AddIncludeObject(*args, **kwargs):
    """
    [incdata,op,flags] : Add object to include container.
    """
    pass

def FindIncludeObject(*args, **kwargs):
    """
    [incdata,name] : Find object in include container.
    """
    pass

def GetComponentFlags(*args, **kwargs):
    """
    [bl] : Get component flags from an object/tag.
    """
    pass

def RemoveIncludeObject(*args, **kwargs):
    """
    [incdata,name] : Remove object from include container.
    """
    pass
# Classes ----------------------------------------------------
'''
CharacterObject
Component
ComponentObject
Template
'''
# Constants --------------------------------------------------
COMPONENT_INSERT_TYPE_ACTIVE = 4
COMPONENT_INSERT_TYPE_AFTER = 3
COMPONENT_INSERT_TYPE_BEFORE = 2
COMPONENT_INSERT_TYPE_END = 5
COMPONENT_INSERT_TYPE_FIRST = 0
COMPONENT_INSERT_TYPE_LAST = 1
COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL = 1
COMPONENT_OBJECT_GETOBJECTS_TYPE_INCLUDED = 2
COMPONENT_OBJECT_GETOBJECTS_TYPE_MAIN = 3
# Everything else --------------------------------------------
__doc__ = 'Character Builder'
__name__ = 'c4d.modules.character.builder'
__package__ = None