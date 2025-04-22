"""
->  set is mutable data type
->  set can contain only immutable data type, int, float, string, tuple, boolean.
->  set contain unique values, duplicate values are not allowed
->  set does not follow index, it stores the values in random order.
"""

set1 = {3, 3.5, 'Hello', (4, 6, 7), True, None}
print(set1, type(set1))

# {None, True, 3.5, 3, (4, 6, 7), 'Hello'} <class 'set'>

#set2 = {3, 3.5, 'Hello', (4, 6, 7), True, None, [3, 6, 8]}
#print(set2)
# TypeError: unhashable type: 'list'

print("_"*50)
############################################
# Apply loop on set data type :

set3 = {3, 3.5, 'Hello', (4, 6, 7), True, None}
for val in set3:
    print(val)
"""
None
True
3.5
3
Hello
(4, 6, 7)

"""

print("_"*50)
#################### Set Methods ##########################
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
'intersection', 'intersection_update', 'isdisjoint', 'issubset',
'issuperset', 'pop', 'remove', 'symmetric_difference',
'symmetric_difference_update', 'union', 'update'
"""



print("_"*50)
#################### Method to add data to set ###########
# Add method :  This method add to the set, at random place.

set4 = {3, 3.5, 'Hello', (4, 6, 7), True, None}
set4.add(100)
# add existing value
set4.add(True)

print("set4 :", set4)
# set4 : {None, True, 3.5, 3, 'Hello', 100, (4, 6, 7)}



print("_"*50)
####################
# update() method : Update method helps to updated one set data to another set.
set_a = {'a', 'b', 'c'}
set_b = {44, 66, 88}

set_b.update(set_a)
print("set_b :", set_b)
# set_b : {'a', 66, 88, 'c', 44, 'b'}

print("_"*50)
####################
# union() method :  This method combine 2 sets values and create new set, does not update original
#                   set values

set_c = {'a', 'b', 'c', 'f'}
set_d = {44, 66, 88, 100}

result = set_c.union(set_d)
print("result :", result)
# {66, 'c', 100, 'a', 44, 88, 'f', 'b'}

print("set_c :", set_c) # {'b', 'c', 'a', 'f'}
print("set_d :", set_d) # {88, 66, 100, 44}


print("_"*50)
#################### Remove data from set #################
# remove method :  This method will remove specific value from set, and does not return anything.
#                 ->  If value does not exist, then remove method will throw error. e.g. Keyerror.
set_e =  {66, 'c', 100, 'a', 44, 88, 'f', 'b'}
set_e.remove(100)
set_e.remove(88)

print("set_e :", set_e) # {66, 'c', 'a', 44, 'f', 'b'}

# remove non existing value
# set_e.remove(200) # KeyError: 200

print("_"*50)
####################
# discard() method: This method remove any specific values from given set if it is available.
#                   ->  If values does not exist, then it will not throw error.


set_f = {4, 6, 8, 25, 7, 22, 56}

# discard existing value
set_f.discard(25)
print("set_f :", set_f)

# discard non existing value
set_f.discard(100)
print("set_f :", set_f) # does not throw error.


print("_"*50)
####################
# pop() method : This method remove any value from set and return it.

set_g = {40, 16, 8, 25, 7, 22, 56, 200}
val = set_g.pop()
print("removed value :", val)
print("set_g :", set_g)
# set_g : {40, 8, 200, 16, 22, 56, 25}


print("_"*50)
####################
# clear() method  :  This method clear all the data from set.
set_h = {40, 16, 8, 25, 7, 22, 56, 200}
set_h.clear()
print("set_h :", set_h)
# set_h : set()

print("_"*50)
####################
# del keyword :  delete the set variable from memory
set_i = {40, 16, 8, 25, 7, 22, 56, 200}
del set_i
#print("set_i :", set_i)
# NameError: name 'set_i' is not defined


print("_"*50)
####################
# intersection() method :  This method helps to find the common values between 2 sets.

set_j = {6, 7, 8, 2, 44}
set_k = {22, 55, 77, 88, 7, 8, 6}

common_values = set_j.intersection(set_k)
print("common values :", common_values)
# common values : {8, 6, 7}

# intersection_update() method : This method find the common values between two sets and update
#                          the target with common values

set_j.intersection_update(set_k)

print("set_j :", set_j) # {8, 6, 7}
print("set_k :", set_k) # {55, 6, 7, 8, 22, 88, 77}

print("_"*50)
####################
# difference() method :  This method help you find the difference value
#  from one set to another.


set_l = {6, 7, 8, 2, 44, 11}
set_m = {22, 55, 77, 88, 7, 8, 6}

diff_val_l_to_m = set_l.difference(set_m)
print("diff from set l to M:", diff_val_l_to_m) # {2, 11, 44}

diff_val_m_to_l = set_m.difference(set_l)
print("diff from set M to L:", diff_val_m_to_l) # {88, 77, 22, 55}


# difference_update method : This method help you find the difference values
# from target set and update the target with difference values

set_l.difference_update(set_m)
print("set_l :", set_l) # {2, 11, 44}
print("set_m :", set_m) # {55, 6, 7, 8, 22, 88, 77}



print("_"*50)
####################
# symmetric_difference() method:  This method find the difference values
# from both sets.

set_p = {6, 7, 8, 2, 44, 11}
set_q = {22, 55, 77, 88, 7, 8, 6}

symm_diff = set_p.symmetric_difference(set_q)
print("symmetric diff :", symm_diff) # {2, 11, 44, 77, 22, 55, 88}
print("set_p :", set_p) # {2, 6, 7, 8, 11, 44}
print("set_p :", set_q) # {55, 6, 7, 8, 22, 88, 77}


#symmetric_difference_update() method : This method get difference value from both
# sets and update result in any of the target set.

set_p.symmetric_difference_update(set_q)
print("set_p :", set_p)  # {2, 11, 44, 77, 22, 55, 88}
