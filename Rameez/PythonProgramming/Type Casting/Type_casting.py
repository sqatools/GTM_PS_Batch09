## Integer ##

# Int to Float #

a=10
b=float(a)
print(b, type(b))

# Int to String #
a=20
b=str(a)
print(b,type(b))

"""
## Int to List ##
a=30
b=list(a)
print(b,type(b))
#Not possible#
"""
# Int to tuple #
#Conersion is not possible#

#Int to Dict#
#Conversion is not possible#

#Int to set#
#Conversion is possible#

# Int to Bool#
a=40
b=bool(a)
print(b, type(b))

c=0
d=bool(c)
print(d, type(d))

## Float ##

# Float to Int #
a= 20.600000
b=int(a)
print(b,type(b))

#Float to String#
a=458.987656789
b=str(a)
print(b,type(b))

#Float to List#
#Conversion is not possible#

#Float to Dict#
#Conversion is not possible#

#Float to Set#
#Conversion is not possible#

#Float to bool#
a=9876787.98767876787687
b=bool(a)
print(b,type(b))


## String ##

# String to int #
a="123"
b=int(a)
print(b,type(b))
print(b**3)

""""
c="Hello"
d=int(c)
print(d,type(d))
"""
#String to Float#
a="45.678"
b=float(a)
print(b,type(b))

#String to List#
a="Hello"
b=list(a)
print(b, type(b))

#String to Tuple#
a="Python"
b=tuple(a)
print(b, type(b))

#String to Dict#
# Direct conversion is not possible#
"""
a= "van"
b=dict(a)
print(b,type(b))
"""
#If string follows the Dict format and the values are defined in jason key value
# format then we convert into dictionary with the help of jason module
import json
a='{"a":100, "b":200, "c":300}'
data= json.loads(a)
print(data,type(data))
print(data['c'])

#String to Set#
a="Python Programming"
b=set(a)
print(b,type(b))

#String to Bool#
a="Rameez"
b=bool(a)
print(b, type(b))

## Boolean ##

# bool to int #
a=True
b=int(a)
print(b,type(b))

# Bool to Float#
a=False
b=float(a)
print(b,type(b))

#Bool String#

a=False
b=str(a)
print(b,type(b))

#Bool to List#
#Conversion is not possible#

#Bool to Tuple#
#Conversion is not possible#

#Bool to Dict#
#Conversion is not possible#

#Bool to Set#
# Conversion is not possible#

## Set ##

# Set to Int #
# Conversion is not possible#

# Set to Float #
# Conversion is not possible#

# Set to String#
a={1,2,3,4,5,"5","ra","m"}
b=str(a)
print(b,type(b))

# Set to tuple #
a={1,2,3,4,5,"5","ra","m"}
b=tuple(a)
print(b,type(b))

#set to Dict#
# Conversion is not possible#

#Set to Boolean#
a={1,2,3,4,5,"5","ra","m"}
b=bool(a)
print(b,type(b))

## Dictionary ##

# Dict to Int #
# Conversion is not possible #

# Dict to float #
# Conversion is not possible #

# Dict to String #

a={"a":100, "b":200, "c":300}
b=str(a)
print(b,type(b))

# Dict to List #
a={"a":100, "b":200, "c":300}
b=list(a)
print(b,type(b))

# Dict to Tuple #

a={"a":100, "b":200, "c":300}
b=tuple(a)
print(b,type(b))

# Dict to Set #
a={"a":100, "b":200, "c":300}
b=set(a)
print(b,type(b))

# Dict to Boolean #
a={"a":100, "b":200, "c":300}
b=bool(a)
print(b,type(b))

## Tuple ##

# Tuple to Int #
# conversion is not possible #

# Tuple to Float #
#Conversion is not possible #

# Tuple to String #
a=(2,4,7,8,"v")
b=str(a)
print(b,type(b))

# Tuple to List #

a=(2,4,7,8,"v")
b=list(a)
print(b,type(b))

# Tuple to set #
a=(2,4,7,8,"v")
b=set(a)
print(b,type(b))

# Tuple to Dictionary #
# Conversion is not possible #
# But if we have two tuple variables i.e., One variable having keys and another
#variable is having values, we can convert tuple into Dictionary by using zip function.
w=("a","b","c")
e=(123,456,789)
result=dict(zip(w,e))
print(result,type(result))

# Tuple to Boolean #
a=(2,4,7,8,"v")
b=bool(a)
print(b,type(b))

