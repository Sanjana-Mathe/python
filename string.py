login_id = input("create your login ID: ")
password = input("create your password: ")
print("Go to back")
entered_id = input("please enter your login ID: ")

if entered_id != login_id:
    print("wrong login ID")
else:
    enter_pass = input("enter your password: ")
    if enter_pass != password:
        print("wrong password")
    else:
        print("Account created successful!")