# Austin Bousquet, William Dudley, Sebastian Calzada
# CPT 273 Process Automation and Scripting
# FINAL Polly the Polling Discord Bot
#
# Feel free to change the title LOL


# Dependencies
import time
import discord
import os
from better_profanity import profanity

# discord token read from .env file
token = os.environ["discord_token"]










###########** Beta 0.1.3 **###########


#Storage were polls are saved temp
polls = ["None"]
voters = []


print("")
print("Welcome to the Poll!")

## Try catch/Switch concept. To manage exception errors, 
# loop wont be canceled until coniditon has been met
while True:
  try:
    poll_t = input("What is the Poll Topic: ")
    
    if poll_t == "":
      raise ValueError
    
    if profanity.contains_profanity(poll_t):
      raise ValueError

    break

  except ValueError:
    print("You cannot enter an empty Title or Profanity to the poll")
    print("")

## ################################################### ## 
## WE NEED TO MNAGE EXCEPTIONS HERE, TO MANY VERIABLES ##
## ################################################### ##
## .isdigit() bugs the code
#########################################################


# Will ask the users for how many options with conditions
limit = int(input("How many options do you want to ask: "))

if limit < 2:
 print("You must ask at least two options.")
 limit = int(input("How many options do you want to ask: "))

elif limit > 10:
 print("You can only ask a maximum of 10 options.")#another bug
 limit = int(input("How many options do you want to ask: "))
 
  
# Will ask the user for all the options and display the variable number option
for i in range(limit):
 opt = input(f"What is option {i + 1}: ")
 polls.append(opt)


# List of options
def Opt_list():
  for j in range(len(polls)):
    print(j, "-", polls[j])

    


# Show the list
print("")
print("The options are: ")
Opt_list()


## Set timer for users to vote
print("")
print("Timer for 30 seconds")
timer = time.time()

#tc = int(input("Time?"))

## Fix countdown timer
# User will vote
while time.time() - timer < 30: #calculates the time and sets to 30s
 
 votes = int(input("Please vote: "))
 print("")
 
 if votes >= 0 and votes < len(polls):
     print(f"You selected: {polls[votes]}") #pulls the variable from the list ## This can be removed later its just to verify it works
 
     voters.append(polls[votes])
     print("Vote added")
     print("")
 
 else:
    print("Invalid Option")
    print("You must select from the following:")
    Opt_list()


#####################################################################
############### will need to do a try catch to validate exceptions ##
############### Otherwise program will crash #
######################################################
## We need to make the timer working continuesly, 
## it will update the countdown only after another INPUT is made
#
## if time.time() - timer > 30:
##   print("time up")


# Count the new list and shows it
# Used Function Opt_List for concept
print("")
print("Total Votes:")

for n in range(len(polls)):
 poll_cnt = voters.count(polls[n])
 print(polls[n], "-", poll_cnt)
