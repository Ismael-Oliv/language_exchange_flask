class Transaction_decorator(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Call method excuted this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@Transaction_decorator
def display():
    print("Display function ran")


display()
