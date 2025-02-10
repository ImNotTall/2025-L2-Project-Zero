def string_check(question, valid_ans_list):
    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


levels = ['easy', 'medium', 'hard']

like_coffee = string_check("Do you like coffee? ", ['yes', 'no'])
choose_level = string_check("Choose a level: ", levels)
