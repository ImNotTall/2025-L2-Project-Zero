import pandas
import random


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


def currency(x):
    return "${:.2f}".format(x)


# Main Routine goes here

MAX_TICKETS = 5
tickets_sold = 0

payment_ans = ('cash', 'credit')

CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

CREDIT_SURCHARGE = 0.05

all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

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
        print(f"{name} is too young")
        continue

    elif age < 16:
        ticket_price = CHILD_PRICE

    elif age < 65:
        ticket_price = ADULT_PRICE

    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    pay_method = string_check("Payment method: ", 2, payment_ans)

    if pay_method == "cash":
        surcharge = 0

    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

winner = random.choice(all_names)

winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index)

ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print(mini_movie_frame.to_string(index=False))

# print(mini_movie_frame)
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

print(f"The lucky winner is {winner}. Their ticket worth {ticket_won} is free!")
print(f"Total Paid is now ${total_paid - ticket_won:.2f}")
print(f"Total Profit is now ${total_profit - profit_won:.2f}")

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
