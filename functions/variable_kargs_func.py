# variable length keyword arguments
# prints as dictionary
def var_length_keyword_args_func(**kwargs):
    print(kwargs)
    for item in kwargs.items():
        print(item)

var_length_keyword_args_func(a=67,g=10,k=10)

#SyntaxError: arguments cannot follow var-keyword argument

#def var_length_keyword_args_func_special(**kwargs,x,b):
#    print(kwargs)

def var_length_keyword_args_func_special(x,y,**kwargs):
    print(x,y,kwargs)

var_length_keyword_args_func_special(1,2,a=90,b=23)

#special cases
def mixed_args_func_special(*args,x,y,**kwargs):
    print(args,x,y,kwargs)

mixed_args_func_special(1,2,3,5,6,x=10,y=90,z=92)
#(1, 2, 3, 5, 6) 10 90 {'z': 92}