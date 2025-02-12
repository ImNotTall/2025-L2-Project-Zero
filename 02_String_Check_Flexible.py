def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


payment_ans = ('cash', 'credit')

while True:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()
