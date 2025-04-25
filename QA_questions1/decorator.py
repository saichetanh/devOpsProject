
def hi(f):
    def wrapper():
        print("calling function" , {f.__name__})
        f()
        print("after calling", {f.__name__})
    return wrapper
@hi
def helloFunction():
    print ("hello")

helloFunction()


# hiThereDecorator = hi(helloFunction)
# # print(hi)
# hiThereDecorator()


# def log_function_call(fn):
#     def wrapper():
#         print(f"Calling function: {fn.__name__}")
#         fn()  # Call the original function
#     return wrapper
#
# def say_hello():
#     print("Hello!")
#
# logged_hello = log_function_call(say_hello)  # Manually wrap the function
# logged_hello()
