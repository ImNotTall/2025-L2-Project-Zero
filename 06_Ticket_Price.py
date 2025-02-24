def int_check(question):
    error = f"Oops - Please enter an integer more than zero "

    while True:

        try:
            response = int(input(question))
            return response

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

CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

CREDIT_SURCHARGE = 0.05

while True:
    print()

    name = not_blank("Name: ")

    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue

    elif 12 <= age < 65:
        ticket_price = CHILD_PRICE

    elif 65 <= age < 121:
        ticket_price = SENIOR_PRICE
        print(f"{name} is too old")
        continue
    elif age == "xxx":
        break
    else:
        pass

    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"the total payable is ${total_to_pay:.2f}\n")


