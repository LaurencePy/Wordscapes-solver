from flask import Flask, render_template, request
import re

app = Flask(__name__)

def load_words():
		with open('words_alpha.txt') as word_file:
				valid_words = set(word_file.read().split())
		return valid_words

english_words = load_words()

def gapfill(words, wordwithgaps):
		pattern = '^' + wordwithgaps.replace('.', '.') + '$'
		regex = re.compile(pattern)
		return [word for word in words if regex.match(word) and len(word) == len(wordwithgaps)]

def search(letters, lengthofword, findmissing, wordwithgaps):
		words = [word for word in english_words if len(word) == lengthofword and all(word.count(char) <= letters.count(char) for char in word)]
		if findmissing.lower() == "y":
				return gapfill(words, wordwithgaps)
		else:
				return words

@app.route('/', methods=['GET', 'POST'])
def index():
		if request.method == 'POST':
				letters = request.form['letters']
				lengthofword = int(request.form['lengthofword'])
				findmissing = request.form['findmissing']
				wordwithgaps = request.form['wordwithgaps']
				results = search(letters, lengthofword, findmissing, wordwithgaps)
				return render_template('results.html', results=results)
		return render_template('index.html')

if __name__ == '__main__':
		app.run(debug=True)
