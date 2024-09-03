def case_converter(class_name: str) -> str:
    """
    >>> case_converter("User")
    "users"
    >>> case_converter("UserProfile")
    "user_profiles"
    >>> case_converter("CUserProfile")
    "c_user_profiles"
    >>> case_converter("Cherry")
    "cherries"
    >>> case_converter("SOMESdk")
    "some_sdks"
    """
    changed_class_name = ""
    if class_name[-1] == "y":
        changed_class_name = class_name[:-1] + "ies"
    elif class_name[-1] == "s":
        changed_class_name += class_name + "es"
    else:
        changed_class_name = class_name + "s"

    chars = []

    for c_idx, char in enumerate(changed_class_name):
        if c_idx and char.isupper():
            nxt_idx = c_idx + 1
            flag = nxt_idx >= len(class_name) or class_name[nxt_idx].isupper()
            prev_char = class_name[c_idx - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)
