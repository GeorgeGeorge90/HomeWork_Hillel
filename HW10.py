str1 = "example"
list1 = ["example2", 234, [2]]


def foo(arg):
    return arg*2


def targetfunction(randomlist, funcobject):
    return [funcobject(i) for i in randomlist]


print(targetfunction(str1, foo))
print(targetfunction(list1, foo))

