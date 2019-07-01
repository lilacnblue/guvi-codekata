correct_password = "123"
name =input("enter name:")
surname =input("enter surname:")
password =input("enter password:")

while correct_password !=password:
    password =input("wrong password! enter again:")

message ="hi %s %s,you are logged in " %(name,surname)
print(message)
