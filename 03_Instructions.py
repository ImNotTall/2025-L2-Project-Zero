# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[0]:
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


# Main Routine goes here

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions")

if want_instructions == "yes":
    instructions()

print()
print("Program Continues...")
