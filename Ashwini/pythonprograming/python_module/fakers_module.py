from faker import Faker
fk=Faker()
for i in range(10):
    first_name=fk.first_name()
    last_name=fk.last_name()
    address=fk.address()
    email=fk.email()
    phone_number=fk.phone_number()
    city=fk.city()
    print("firstname :", first_name, "\nlast_name :", last_name, "\naddress:", address, "\nemail:", email, "\nphone_number:",
          phone_number,"\ncity:",city)
    print("_" * 50)
