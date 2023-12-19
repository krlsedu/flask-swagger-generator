class Utils:

    @staticmethod
    def is_list(typ):
        if hasattr(typ, '__origin__') and typ.__origin__ is list:
            return True
        elif typ is list or isinstance(typ, list):
            return True
        return False
