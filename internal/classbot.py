import asyncio
import datetime
import time
from pathlib import Path
import nextcord as discord
import traceback
from nextcord.ext import commands

DiscordBot_Cogs = [
	'cogs.cmd',
	'cogs.srvrestart',
	'cogs.test',
	'cogs.errorhandler',
]

class ringoBot(commands.Bot):
	def __init__(self, command_prefix):
		super().__init__(command_prefix)
		for cogs in DiscordBot_Cogs:
			try:
				self.load_extension(cogs)
			except Exception:
				traceback.print_exc()