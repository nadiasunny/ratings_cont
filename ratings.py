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
        
    print(scores)

process_scores('scores.txt')

