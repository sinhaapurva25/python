##3
# def divide(x,y):  
#     print(x//y)  
# def outer_div(func):  
#     def inner(x,y):  
#         if(x<y):  
#             x,y = y,x  
#         return func(x,y)  
#     return inner  
# divide1 = outer_div(divide)  
# divide1(50,3)

# ##4_using @ function
# def outer_div(func):  
#     def inner(x,y):  
#         if(x<y):  
#            x,y = y,x  
#         return func(x,y)  
#     return inner  
# # syntax of generator  
# @outer_div  
# def divide(x,y):  
#      print(x//y)
# divide1 = outer_div(divide)  
# divide1(9.8,2.0)

# def do_twice(func):  
#     def wrapper_do_twice(name):  
#         func(name)  
#         func(name)  
#     return wrapper_do_twice

def do_twice(func):  
    def wrapper_function(*args):  
        func(*args)  
        # func(*args)  
    return wrapper_function