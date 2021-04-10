import nltk

from nltk.tokenize import word_tokenize, sent_tokenize, casual_tokenize, MWETokenizer
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.probability import FreqDist
from nltk import pos_tag

import pandas

# TASK 1
f = open('./DATA/BIO_CS_DATA/TEST/biology/class_11_biology_chapter_1_0.txt', 'r')

file_str = f.read().lower()

# Task 2
sentences = sent_tokenize(file_str)

tokens_word = word_tokenize(file_str)
tokens_word_set = set(tokens_word)

tokens_casual = casual_tokenize(file_str)
tokens_casual_set = set(tokens_casual)

mwe = MWETokenizer([('in', 'the'), ('get', 'a')])
tokens_mwe = mwe.tokenize(casual_tokenize(file_str))
tokens_mwe_set = set(tokens_mwe)

mean_list = []

for s in sentences:
    mean_list.append({
        'word_tokenizer': len(word_tokenize(s)),
        'casual_tokenizer': len(casual_tokenize(s)),
        'MWETokenizer': len(mwe.tokenize(casual_tokenize(s)))
        })

# Task 3
token_union = tokens_word_set.union(tokens_casual_set).union(tokens_mwe_set)

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer(language='english')

original_token_list = [t for t in token_union]
stemmed_list_porter = [porter.stem(t) for t in token_union]
stemmed_list_lancaster = [lancaster.stem(t) for t in token_union]
stemmed_list_snowball = [snowball.stem(t) for t in token_union]

df = pandas.DataFrame(data={
    'original_token': original_token_list,
    'porter': stemmed_list_porter,
    'lancaster': stemmed_list_lancaster,
    'snowball': stemmed_list_snowball
    })

# Task 4
freq_dist = FreqDist(casual_tokenize(file_str))
most_common = freq_dist.most_common(10)
hapaxes = freq_dist.hapaxes()

freq_dist.plot()
# Se observa, in primul rand, ca majoritatea cuvintelor sunt hapaxe din cauza ca corpus-ul este mic.
# Din acelasi motiv, se observa 'alunecari' din ce in ce mai vizible apropiindu-ne de y=1.
# Daca am fi avut un corpus gigantic, graficul ar fi apropiat de o functie liniara la aparenta.
# Din grafic se observa ca fie avem cuvinte foarte des intalnite, fie avem hapaxe, ceea ce indica ca avem un corpus mic.


# Task 5
pos = pos_tag(casual_tokenize(file_str))
pos_dict = { tag: [] for (word, tag) in pos }

for (word, tag) in pos:
    pos_dict[tag].append(word)

pos_tag_fd = FreqDist(tag for (word, tag) in pos).most_common()