pip install googletrans==3.1.0a0

!pip install textattack

from googletrans import Translator
from textattack.augmentation import EmbeddingAugmenter

translator = Translator()

Question = open("My own questions.txt","r")
read_questions = Question.readlines()

for read_line in read_questions:
  translation = translator.translate(text=read_line, src='ar', dest='en')
  translated_text = [translation.text]
  print(translated_text)

  for text in translated_text:
    write_translated_questions = open('Translated English Questions.txt', 'a+')
    write_english_dataset = write_translated_questions.writelines('%s\n' %text) 

Question.close()
write_translated_questions.close()

read_translated_questions = open('Translated English Questions.txt', 'r')
read_english_questions = read_translated_questions.read().splitlines()  # read without linebreak.

for i in range(0, 100):  # it will generatre 398 questions.
  for line in read_english_questions:
    text = translated_text
    aug = EmbeddingAugmenter()
    new_text = aug.augment(line)
    print(new_text)

    for text in new_text:
      english_questions_dataset = open('English Dataset.txt', 'a+')
      write_english_dataset = english_questions_dataset.writelines('%s\n' %text)

read_english_dataset = open('English Dataset.txt', 'r')
english_dataset = read_english_dataset.read().splitlines()
print(len(english_dataset))

for read_line in english_dataset:
  back_translation = translator.translate(text=read_line, src='en', dest='ar')
  arabic_translated_questions = [back_translation.text]
  print(arabic_translated_questions)

  if translator.detect(arabic_translated_questions) == 'en':
    back_translation = translator.translate(text=arabic_translated_questions, src='en', dest='ar')
  #for arabic_questions in arabic_translated_questions:
    arabic_questions_dataset = open('Arabic Generated Dataset.txt', 'a+')
    write_arabic_questions_dataset = arabic_questions_dataset.writelines('%s\n' %back_translation.text)
  else:
    arabic_questions_dataset = open('Arabic Generated Dataset.txt', 'a+')
    write_arabic_questions_dataset = arabic_questions_dataset.writelines('%s\n' %back_translation.text)

"""# ChatBot building"""

pip install chatterbot

pip install chatterbot_corpus

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

