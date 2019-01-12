def _flatten_generator(nested_list):
    while nested_list:
        item = nested_list.pop(0)

        # Explicitly for test cases. Generic solution could check if
        # item is iterable and not str.
        if isinstance(item, (list, tuple)) and not isinstance(item, str):
            # firts convert tuple to list
            nested_list = list(item) + nested_list
        else:
            yield item


def flatten(iterable):
    """Flatten nested list."""
    return [i for i in _flatten_generator(iterable) if i is not None]
