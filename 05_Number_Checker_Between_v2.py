def int_check(question, low, high):

    error = f"Oops - Please enter an integer more than zero {low} and {high}"

    while True:

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


while True:
    print()

    my_num = int_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")
