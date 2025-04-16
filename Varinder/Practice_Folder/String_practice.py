#without idexing

# pet = "dog"
# for p in pet:
#     print(p)

##########################
# with indexing#

# fruit = "Apple"
# fruit_len = len(fruit)
# for f in range(fruit_len):
#     print(f,fruit[f])
####################################################
name = "Harveer"
age = 13
city = "Ashburn"

person_identity = "He is " +name+" His age is "+str(age)+" and he lives in "+city
print(person_identity)

person_identity2 = "He is {} His age is {} and he lives in {}".format(name,age,city)
print(person_identity2)

person_identity3 = f"He is {name}, his age {age} and he lives in {city}"
print(person_identity3)


