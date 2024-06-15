# This is a sample Python script exploring lambda calculus concepts in programming


def get_sum(num1, num2):
    total = num1 + num2
    print(f'sum:, {total}')

#here, we make use of higher order funtions which enable us to take in functions as inputs and also return functions as outputs
def l_sum(num1, num2):
    #curring: this is a way of supporting multiple function inputs
    #this done by having a function return another function sequentially performing a beta reduction for each of the inputs
    total = (lambda x: lambda y: x + y)(num1)(num2)

    print(f'sum using lambda:, {total}')



#booleans and conditionals
def if_then(b,x,y):
    if b:
        return x
    else:
        return y
def l_bool(value):
    true = (lambda x : lambda y: x)
    false = (lambda x : lambda y: y)




if __name__ == '__main__':
    get_sum(1, 2)
    l_sum(1, 2)
