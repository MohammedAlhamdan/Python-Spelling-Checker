from flask import Flask
from Functions import Edit_Distance, Vocab
app = Flask(__name__)

app = Flask(__name__)

@app.route('/Edit Distance')
def call_method1():
    return Edit_Distance.editDistance()

@app.route('/Create a Dictionary')
def call_method2():
    return Vocab.create_vocabulary_dict()

@app.route('/Spelling Checker')
def call_method2():
    return Vocab.spelling_checker()

if __name__ == '__main__':
    app.run(debug=True)