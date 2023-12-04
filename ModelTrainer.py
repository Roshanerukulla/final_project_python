
import pandas as pd
import re
from nltk.probability import FreqDist
from nltk.corpus import stopwords 
import spacy
from gensim import corpora, models
import nltk
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))
import streamlit as st


class ModelTrainer:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self._preprocess_data()

    def _preprocess_data(self):
        self.df['Text'] = self.df['Text'].apply(lambda x: x.lower())
        self.df['OriginalComment'] = self.df['Text']  # Create an 'OriginalComment' column with the original comments

    def train_lda_model(self):
        texts = [text.split() for text in self.df['Text']]
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

        lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=2)
        return lda_model
