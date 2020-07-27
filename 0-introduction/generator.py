def setVariables():
    a = 1
    yield a
    
    a = 2
    yield a
    
    a = 3
    yield a
    
    a = 4
    yield a

my_first_gen = setVariables()

print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))
