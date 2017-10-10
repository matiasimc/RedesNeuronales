import nltk
import numpy as np
from csvtopoems import *
from options import *
import itertools

'''
Convertir la lista de poemas (que a su vez es una lista de estrofas, que a su vez 
es una lista de versos) en un gran string que contenga los tokens especiales de 
comienzo y final de poemas, versos y estrofas.
'''
def poems_to_string(plist):
    s = "".encode("utf-8")
    for poem in plist:
        s += "START_POEM "
        for stanza in poem:
            s += "START_STANZA "
            for verse in stanza:
                s += "START_VERSE "
                s += verse.lower()
                s += " END_VERSE "
            s += "END_STANZA "
        s += "END_POEM "
    return s

'''
Convierte un string en tokens
'''
def string_to_tokens(s):
    return nltk.word_tokenize(s)

'''
Obtiene la palabras mas frecuentes y retorna vectores utiles
'''
def get_most_used_words(filename):
    plist = parse_csv(filename)
    s = poems_to_string(plist)
    tokens = string_to_tokens(s)
    word_freq = nltk.FreqDist(tokens)
    vocab = word_freq.most_common(VOCABULARY_SIZE-1)
    index_to_word = [x[0] for x in vocab]
    index_to_word.append("UNKNOWN_WORD")
    word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])
    return index_to_word, word_to_index

'''
Crea los datos de entrenamiento
'''
def get_training_data(filename):
    plist = parse_csv(filename)
    s = poems_to_string(plist)
    tokens = string_to_tokens(s)
    itw, wti = get_most_used_words(filename)
    for i, t in enumerate(tokens):
        tokens[i] = t if t in wti else "UNKNOWN_WORD"
    x_train = np.array([wti[w] for w in tokens[:-1]])
    y_train = np.array([wti[w] for w in tokens[1:]])
    return x_train, y_train



