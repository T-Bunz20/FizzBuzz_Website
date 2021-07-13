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
