def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name':'Sanamdeep Singh',  
        'student_id':10333491,
        'pizza_toppings':[
            'cheese',
            'peporoni',
            'lamb',
            'capcicum'
        ],
        'movies':[
            {
            'the killer':'action'
            },
            {
            'fly me to the moon':'funny'
            },
            {
            'unstoppable':'drama'
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    another_movie ={
        'smile':'horror'
    }
    about_me['movies'].append(another_movie)
    print(about_me) # Temporary debug print
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    print(f"My name is {full_name}, but you can call me sir {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted([topping.lower() for topping in about_me['pizza_toppings']])
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()