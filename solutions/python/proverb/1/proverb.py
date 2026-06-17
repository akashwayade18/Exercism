def proverb(*items, qualifier=None):
    if not items:
        return []
    lines = []
    # Using zip and list slicing to pair consecutive items:
    # items[:-1] gets all items except the last one
    # items[1:] gets all items except the first one
    for cause, consequence in zip(items[:-1], items[1:]):
        lines.append(f"For want of a {cause} the {consequence} was lost.")  
    # Using unpacking implicitly by referencing the very first item
    qualifier_str = f"{qualifier} " if qualifier else ""
    first_item = items[0]
    lines.append(f"And all for the want of a {qualifier_str}{first_item}.")
    return lines