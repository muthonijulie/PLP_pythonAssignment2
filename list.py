my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(1,15)
print(my_list)

an_list=[50,60,70]
my_list.extend(an_list)
print(my_list)

my_list.pop(-1)
print(my_list)

my_list.sort()
print(my_list)

l=my_list.index(30)
print(l)
