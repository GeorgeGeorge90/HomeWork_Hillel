


def two_point(arg1, arg2):
    if isinstance(arg1, int) and isinstance(arg2, int):
        return int(arg1) - int(arg2)
    elif isinstance(arg1, float) and isinstance(arg2, float):
        return float(arg1) - float(arg2)
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return f'{str(arg1)} {str(arg2)}'  # f-string for concatenation
    elif isinstance(arg1, str) and not isinstance(arg2, str):
        return {arg1: arg2}
    else:
        return arg1, arg2



print(two_point('a', 2))

