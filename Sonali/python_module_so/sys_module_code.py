import sys

#wanted to know which module is running currently. which python file is running now.
values = sys.argv #sys.argv is the mandet line
print(values)

#wanted to run the file in the terminal directly then right click on that file and open in terminal. make sure the correct file name is opened
#then run the comman python.\python file name

#python .\sys_module_code hello python
#output is ['C:\\AutomationCode\\GTM_PS_Batch09\\Sonali\\python_module_so\\sys_module_code.py']


print(sys.version)  # it will print python version

print(sys.version_info) #it will give full details of the python
print(sys.platform) # it will print platfor that is windows 32 or windows64