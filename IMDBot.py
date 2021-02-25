import film as f
import person as p
import company as c

print('IMDBot: Hello There! My name is IMDBot. What is yours?')
userName = input()
print('IMDBot: I am happy to be of service ' + userName + ', how can I help you today?')

while True:
    try:
        user_input = input(userName + ': ').lower() #collect user input for this iteration
        if (user_input.__contains__('bye')): #end conversation if user says bye
            break
        elif (user_input.lower().__contains__('a movie')): # pick the movie to talk about
            movie = f.findMovie(userName)
        elif (user_input.lower().__contains__('director' or 'directed')): #find the director of the movie we're talking about and store as object for follow up questions about them
            if 'movie' in locals(): # check if a movie is being spoken about
                person = f.findDirector(movie)
            else:
                print('IMDBot: Sorry, I do not know what you are talking about.') # if a movie is not being currently discussed, tell user it doesn't understand
        else:
            print('IMDBot: Sorry, what you are saying is a bit out of my scope right now') 
    except(KeyboardInterrupt, EOFError, SystemExit): #end conversation in case of fatal error or user inputs ctrl+c
        break
print('\nIMDBot: Goodbye! It was nice talking to you ' + userName)