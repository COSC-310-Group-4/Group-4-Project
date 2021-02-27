import film as f
import person as p
import company as c
import user as u

print('IMDBot: Hello There! My name is IMDBot. ', end='')
userName = u.askForName() #set username for the first time
print(f'IMDBOT: I just want to make sure I have your name right.')
userName = u.checkName(userName) #check username if correct. method can also be used if user wants to change their username
print(f'I am a bot who knows all about movies. How can I help you today?') #concatenates to "IMDBot: That's a cool name, userName! "

while True:
    try:
        user_input = input(f'{userName}: ') #collect user input for this iteration. Do not convert to lower here.
        if (user_input.lower().__contains__('bye')): #end conversation if user says bye
            break
        elif (user_input.lower().__contains__('a movie') or user_input.lower().__contains__('another movie')): # pick the movie to talk about
            movie = f.findMovie(userName)
        elif (user_input.lower().__contains__('director') or user_input.lower().__contains__('directed')): #find the director of the movie we're talking about and store as object for follow up questions about them
            if 'movie' in locals(): # check if a movie is being spoken about
                person = f.findDirector(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to find the director. Try to ask me to find a movie :)') # if a movie is not being currently discussed, tell user it doesn't understand
        elif (user_input.lower().__contains__('production company') or user_input.lower().__contains__('production companies')):
            print("IMDBot: Okay, let me search the production companies for you!") # buffer for searching companies
            companies = c.findCompany(movie) # list the production companies of the movie asked
            print('IMDBot: What else would you like to know about the movie? :)')
        elif (user_input.lower().__contains__('summary') or user_input.lower().__contains__('plot')):
            if 'movie' in locals():
                movie = f.giveSummary(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about. Try to ask me to find a movie :)')
        elif (user_input.lower().__contains__('characters')):
            if 'movie' in locals():
                movie = f.showCharacters(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to list the characters. Try to ask me to find a movie first!')
        elif (user_input.lower().__contains__('who played')):
            if 'movie' in locals():
                character = user_input.split('played ')[1] #if user writes 'who played neo in matrix' cuts to 'neo in matrix'
                character = character.split(' ')[0] #continues to cut the string. now it is 'neo'. this might be problematic because it is only looking at the first name
                person = f.whoPlayed(movie, character)
            else:
                print('IMDBot: Sorry, I need to know which movie you\'re talking about first. Please ask me to look up a movie first.')
        elif (user_input.lower().__contains__('how long') or user_input.lower().__contains__('runtime')):
            if 'movie' in locals():
                movie = f.runtime(movie)
            else:
                print('IMDBot: Sorry, I need to know which movie you want me to check the runtime for. Please ask me to find a movie first.')
        elif (user_input.lower().__contains__('change' and 'name')):
            userName = u.checkName(userName)
            print('How can I help you?') #concatenates to "IMDBot: That's a cool name, userName! "
        elif (user_input.lower().__contains__('nevermind')):
            print(f'IMDBot: Ok. How can I help?')
        elif(user_input.lower().__contains__('a member of')):
            #takes in user input and calls isMember() from person.py
            #input needs to be in the form: "is Tom Holland a member of the movie Cherry"
            #input can only handle people (2 words) and a movie (1 word)
            person = user_input.split("is ")[1]
            person = person.split(' a')[0]
            movie = user_input.split("movie ")[1]
            p.isMember(movie, person)
            print("IMDBOT: They did a great job on the movie! What else do you want to know?")
        elif(user_input.lower().__contains__('what other')):
            #takes in user input and calls otherRoles() from person.py
            #input needs to be in the form: "what other movies is Tom Holland in"
            #person's name has to be 2 words
            person = user_input.split("is")[1]
            person = person.split('in')[0]
            p.otherRoles(person)
            print("IMDBOT: What else would you like to know?")
            
        else:
            print('IMDBot: Sorry, what you are saying is a bit out of my scope right now') 
    except(KeyboardInterrupt, EOFError, SystemExit): #end conversation in case of fatal error or user inputs ctrl+c
        break
print('\nIMDBot: Goodbye! It was nice talking to you ' + userName)