import re


print("Welcome to Wordscapes solver by Laurence Eaton. Please see instructions for use in readme.md\n")



def load_words():
		with open('words_alpha.txt') as word_file:
				valid_words = set(word_file.read().split())

		return valid_words


if __name__ == '__main__':
		english_words = load_words()

def gapfill(words):
	wordwithgaps = input("\nEnter the word with gaps where '.' is used to show a missing letter: ")
	print("Sorting words...\n")
	pattern = '^' + wordwithgaps.replace('.', '.') + '$'
	regex = re.compile(pattern)
	for word in words:
		if re.match(regex, word):
			print(word)
	inputloop()



def search(letters, lengthofword, findmissing):
	words = []
	print("Searching for words...\n")
	for line in open('words_alpha.txt'):
		word = line.strip()
		if len(word) == lengthofword and all(word.count(char) <= letters.count(char) for char in word):
			print(word)
			words.append(word)
	if findmissing == "y":
		gapfill(words)
	else:
		inputloop()

def inputloop():
		notdone = True

		while notdone:
				letters = input("Enter the letters you have available to create a word: ")
				findmissing = input("Would you like to find words which match certain letters missing? (y/n): ")
				if letters.isalpha():
						lengthofword = int(input("Enter the length of the word to be found: "))
						if lengthofword > 0:
								notdone = False
								search(letters, lengthofword, findmissing)
						else:
								print("Incorrect input. Please redo")
				else:
						print("Incorrect input. Please redo")

inputloop()










