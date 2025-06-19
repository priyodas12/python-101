# prints args as tuple
def var_argument_func(*args):
    print(args)

var_argument_func(1,2,3,)
var_argument_func(1,2,3,5)

def mixed_argument_func(a,b,*args):
    print(a,b,args)

mixed_argument_func(True,7.903,6,'y',9.99)


def mix_argument_special_func(*args,a,b):
    print(a,b,args)

# keyword argument followed by args
mix_argument_special_func(12,22,32,a=90,b=89)