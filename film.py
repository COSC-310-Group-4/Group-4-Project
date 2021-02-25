import imdb

ia = imdb.IMDb() # Initializes the IMDb integration through an IMDbPy method

def findMovie(userName): # Finds the movie requested by the user
    print('IMDBot: Sure thing! Which movie would you like to know about?')
    search = input(userName + ': ').lower()
    print('IMDBot: Hmmm let me remember...') # Serves to provide a buffer while the query is sent
    movie = ia.get_movie(ia.search_movie(search)[0].movieID) # gets the movieID through a search, then creates an object for the movie from the IMDbPy classes
    print('IMDBot: Ok! What do you want to know about '+ movie['title'] +'?') # confirms the movie, if it is incorrect, the user must ask about the movie again but in more specific terms (can happen with sequels/reboots)    
    return movie # returns movie object
    
def findDirector(movie):
    dirList = ''
    if (len(movie['directors']) == 1): 
        print('The director of ' + movie['title'] + ' is ' + movie['directors']['name']) # outputs this if the movie has only one director
    else:
        c = 1
        for director in movie['directors']: #loops in order to ensure multiple directors are listed properly (Try asking for "The Matrix" directors)
            if (c < len(movie['directors'])):
                dirList += director['name'] + ', '
            else: 
                dirList += 'and ' + director['name']
            c += 1
        print('The directors of ' + movie['title'] + ' are ' + dirList)
    return movie['directors'][0] # returns a person object in case of follow up questions (can only return one director properly or other functions might not work)
        
