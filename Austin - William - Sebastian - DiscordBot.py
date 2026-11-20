# Austin Bousquet, William Dudley, Sebastian Calzada
# CPT 273 Process Automation and Scripting
# FINAL Polly the Polling Discord Bot
#
# Feel free to change the title LOL


# Dependencies
import discord
import os

# discord token read from .env file
token = os.environ["discord_token"]











# This is the python placeholder file for the script for the bot.

###########****** Beta 0.1.1******########### (Base code) CHANGE ME  


#Storage were polls are saved temp
polls = ["None"]
voters = []


print("")
print("Welcome to the Poll!")

poll = input("What is the Poll Topic: ")

#Will Ask the users for how many options with conditions

limit = int(input("How many options do you want to ask: "))

if limit < 1:
    print("You must ask at least one option.")
    limit = int(input("How many options do you want to ask: "))

elif limit > 10:
    print("You can only ask a maximum of 10 options.")
    limit = int(input("How many options do you want to ask: "))

else:
   print("Error")


#Will ask the user for all the options and display the variable number option
for i in range(limit):
    opt = input(f"What is option {i + 1}: ")
    polls.append(opt)

#Show the list
print("")
print("The options are: ")

for j in range(len(polls)):
 print(j, "-", polls[j])

#User will vote
votes = int(input("Please vote: "))
print("")

if votes >= 0 and votes < len(polls):
    print(f"You selected: {polls[votes]}") #pulls the variable from the list

    if votes >= 0 and votes < len(polls):
     voters.append(polls[votes])
     print("Vote added") #Just to verify *can be removed*
    
else:
    print("Enter a valid option")
#* will need to do a try catch to validate exceptions *#
    # Otherwise program will crash #


print("")
print("Total Votes:")

#count the new list
for n in range(len(polls)):
    pollcnt = voters.count(polls[n])
    print(polls[n], "-", pollcnt)


