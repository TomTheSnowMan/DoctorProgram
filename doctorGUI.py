"""
File: doctorGUI.py
Author: Tom
Date: 4/20/2020
Conducts an interactive session of nondirective psychotherapy
"""

from breezypythongui import EasyFrame
import random

hedges = ("Please tell me more.",
		 "Many of my patients tell me the same the thing.",
		 "Please continue.")

qualifiers = ("Why do you say that ",
			"You seem to think that ",
			"Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours"}

class DoctorGUI(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title = "Eliza 1967")
		self.addLabel(text = "Good morning I hope you are will today.", row = 0, column = 0)
		self.addLabel(text = "What can I do for you today?", row = 1, column = 0)

		self.usertext = self.addTextField(text = "", row = 2, column = 0, sticky = "NSEW")

		self.responseLabel = self.addLabel(text = "", row = 3, column = 0)

		self.addButton(text = "Submit", row = 4, column = 0, command = self.reply)

	def reply(self):
		sentence = self.usertext.getText()
		randNum = random.randint(1, 4)
		if randNum == 1:
			self.responseLabel["text"] = random.choice(hedges)
		else:
			self.responseLabel["text"] = random.choice(qualifiers) + changePerson(sentence)
		self.usertext.setText("")

def changePerson(sentence):
	"""
	Replaces first person pronouns wiht second person pronouns
	"""
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)

def main():
	DoctorGUI().mainloop()

main()