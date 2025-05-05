# install faker module with below command
# pip install faker

from faker import Faker

fk = Faker()
print(dir(fk))
for i in range(10):
    first_name = fk.first_name()
    last_name = fk.last_name()
    address = fk.address()
    email = fk.email()
    phone = fk.phone_number()
    print("firstname :", first_name,"\nlast_name :",last_name,"\naddress:", address,"\nemail:", email,"\nphone:", phone)
    print("_"*50)

