import sys

# read parameter from command line using sys.
elem_arg = sys.argv
# argv : arguments
print(elem_arg) #

# command to provide param values with python file execution.

#  python .\sys_module.py hello Python Programming Rammez  Sonali Arti
# ['.\\sys_module.py', 'hello', 'Python', 'Programming']
# ['.\\sys_module.py', 'hello', 'Python', 'Programming', 'Rammez', 'Sonali', 'Arti']


# get current python version information
print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)

print(sys.version)
# 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]


# get current platform details
print(sys.platform) # win32

