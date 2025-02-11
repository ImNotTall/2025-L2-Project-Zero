def int_check(question):

    error = "Oops - Please enter an integer"

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)


while True:
    print()

    name = input("Name: ").strip()

    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")