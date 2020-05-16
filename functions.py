def cython_obj_to_dict(obj: object) -> dict:
    keys = dir(obj)
    keys = filter(lambda k: k[0] != "_", keys)
    data = [(k, getattr(obj, k, None)) for k in keys]
    data = [(k, v) for k, v in data if not callable(v)]
    data = dict(data)
    return data


def display_obj_values(obj: object):
    from tabulate import tabulate

    data = cython_obj_to_dict(obj)
    print(tabulate(data.items()))
