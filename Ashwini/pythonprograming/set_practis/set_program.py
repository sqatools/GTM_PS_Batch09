#Python program to create a set with some elements.
set={2,3,4,5}
print(set)
print("-"*50)
#Python program to add an element to a set.
set={2,3,5,6,8}
set.add(9)
print(set)
print("-"*50)
# Python program to remove an element from a set.
set={23,24,34,31,30}
set.remove(31)
print(set)
print("-"*50)

#Python program to find the length of a set.
a={2,3,4,5,10}
a_len=len(a)
print(a_len)
print("-"*50)
#Python program to check if an element is present in a set.
b={20,10,8,9,16}
if 10 in b:
    print("True")
else:
    print("False")
print("-"*50)
#Python program to find the union of two sets.
set_c={10,20,21,25,15,16}
set_d={34,17,16,27,31,21}
result=set_c.union(set_d)
print("result:",result)
print("-"*50)
#Python program to find the intersection of two sets.
set_e={10,12,21,25,17,16}
set_f={14,17,16,27,12,21}
result=set_e.intersection(set_f)
print(result)

print("-"*50)
#Python program to find the difference of two sets.
set_c={10,20,21,25,15,16}
set_d={34,17,16,27,31,21}
diff_val_c_to_d=set_c.difference(set_d)
print(diff_val_c_to_d)
diff_val_d_to_c=set_d.difference(set_c)
print(diff_val_d_to_c)
print("-"*50)
#Python program to find the symmetric difference of two sets.
set_g={10,20,30,15,25}
set_h={12,15,22,16,30}
r=set_g.symmetric_difference(set_h)
print(r)
#Python program to show if one set is a subset of another set.
# Python program to convert a list to a set.
list=[2,3,5,8,9]
result=frozenset(list)
print(result)
#Python program to convert a set to a list.
set_1={2,3,6,7,9}



print("-"*50)
# Python program to check if all elements in a set are even.
set={12,11,23,15,24,14}
count=0
for ele in set:
    if ele%2==0:
        count +=1
if count == len(set):
     print("All elements in the set are even")
else:
  print("All elements in the set are not even")
