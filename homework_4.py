immutable_var = 1,2,3,True
print(immutable_var)
immutable_var[0]=5
print(immutable_var) #кортеж относится к неизменяемым коллекциям
mutable_list = [1,2,3,4,5]
mutable_list[0]=9
print(mutable_list)
