def get_max(a, b):
    return a if a > b else b

def get_max_without_arguments():
    raise TypeError('missed argument')


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    maximum = float('inf')
    for a in args:
    	if a > maximum:
    		maximum = a
    return maximum

def get_max_with_one_or_more_arguments(first, *args):
    maximum = float('inf')
    for a 


def get_max_bounded(*args, low, high):
    pass


def make_max(*, low, high):
    def inner(first, *args):
        pass

    return inner
