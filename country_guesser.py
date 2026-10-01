print("\U0001F389" * 10 + "Welcome The Guessing Game"+ "\U0001F389" * 10)
print("\U0001F31F My friends call me Guesser")
print ("\U0001F3AF My aim is to be a guess game. I will give a hint then user try to guess.")
print ("\U000023F3 The game will finish when maximum guess number reached or when you guess corrrect.")
print ("\U0001F4A1 Do not worry the program will help you if you come to final guesses.")
print ("\U0001F3B2" * 10 + "\n")



user_name = input("What is your name? ")
print ("\U0001F91D Nice to meet you", user_name, "Let's start to guess")

#Program choses a number between 1 and 10
import random
import math
rand_number = random.randrange(1,11)


#The program prints the first hint
print("\n" + "\U0001F50D" * 10 + " FIRST HINT! " + "\U0001F50D" * 10)
print ("\U0001F30E The subject is countries")

# User enters the maximum guess number then start to guess.
maximum = int (input("Enter the maximum guess number you want (chose between 1-10)"))
choose = input("\U0001F3AF Enter your guess: ")

number = 1
country = 0

# While number is smaller or equal to maximum guess number the game continues.
while(number <= maximum):
       
       # The assigned numbers for each country respect to input
       if (choose == "canada"):
           country = 1

       elif (choose == "england"):
             country = 2
    
       elif (choose == "germany"):
             country = 3

       elif (choose == "mexico"):
             country = 4

       elif (choose == "france"):
             country = 5

       elif (choose == "italy"):
             country = 6

       elif (choose == "turkiye"):
             country = 7

       elif (choose == "india"):
             country = 8

       elif (choose == "china"):
             country = 9

       elif (choose == "japan"):
             country = 10
             
    
       #Second hint if the guess number reaches 2/3 of maximum guess number.
       if (number == math.floor(2*maximum/3)):
           
              
              if (country == rand_number): 
                  number = maximum + 1
      
              else:
                   #if the last guess is wrong, the program prints appropriate second hint.
                   print("\U0001F44E Incorrect. Don't worry", user_name, ". Rome wasn't built in a day\U0001F9D0\U0001F9D0\U0001F9D0")
                   print ("\n" + "\U0001F50D" * 10 + "Do not worry. Here is your second hint."+ "\U0001F50D" * 10)
               
                   if (rand_number == 1):
                        print("\U0001F30E This country in North America")
                        choose = input("Enter your guess: ")
                        
                                            
                   elif (rand_number == 2):
                        print ("\u26BD Where was soccer founded?")
                        choose = input("Enter your guess: ")
                         
                        

                   elif (rand_number == 3):
                          print ("\U0001F3F0 Where is famous with Cologne Cathedral?")
                          choose = input("Enter your guess: ")
                           
                          

                   elif (rand_number == 4):
                          print ("\U0001F32E Where is famous with taco?")
                          choose = input("Enter your guess: ")
                           
                          
                      
                   elif (rand_number == 5):
                          print ("\U0001F1EB\U0001F1F7 My favourite word is oui.")
                          choose = input("Enter your guess: ")
                           

                   elif (rand_number == 6):
                          print ("\U0001F3DB Where is Tower of Pisa?")
                          choose = input("Enter your guess: ")
                           
                          

                   elif (rand_number == 7):
                           print ("\U0001F362 This country has so much kebab and doner.")
                           choose = input("Enter your guess: ")
                            
                      
                   elif (rand_number == 8):
                          print ("\U0001F3F0 Where is Taj Mahal?")
                          choose = input("Enter your guess: ")
                           
                         
                   elif (rand_number == 9):
                          print ("\U0001F465 This country has the most population in the world")
                          choose = input("Enter your guess: ")
                           
                      
                   elif (rand_number == 10):
                          print ("\U0001F697 Where was Toyata established?")
                          choose = input("Enter your guess: ")
                          
                          
 
                   if (choose == "canada"):
                       country = 1

                   elif (choose == "england"):
                         country = 2
    
                   elif (choose == "germany"):
                         country = 3

                   elif (choose == "mexico"):
                        country = 4

                   elif (choose == "france"):
                         country = 5

                   elif (choose == "italy"):
                         country = 6

                   elif (choose == "turkiye"):
                         country = 7

                   elif (choose == "india"):
                         country = 8

                   elif (choose == "china"):
                         country = 9

                   elif (choose == "japan"):
                         country = 10
                          
                          
       # print different messages if the user guess correctly in different guess numbers.
       if (country == rand_number):
           print("\U0001F44D Correct ", user_name, ". What a guesser")
           if(number == 1):
              print("I bet you are the cleverest person in the world,", user_name, " \U0001F929\U0001F929\U0001F929")
              
           elif(number <= math.floor(1/3*maximum)):
                print("You,", user_name, ", can build your Rome in a day \U0001F605\U0001F605\U0001F605.")

           elif (number <= math.floor(2/3*maximum)):
                 print ("It is good guess, and", user_name," I believe you can better in next play \U0001F60A\U0001F60A\U0001F60A.")
           

           elif (number > math.floor(2/3*maximum)):
                print ("You saved the reputation of", choose,"\U0001F628\U0001F628\U0001F628") 
                      
                      
           number = maximum + 1
           
           
       # if guess is incorrect, take another input for guess
       elif(country!=rand_number):
           print("\U0001F44E Incorrect. Don't worry", user_name, ". Rome wasn't built in a day\U0001F9D0\U0001F9D0\U0001F9D0")
           number = number + 1
           if (number < maximum ):
               choose = input("\U0001F3AF Enter your guess: ")
           #if it is the last guest, print appropriate message.
           if (number == maximum ):
                  print("Upps...This is your last guess,", user_name, "\U0001F62D\U0001F62D\U0001F62D.")
                  number = maximum + 1

print("\n")
print("Thank",user_name,"for guessing with us.")
print("We hope you spent a good and enjoyable time.")

input()

