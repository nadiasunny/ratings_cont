"""Restaurant rating lister."""
#create function
    #create empty dictionary
    #open file
    #loop over line files
        #stripe whitespace from right
        # split on ":"
        #Ramen On Empty:3 --> ['Ramen On Empty', 3]
        #dict[line[0]] = line[1]
    # use sorted() to sort into alphabetical order
    # use .items
    # print restaurant is rated at ratings

def process_scores(filename):

    data = open(filename)

    user_restaurant = input('What restaurant are you rating? ')
    user_rating = input(f'What is your rating for {user_restaurant}: ')

    while int(user_rating) > 5 or int(user_rating) < 1:
        user_rating = input('Your rating must be between 1-5: ')

    scores = {user_restaurant: user_rating}
    for line in data:
        line = line.rstrip()
        words = line.split(":")

        scores[words[0]] = words[1]
        
    # # sorted_scores = sorted(scores)
    # for restaurant in sorted_scores:
    #     print(f"{restaurant} score is {scores[restaurant]}")
    for res, rating in sorted(scores.items()):
        print(f"{res}'s is rated at {rating}.")

process_scores('scores.txt')
    
    