#Jordan Brooks
#Pythonian program
#Yo Mama Joke prompter

#Help from: 
		#My roomates CIS 221 Python textbook
		#Roomates knowledge of creating classes
		#Stack Overflow
		#Morgan Benton slides on flow control
		#previous projects i made



def yomama(): 
#First thing you see when program starts up	
	print ("Welcome to Jordan's Yo Mama joke project! These jokes are not for the faint of heart. Proceed with caution.")


def bye():
#Last thing you see when you exit
    print ("I hope you got a laugh! No hard feelings of course.")


def main():
#My actual program to display a joke	
	a = input('Enter a number 1-9: ')

	if (a == '1'):
		print('Yo Mama so fat when she went to the movies she sat next to everyone!')

	if (a == '2'):
		print('Yo mama so poor when she goes to KFC, she has to lick other peoples fingers!')

	if (a == '3'):
		print('Yo Mama so fat, that when she fell, no one was laughing but the ground was cracking up! ')

	if (a == '4'):
		print('Yo Mamas so nasty, I talked to her over the computer and she gave me a virus!')

	if (a == '5'):
		print('Yo Mama so stupid, she put two quarters in her ears and thought she was listening to 50 Cent!')

	if (a == '6'):
		print('Yo Mama house so dirty she has to wipe her feet before she goes outside!')

	if (a == '7'):
		print('Yo Moma is so fat when she got on the scale it said, "I need your weight not your phone number!"')

	if (a == '8'):
		print('Yo Mama so lazy she thinks a two-income family is where yo daddy has two jobs!')

	if (a == '9'):
		print('Yo mama so ugly she looks out the window and got arrested for mooning!')

#For when a user types in an invalid input
	if a not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
   		print ('Incorrect input. Yo Mama must have made you stupid. You made me mad and now I kicked you out of my program.')


#EVERYTHING ABOVE IS JUST DEFINING CLASSES!
#PROGRAM ONLY STARTS ONCE yomama() RUNS


yomama()
#yomama class
main()
#main program that displays jokes


#Choose to pick another joke or exit program
b = input('Type "more" and then Enter to see another joke. To exit program press Enter:  ')
if (b == 'more'):
	main()
else:	
	bye()
	#class bye gives you final goodbye message
	
