def plus(a, b):
    return (int(a)+int(b))


def minus(a, b):
    return (int(a)-int(b))


def multiple(a, b):
    return (int(a)*int(b))


def divide(a, b):
    return (int(a)/int(b))


def downgrade(a, b):
    return (int(a)//int(b))


def left(a, b):
    return (int(a) % int(b))


print(plus("20", 5))
print(minus("20", 5))
print(multiple("20", 5))
print(divide("20", 5))
print(downgrade("20", 5))
print(left("20", 5))
