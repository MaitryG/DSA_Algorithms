import copy
original = [[1,2],[3,4]]

shallow_copy = copy.copy(original)
shallow_copy[0][0] = 9
print(original)

deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 10
print(original)


def decorator_func(original_func):
    def wrapper_func():
        print("Hello :", original_func.__name__)
        return original_func()
    return wrapper_func()

@decorator_func
def display():
    print("Helo world")

display()