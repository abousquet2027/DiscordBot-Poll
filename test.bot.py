# Austin Bousquet, William Dudley, Sebastian Calzada
# CPT 273 Process Automation and Scripting
# FINAL Polly the Polling Discord Bot
#
# Feel free to change the title LOL


# Dependencies
import os
import discord
from discord import app_commands
from better_profanity import profanity

# variable for the discord token (read from .env)
token = os.environ["DISCORD_TOKEN"]


###############***Austin Bousquet script changes below:################################

# variables for discord intents expressions
# these instruct discord on what to recieve from the api requests
# in this case the default, expressions are from discord.py
intents = discord.Intents.default()

# this is creating the discord client and connection to discord
client = discord.Client(intents=intents)

# variable that stores the commands from discord.py (/poll)
tree = app_commands.CommandTree(client)

# this class is for the buttons, vote storage, and the tally display in discord
class PollView(discord.ui.View):
    def __init__(self, options: list[str], duration: int):
        # this is defining how long the poll will be open
        super().__init__(timeout=duration)
        # this is for holding the poll choices open in the view
        self.options = options
        # this is storing each voters options
        self.votes: dict[int, int] = {}
        # this is the attribute for holding the discord message optjects
        self.message: discord.Message | None = None

        # this for loop is for adding a button for each poll option
        for index, option in enumerate(options):
            button = discord.ui.Button(
                label=option[:80],
                style=discord.ButtonStyle.primary,
            )
            # button callback that records the options index for use
            button.callback = self.make_vote_callback(index)
            # this makes the button visible under the poll message
            self.add_item(button)

    # this is for handling the buttons for 
    def make_vote_callback(self, option_index: int):
        # This is recording or replacing the users vote
        async def vote(interaction: discord.Interaction):
            self.votes[interaction.user.id] = option_index
            # this acknowledges and displays that the vote was recorded to the user
            await interaction.response.send_message(
                f"Your vote for **{self.options[option_index]}** was added.",
                # this forces the message to the user only and not to everyone (discord.py parameter)
                ephemeral=True,
            )
        # returns the callback so it can be assigned to the button clicked
        return vote

    # this runs when the voting timer ends
    async def on_timeout(self):
        # sets the count to 0 for vote choice
        counts = [0] * len(self.options)
        # for loop to count the votres
        for option_index in self.votes.values():
            counts[option_index] += 1
        # formats the results
        results = [
            f"{option}: {counts[index]} vote(s)"
            for index, option in enumerate(self.options)
        ]
        # this disables the buttons after voting ends
        for item in self.children:
            item.disabled = True
        # message shown with final results
        if self.message is not None:
            await self.message.edit(
                content="**Poll is now closed!**\n" + "\n".join(results),
                view=self,
            )

# these are the poll instructions/parameters for /poll
@tree.command(name="poll", description="Polly the poll bot, with buttons!")
@app_commands.describe(
    topic="What is this poll about",
    options="Enter at least 2 choices with a max of 10 choices, each separated by commas",
    duration="Voting time in seconds (10–86400)",
)
async def poll(
    interaction: discord.Interaction,
    topic: str,
    options: str,
    duration: app_commands.Range[int, 10, 86400] = 30,
):
    # this splits the choices by comma and removes whitespace and blanks
    choices = [choice.strip() for choice in options.split(",") if choice.strip()]
    # this is defining the choices (at least 2 and no more than 10)
    if len(choices) < 2 or len(choices) > 10:
        await interaction.response.send_message(
            "Please provide 2–10 choices, separated by commas.",
            ephemeral=True,
        )
        return
    # using the pofanity module, this will reject the poll if it has profanity
    if profanity.contains_profanity(topic) or any(
        profanity.contains_profanity(choice) for choice in choices
    ):
        await interaction.response.send_message(
            "Please be civil, no swearing!",
            # displays message only for the user entering the poll
            ephemeral=True,
        )
        return
    # starts the poll and the timer
    view = PollView(choices, duration)
    # message when a poll starts
    await interaction.response.send_message(
        f"Welcome to Polly the Polling Bot!"
        f"\nCreated Fall of 2026 CPT-273 by:"
        f"\nAustin Bousquet, William Dudley, and Sebastian Calzada"
        f"\n**Poll: {topic}**\nUsing the buttons below please vote."
        f"\nThis poll will close in {duration} seconds.",
        view=view,
    )
    # variable for saving the message for later use
    view.message = await interaction.original_response()


