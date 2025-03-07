# def double_dacker(work):
#     print('This is First Line of The code')
#     work()
#     # return work*2


# def soCalled():
#     print('Hi')

# double_dacker(soCalled)

# 
def double_fun(woek=2):
    print('This a outer function')
    print('This is woek',woek)
    def innnerFunction(x):
        print('Inside the function')
    return innnerFunction


# print(double_fun(4)())
obj = double_fun()(3)
