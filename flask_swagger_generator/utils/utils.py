import re
from importlib import import_module


class Utils:

    @staticmethod
    def is_list(typ):
        if hasattr(typ, '__origin__') and typ.__origin__ is list:
            return True
        elif typ is list or isinstance(typ, list):
            return True
        return False

    @staticmethod
    def extract_inner_type(typ):
        match = re.search(r'\[(.*?)\]', str(typ))
        return match.group(1) if match else None

    @staticmethod
    def get_class_by_type(typ):
        fully_qualified_classname = Utils.extract_inner_type(typ)
        if fully_qualified_classname is None or fully_qualified_classname == '~T':
            return None
        if '.' not in fully_qualified_classname:
            return eval(fully_qualified_classname)
        module_name, class_name = fully_qualified_classname.rsplit(".", 1)
        module = import_module(module_name)
        cls = getattr(module, class_name)
        return cls
