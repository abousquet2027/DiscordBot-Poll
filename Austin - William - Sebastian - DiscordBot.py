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











# This is the python placeholder file for the script for the bot.

###########** Beta 0.1.2 **########### BUGGY AS HELL, not really. READ ALL "##" Notes


#Storage were polls are saved temp
polls = ["None"]
voters = []


print("")
print("Welcome to the Poll!")

## Try catch/Switch concept. To manage exception errors, 
# loop wont be cancel until coniditon has been met
while True:
  try:
    poll_t = input("What is the Poll Topic: ")
    if not poll_t.isalpha():
      raise ValueError

    break

  except ValueError:
    print("Please only enter words")

## ################################################### ## 
## WE NEED TO MNAGE EXCEPTIONS HERE, TO MANY VERIABLES ##
## ################################################### ##
## .isdigit() bugs the code
#########################################################
## Im OUT OF OPTIONS | Per S.C |


# Will ask the users for how many options with conditions
limit = int(input("How many options do you want to ask: "))

if limit < 1:
 print("You must ask at least one option.")
 limit = int(input("How many options do you want to ask: "))

elif limit > 10:
 print("You can only ask a maximum of 10 options.")
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

# User will vote
while time.time() - timer < 30: #calculates the time and sets to 30s
 
 votes = int(input("Please vote: "))
 print("")
 
 if votes >= 0 and votes < len(polls):
     print(f"You selected: {polls[votes]}") #pulls the variable from the list
 
     if votes >= 0 and votes < len(polls):
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
## it will update the countdown after another INPUT
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
 