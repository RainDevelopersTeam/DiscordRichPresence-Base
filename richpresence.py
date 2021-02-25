import pypresence
import time

import sys
import os

import configuration

richPresence = pypresence.Presence(configuration.settings["clientid"])

richPresence.connect()

richPresence.update(
	state = configuration.settings["state"],
	details = configuration.settings["details"],

	start = time.time(),

	buttons = configuration.buttons,

	large_image = configuration.settings["largeimage"],
	small_image = configuration.settings["smallimage"],
	large_text = configuration.settings["largeimagetitle"],
	small_text = configuration.settings["smallimagetitle"]
)