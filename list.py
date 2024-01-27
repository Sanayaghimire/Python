names = ['danish', 'eru','roshan','kedar','binod']
print(names)
print("Hey "+names[0].title() + ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[1].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[2].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[3].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[-1].title()+ ", I would like to invite you to dinner tonight at mine.\n\n")
print("Unfortunately "+names[1].title()+" may not able to make it to our plan tonight.")



names[1]='Mandira'

print("Hey "+names[1].title()+ ", I would like to invite you to dinner tonight at mine.\n\n")

print("Hello everyone, I just found the bigger dinner table")
names.insert(0,'Ramesh')
names.insert(3, 'Sulav')
names.insert(7, 'Ram')
print(names)
print("\n")
print("Hey "+names[0].title() + ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[1].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[2].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[3].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[4].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[5].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[6].title()+ ", I would like to invite you to dinner tonight at mine.")
print("Hey "+names[-1].title()+ ", I would like to invite you to dinner tonight at mine.\n\n")


print("Sorry, I can invite only two person")
popped_names = names.pop()
print("I'm sorry "+popped_names+", I cannot invite you to dinner tonight.")
print(names)
popped_names = names.pop()
print("I'm sorry "+popped_names+", I cannot invite you to dinner tonight.")
print(names)
popped_names = names.pop()
print("I'm sorry "+popped_names+", I cannot invite you to dinner tonight.")
print(names)
popped_names = names.pop()
print("I'm sorry "+popped_names+", I cannot invite you to dinner tonight.")
print(names)
popped_names = names.pop()
print("I'm sorry "+popped_names+", I cannot invite you to dinner tonight.")
print(names)
popped_names = names.pop()
print("I'm sorry "+popped_names+", I cannot invite you to dinner tonight.")
print(names)

print("\n\n")

print(names[0].title()+", I would like to invite you to dinner tonight.")
print(names[1].title()+", I would like to invite you to dinner tonight.")


len(names)
print("The number of people I am inviting for dinner is "+str(len(names)))

del names[0]
print(names)


print("\n\n\n")


#organizing list
visit_places=['italy', 'bali', 'tomso', 'uppermustang', 'abc']
print(visit_places)

print(sorted(visit_places))

print(visit_places)

print(sorted(visit_places, reverse=True))

print(visit_places)
visit_places.reverse()
print(visit_places)

visit_places.reverse()
print(visit_places)

print("\n")

visit_places.sort()
print(visit_places)

visit_places.sort(reverse=True)
print(visit_places)

print("\n\n")
#working with list(looping)
pizzas=['chicken', 'mashroom', 'pepperoni']
for pizza in pizzas:
    print(pizza)
    print("I like "+pizza+" pizza so much.")
print("I really love pizza. \n\n")


animals=['dog','cat','rabbit']
for animal in animals:
    print(animal.title())
    print("A "+ animal.title()+" would make a great pet.")
print("These animals are domestic animals.\n\n\n")

for value in range(1,21):
    print(value)

print("\n\n")
#for value in range(1,1000001):
  #  print(value)
#print(max(range(1,1000001)))
# print(min(range(1,1000001)))
#print(sum(range(1,1000001)))


odd_numbers= list(range(1, 21, 2))
for value in odd_numbers:
    print(value)

print("\n\n")
multiples=[]
for value in range(3,31, 3):
   multiples.append(value)
print(multiples)
print("\n\n")


cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(cubes)
print("\n\n")


cubes=[value**3 for value in range(1,11)]
print(cubes)

print(("\n\n"))
#slicing through list

books=['alchemist','the theft book', '1964','the subconcious mind', 'things falls a part','invisible man']
print(books)
print("The first three items in the list are:" + str(books[:3]))
print("The middle items in the list are:"+str(books[2:5]))
print("The last items in the list are:"+str(books[-3:]))

print(("\n\n"))
my_pizza=['mushroom','pepperoni','chiken', 'cheese']
friend_pizza=pizzas[:]
print(pizzas)
print(friend_pizza)
print("\n")
my_pizza.append('onions')
for pizza in my_pizza:
    print("My favourite pizzas are: "+pizza)
print("\n\n")
friend_pizza.append('bacon')
for pizza in friend_pizza:
    print("My friend pizzas are: "+pizza)