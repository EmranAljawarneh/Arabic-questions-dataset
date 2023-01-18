import pandas as pd

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

arabic_questions_dataset = open('Arabic Generated Dataset.txt', 'r')
arabic_dataset = arabic_questions_dataset.read().splitlines()
for i in arabic_dataset:
  sent_Toke = sent_tokenize(i)
  word_Toke = word_tokenize(i)
  stop_words = set(stopwords.words("arabic"))
  filtered_text = [word for word in word_Toke if word not in stop_words]
  stems = [stemmer.stem(word) for word in word_Toke]
  lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_Toke]
  print(lemmas)

