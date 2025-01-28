from collections.abc import Iterable

class BirdbrainUtility:
    @classmethod
    def is_none_or_empty(self, s):
        if s is None or s == "":
            return True
        else:
            return False

    @classmethod
    def flatten_string(self, original_list, divider = "/"):
        original_list = [item for item in original_list]
        s = ""
        for element in list(original_list):
            if isinstance(element, str):
                s += str(element) + divider
            elif isinstance(element, int):
                s += str(element) + divider
            else:
                for sub_element in element:
                    s += str(sub_element) + divider

        return(s[:-1])
