I am putting my notes here from my research on the profanity filter and packages etc. so we can easily look at this when we meet sunday
probably won't have much on it until saturday or sunday morning


Profanity filtering
- module =  better-profanity
filters swears and variations of swears like when people use @ instead of a or $ instead of S etc.
Can replace letters of the swears with *** or just block the words if we prefer, can talk on sunday


Discord.py notes:
potentially use from discord import app_commands
discord.ui.Button variable can configure a button, so the voting stays anonymous
may need to use modals
something like this to command bot:   bot = commands.Bot(command_prefix="/", intents=intents)

may need to use re module to make a list of political words we don't want to allow, profanity module doesn't have any political filtering up to us if we still want to exclude politics
