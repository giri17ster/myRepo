def decorated_function(f):
    def child_decorated_function(a,b):
        print("Value of the first param : ", a)
        print("Value of the second param : ", b)
        print("function name - ", f.__name__)
        x = f(a,b)
        print("Result = ",x)
        print("function name - ", f.__name__)
    return child_decorated_function;

#parent_function = decorated_function(parent_function)
@decorated_function
def parent_function(a,b):
    return a+b

parent_function(2,3)