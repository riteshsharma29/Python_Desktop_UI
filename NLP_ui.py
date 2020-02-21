from flask import Flask, request, render_template,jsonify
import nltk
from autocorrect import Speller
from gensim.summarization import summarize as g_sumn
import sys
import re
import PySimpleGUI as sg

# 1
def lower_case(text):
    word = text.lower()
    result = {
        "result": word
    }
    result = {str(key): value for key, value in result.items()}
    print(result['result'])

#lower_case('RITESH')

# 2
def sent_tokenize(text):
    sent_tokenize = nltk.sent_tokenize(text)
    result = {
        # remove str() if you want the output as list
        "result": str(sent_tokenize)
    }
    result = {str(key): value for key, value in result.items()}
    print(result['result'])

#sent_tokenize("I'm RITESH. This is a nlp test.")

# 3
def word_tokenize(text):
    word_tokenize = nltk.word_tokenize(text)
    result = {
        "result": str(word_tokenize) #remove str() if you want the output as list
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

#word_tokenize('I AM RITESH')

# 4
def spell_check(text):
    spell = Speller(lang='en')
    spells = [spell(w) for w in (nltk.word_tokenize(text))]
    result = {
        "result": " ".join(spells)
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

#spell_check('Thss iis jus a test')

# 5
def lemmatize(text):
    from nltk.stem import WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()

    word_tokens = nltk.word_tokenize(text)
    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                       word_tokens]
    result = {
        "result": " ".join(lemmatized_word)
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

#lemmatize('this a nlp of this function')

#6
def stemming(text):
    from nltk.stem import SnowballStemmer
    snowball_stemmer = SnowballStemmer('english')

    word_tokens = nltk.word_tokenize(text)
    stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
    result = {
        "result": " ".join(stemmed_word)
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

#stemming('testing the functioning of')

# 7
def remove_tags(text):
    import re
    cleaned_text = re.sub('<[^<]+?>', '', text)
    result = {
        "result": cleaned_text
    }
    result = {str(key): value for key, value in result.items()}
    res = re.sub(' +', ' ', result['result'])
    print (res)

#remove_tags('his <\test> tag    <\test> test')

#8
def remove_numbers(text):

    remove_num = ''.join(c for c in text if not c.isdigit())
    result = {
        "result": remove_num
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

#remove_numbers('nlp test 1243')

#9
def remove_punct(text):
    from string import punctuation
    def strip_punctuation(s):
        return ''.join(c for c in s if c not in punctuation)

    text = strip_punctuation(text)
    result = {
        "result": text
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

# remove_punct("ERROR !!! What ? or $")

#10
def remove_stopwords(text):
    from nltk.corpus import stopwords
    stopword = stopwords.words('english')
    word_tokens = nltk.word_tokenize(text)
    removing_stopwords = [word for word in word_tokens if word not in stopword]
    result = {
        "result": " ".join(removing_stopwords)
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])

# remove_stopwords("Natural Language processing of information")

# 11
def keyword(text):
    word = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(word)
    chunk = nltk.ne_chunk(pos_tag)
    NE = [" ".join(w for w, t in ele) for ele in chunk if isinstance(ele, nltk.Tree)]
    result = {
        "result": NE
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'][0])

#keyword("who is Narendra Modi")

# 12
def summarize(text):
    sent = nltk.sent_tokenize(text)
    if len(sent) < 2:
        summary1 =  "please pass more than 3 sentences to summarize the text"
    else:
        summary = g_sumn(text)
        summ = nltk.sent_tokenize(summary)
        summary1 = (" ".join(summ[:2]))
    result = {
        "result": summary1
    }
    result = {str(key): value for key, value in result.items()}
    print (result['result'])


#summarize('test')


# UI layout
sg.theme('TanBlue')

layout = [
    [sg.Submit('LOWER CASE', size=(15, 2)), sg.Submit('SENT TOKENIZE', size=(15, 2)),
     sg.Submit('WORD TOKENIZE', size=(15, 2)), sg.Submit('SPELL CHECK', size=(15, 2)),
     sg.Submit('LEMMATIZE', size=(15, 2)), sg.Submit('STEMMING', size=(15, 2))],
    [sg.Submit('REMOVE TAGS', size=(15, 2)), sg.Submit('REMOVE NUMBERS', size=(15, 2)),
     sg.Submit('REMOVE PUNCTUATION', size=(15, 2)), sg.Submit('REMOVE STOPWORDS', size=(15, 2)),
     sg.Submit('KEYWORD', size=(15, 2)), sg.Submit('SUMMARIZE', size=(16, 2))],
    [sg.Text('INPUT TEXT                    ', size=(10, 1)), sg.Multiline(size=(80, 12),font=("Helvetica", 12), key='Input')],
    [sg.Submit('CLEAR INPUT', size=(30, 2)), sg.Submit('CLEAR OUTPUT', size=(30, 2)),
     sg.Submit('CLEAR ALL', size=(30, 2))],
    [sg.Text('RESULT                    ', size=(10, 1)), sg.Output(size=(80, 12),font=("Helvetica", 12), key='Output')],
    ]

window = sg.Window('NLP Text Proccesor UI', layout)

while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'Exit':
        break
    #  we pass raw string pattern with r'{}'.format(v['Pattern'])
    elif e == 'LOWER CASE' and v['Input'] != 0:
        lower_case(v['Input'])
    elif e == 'SENT TOKENIZE' and v['Input'] != 0:
        sent_tokenize(v['Input'])
    elif e == 'WORD TOKENIZE' and v['Input'] != 0:
        word_tokenize(v['Input'])
    elif e == 'SPELL CHECK' and v['Input'] != 0:
        spell_check(v['Input'])
    elif e == 'LEMMATIZE' and v['Input'] != 0:
        lemmatize(v['Input'])
    elif e == 'STEMMING' and v['Input'] != 0:
        stemming(v['Input'])
    elif e == 'REMOVE TAGS' and v['Input'] != 0:
        remove_tags(v['Input'])
    elif e == 'REMOVE NUMBERS' and v['Input'] != 0:
        remove_numbers(v['Input'])
    elif e == 'REMOVE PUNCTUATION' and v['Input'] != 0:
        remove_punct(v['Input'])
    elif e == 'REMOVE STOPWORDS' and v['Input'] != 0:
        remove_stopwords(v['Input'])
    elif e == 'KEYWORD' and v['Input'] != 0:
        keyword(v['Input'])
    elif e == 'SUMMARIZE' and v['Input'] != 0:
        summarize(v['Input'])
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')
    elif e == 'CLEAR ALL':
        window['Input'].Update('')
        window['Output'].Update('')

