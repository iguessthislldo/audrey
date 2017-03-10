def is_not_saved(obj):
    return obj._state.adding

def is_saved(obj):
    return not obj._state.adding

class Object_Not_Saved_Error(Exception):
    def __init__(self, obj):
        self.message = (
            "An object: \"{}\" needs to be saved before the program can"
            "continue"
        ).format(repr(obj))

def assume_saved(obj):
    if obj._state.adding:
        raise Object_Not_Saved_Error(obj)
    
    
