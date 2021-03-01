import imdb

ia = imdb.IMDb()

def findCompany(movie): # Find the companies that produce the given movie
    # getting the movie name
    movieName = movie['title']

    # get the list of companies of the movie 
    companies = movie.data['production companies']

    if len(companies) == 0:
        print("IMDBot: There is no production company for this movie")
        return
    else:
        print("IMDBot: The production company is: " + companies[0]['name'])

    return companies[0] # return the main company of the movie production

    


