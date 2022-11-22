import time

RED = "\033[91m"
WHITE = "\033[0m"


def benchmark(func):
    """
    Decorador que te mide el tiempo que tarda la funcion en ejecutarse.
    Se puede usar como cualquier funcion, e.g. benchmark(func),
    pero al ser un decorador la gracia que tiene es que al hacer
    @benchmark
    def func():...
    cada vez que uses func() estaras usando benchmark(func)()
    :param func: la funcion que quieres testear
    :return: la funcion original envuelta por el codigo de testeo
    """
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Time taken for {RED}{func.__name__}{WHITE}: {end - start:.4f}')
        return result

    return inner


def remove_punctuation(text):

    """
    Removes the characters:
    !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789
    from the text.
    """

    chars_to_remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

    tr = str.maketrans("", "", chars_to_remove)

    return text.translate(tr)
