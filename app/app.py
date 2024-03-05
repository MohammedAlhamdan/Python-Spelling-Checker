from flask import Flask, render_template, request
from Functions.Edit_Distance import editDistance
from Functions.Vocab import create_vocabulary_dict, spelling_checker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    str1 = request.form['str1']
    str2 = request.form['str2']
    distance = editDistance(str1, str2)
    return f'The edit distance between {str1} and {str2} is {distance}'

@app.route('/spelling_checker', methods=['POST'])
def spelling_check():
    corpus_file = request.form['corpus_file']
    misspelled_word = request.form['misspelled_word']

    vocabulary_dict = create_vocabulary_dict(corpus_file)
    corrected_words = spelling_checker(misspelled_word, vocabulary_dict)

    return f'The corrected words for {misspelled_word} are: {", ".join(corrected_words)}'



if __name__ == '__main__':
    app.run(debug=True)