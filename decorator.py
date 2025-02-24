# chnage the internal workinf without change the code.
# Special type of higher order function that can take function an argument it alse return function (where we change the behaviour).

# Syn:-
        # def outer(fun.)
                #def inner_fun(parameters)
                  #modification
        #return inner_fun
        # def fun1(argument)
        # 
        # res=outer-fun(fun1)

def outer_fun(fun1):
    def inner_fun():
        print("Before modifi :")
        fun1()
        print("After modifi")
    return inner_fun

@outer_fun
def fun():
    print("this if friom main")
    # res=outer_fun
    # fun()
fun()
