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
    scores = {}

    for line in data:
        line = line.rstrip()
        words = line.split(":")

        scores[words[0]] = words[1]
        
    # # sorted_scores = sorted(scores)
    # for restaurant in sorted_scores:
    #     print(f"{restaurant} score is {scores[restaurant]}")
    print(scores.items())
    print(sorted(scores))
    
print(process_scores('scores.txt'))

print(f"{('lot', 'of', 'sheece',)[1]} llo")
# print_sorted_scores(score):
    
    