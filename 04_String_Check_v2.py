def string_check(question, valid_ans_list, num_letters):
    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("Do you like coffee? ", yes_no_list, 1)
print(f"You chose {like_coffee}")
pay_method = string_check("Payment method: ", payment_list, 2)
print(f"You chose {pay_method}")