@client.event
async def on_ready():
    # displayed for logs for discord and starting the /poll command
    print(f"Logged in as {client.user}; starting command sync")
    # server id variable (change for different server!)
    guild = discord.Object(id=1562832368472170536)
    # copies the above commands into the discord server
    tree.copy_global_to(guild=guild)

# i was having problems during testing and this is used to force the changes faster on the
# discord server
    try:
        synced = await tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s) to server {guild.id}")
    except Exception as error:
        print(f"Command sync failed: {type(error).__name__}: {error}")

print("running the update poll bot file", flush=True)
client.run(token)

############################################################################################







# # This is the python placeholder file for the script for the bot.

# ###########** Beta 0.1.2 **########### BUGGY AS HELL, not really. READ ALL "##" Notes


# #Storage were polls are saved temp
# polls = ["None"]
# voters = []


# print("")
# print("Welcome to the Poll!")

# ## Try catch/Switch concept. To manage exception errors, 
# # loop wont be canceled until coniditon has been met
# while True:
#   try:
#     poll_t = input("What is the Poll Topic: ")
    
#     if not poll_t.isalpha():
#       raise ValueError
    
#     if profanity.contains_profanity(poll_t):
#       raise ValueError

#     break

#   except ValueError:
#     print("You cannot enter Numbers or Profanity to the poll")
#     print("")

# ## ################################################### ## 
# ## WE NEED TO MNAGE EXCEPTIONS HERE, TO MANY VERIABLES ##
# ## ################################################### ##
# ## .isdigit() bugs the code
# #########################################################


# # Will ask the users for how many options with conditions
# limit = int(input("How many options do you want to ask: "))

# if limit < 2:
#  print("You must ask at least two options.")
#  limit = int(input("How many options do you want to ask: "))

# elif limit > 10:
#  print("You can only ask a maximum of 10 options.")
#  limit = int(input("How many options do you want to ask: "))
 
  
# # Will ask the user for all the options and display the variable number option
# for i in range(limit):
#  opt = input(f"What is option {i + 1}: ")
#  polls.append(opt)


# # List of options
# def Opt_list():
#   for j in range(len(polls)):
#     print(j, "-", polls[j])


# # Show the list
# print("")
# print("The options are: ")
# Opt_list()


# ## Set timer for users to vote
# print("")
# print("Timer for 30 seconds")
# timer = time.time()

# # User will vote
# while time.time() - timer < 30: #calculates the time and sets to 30s
 
#  votes = int(input("Please vote: "))
#  print("")
 
#  if votes >= 0 and votes < len(polls):
#      print(f"You selected: {polls[votes]}") #pulls the variable from the list ## This can be removed later its just to verify it works
 
#      voters.append(polls[votes])
#      print("Vote added")
#      print("")
 
#  else:
#     print("Invalid Option")
#     print("You must select from the following:")
#     Opt_list()


# #####################################################################
# ############### will need to do a try catch to validate exceptions ##
# ############### Otherwise program will crash #
# ######################################################
# ## We need to make the timer working continuesly, 
# ## it will update the countdown only after another INPUT is made
# #
# ## if time.time() - timer > 30:
# ##   print("time up")


# # Count the new list and shows it
# # Used Function Opt_List for concept
# print("")
# print("Total Votes:")

# for n in range(len(polls)):
#  poll_cnt = voters.count(polls[n])
#  print(polls[n], "-", poll_cnt)
