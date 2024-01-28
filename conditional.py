car = 'audi'


print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict True.")
print(car == 'audi')


print("\nIs car == 'honda'? I predict False.")
print(car == 'honda')


print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

print("\nIs car !='toyota' and car! ='honda'? I predict True")
print(car!='toyota' and car!='honda')
print("\n Is car=='audi' and car=='honda'? I predict False")
print(car=='audi' and car=='honda')

print("\n Is car=='audi' or car=='honda'? I predict True")
print(car=='audi'or car=='honda')

print("\n Is car =='toyata' or car=='honda'? I predict False")
print(car=='toyota' or car=='honda')

print("\n\n\n")
added_car='BMW'


print(added_car=='audi')
print(added_car=='BMW')

print(added_car.lower()=='bmw')
if added_car!='honda':
    print("\nThe honda is out of service\n\n")
else:
    print( "\nWelcome "+added_car +" to pur service.\n\n")



number=21
number2=13
print(number==21)
print(number!=21)
print(number<=21)
print(number>=22)
print(number<=21 and number2>=10)
print(number==21 or number2<=20)
print(number==21 and number2>=20)

print("\n\n")
numbers=['1', '2','3','4','8']
num='2'
print(num in numbers)
num='9'
print(num not in numbers)