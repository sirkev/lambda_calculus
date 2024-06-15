# This is a sample Python script exploring lambda calculus concepts in programming


def get_sum(num1, num2):
    total = num1 + num2
    print(f'sum:, {total}')


def l_sum(num1, num2):
    total = (lambda x: lambda y: x + y)(num1)(num2)
    print(f'sum using lambda:, {total}')


if __name__ == '__main__':
    get_sum(1, 2)
    l_sum(1, 2)
