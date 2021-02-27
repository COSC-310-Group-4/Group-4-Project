import imdb

ia = imdb.IMDb()

def findCompany(movie): # Find the companies that produce the given movie
    # lookup for movie and get the movie id
    moviesId = movie.movieID 

    # getting information of the movie
    movie = ia.get_movie(moviesId)

    # getting the movie name
    movieName = str(movie)

    # get the list of companies of the movie 
    companies = movie.data['production companies']

    if len(companies) == 0:
        print("IMDBot: There is no production company for this movie")
    else:
        print("IMDBot: The production companies for the movie " + movieName + " are:")

        # print the companies
        for company in companies:
            print(company['name'])


    return companies # return the set of companies
