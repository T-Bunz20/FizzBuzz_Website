from flask import Flask, render_template

app = Flask(__name__)


@app.route('/fizzbuzz/<int:max_num>')
def start(max_num):
    title = "Fizzbuzz Challenge"

    l = []
    for i in range(1,max_num+1):
        element = str(i) + " "
        if i % 3 == 0:
            element += "Fizz"
        if i % 5 == 0:
            element += "Buzz"
        l.append(element)

    return render_template('challenge.html', title=title, numbers=l)

@app.route('/words/<string:word>')
def words(word):
    word = word.upper()
    title = "Anagrams for " + word + ":"
    f = open("words.txt")
    word_list = f.read().splitlines()
    anagrams = []
    for i in word_list:
        if sorted(i) == sorted(word):
            anagrams.append(i)


    return render_template('challenge.html', title=title, numbers=anagrams)

@app.route('/dictionary')
def dictionary_start():
    title = "Dictionary"
    text = "Choose a letter!"
    real_word = ""
    choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
     "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    return render_template('dictionary.html', title=title, text=text, real_word=real_word, choices=choices)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    title = "Dictionary"
    count = 0
    f = open("words.txt")
    real_word = ""
    word_list = f.read().splitlines()
    for i in word_list:
        if i == word.upper():
            real_word = word + " is a real word!"
        if i.startswith(word.upper()):
            count += 1

    if count == 1:
        text = "1 word with the prefix " + word + "!"
    elif count == 0:
        text = "There are no words with the prefix " + word + "."
    else:
        text = str(count) + " words with the prefix " + word + "!"

    choices = [word+"a", word+"b", word+"c", word+"d", word+"e", word+"f", word+"g", word+"h", 
    word+"i", word+"j", word+"k", word+"l", word+"m", word+"n", word+"o", word+"p", word+"q", 
    word+"r", word+"s", word+"t", word+"u", word+"v", word+"w", word+"x", word+"y", word+"z"]

    return render_template('dictionary.html', title=title, text=text, real_word=real_word, choices=choices)
