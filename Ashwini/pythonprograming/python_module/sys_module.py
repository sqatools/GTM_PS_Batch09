import sys

# read parameter from command line using sys.
elem_arg = sys.argv
# argv : arguments
print(elem_arg)

# ['.\\sys_module.py', 'Hello', 'good', 'Morning', 'sonali', 'monali']
#get current python version information
print(sys.version_info)#sys.version_info(major=3, minor=13, micro=2, releaselevel='final', serial=0)
print(sys.version) #3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]

#get current platfrom details
print(sys.platform) #win32