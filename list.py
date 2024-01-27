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
print("These animals are domestic animals.")

