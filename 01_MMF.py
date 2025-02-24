# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, num_letters, valid_ans_list=('yes', 'no')):
    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def instructions():
    make_statement("Instructions", "🔎")

    print('''
    
For each ticket holder enter
- Their Name
- Their Age
- The Payment Method (Cash / Credit)

The program will record the ticket sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the exit code ('xxx'), the program will display the ticket 
sales information and write the data to a text file. 

It will also choose one lucky ticket holder who wins the draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def int_check(question):
    error = f"Oops - Please enter an integer more than zero "

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)


# Main Routine goes here

MAX_TICKETS = 5
tickets_sold = 0

payment_ans = ('cash', 'credit')

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ", 1)

if want_instructions == "yes":
    instructions()

while tickets_sold < MAX_TICKETS:
    print()
    name = not_blank("Name: ")

    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    elif age == "xxx":
        break
    else:
        pass

    pay_method = string_check("Payment method: ", 2, payment_ans)
    print(f"{name} has brought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
