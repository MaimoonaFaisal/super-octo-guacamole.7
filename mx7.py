age = int(input("please enter your age: "))
salary = int(input("enter your monthly salary:"))

if age >= 18:
    print("age requirement met")
    if salary >= 30000:
        print("salary requirement met")
        print("loan approved")

    else:
        print("salary too low")
        print("loan rejected!")

else:
    print("age requirement not met")
    print("age requirement met")