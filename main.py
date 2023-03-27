def memoize(max_size=100):
    dictionary = {}

    def decorator(func):

        def inner(*args):
            if args in dictionary:
                return dictionary[args]
            result = func(*args)
            if len(dictionary) >= max_size:
                dictionary.popitem()
            dictionary[args] = result
            return result

        return inner

    return decorator


@memoize(max_size=100)
def my_func(x):
    return x ** 2
