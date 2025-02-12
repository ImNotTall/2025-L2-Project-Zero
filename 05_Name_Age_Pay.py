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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main Routine goes here

payment_ans = ('cash', 'credit')

while True:
    print()

    name = not_blank("Name: ")

    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

pay_method = string_check("Payment method: ", payment_ans, 2)
print(f"{name} has brought a ticket ({pay_method}")
