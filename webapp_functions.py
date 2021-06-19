'''

All the functions neended for the web application to run

'''


import pickle
import webbrowser
import pandas as pd
import sqlite3 as sql
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow import keras
from collections import Counter
import itertools
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords




def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrapped_etsy_reviews.csv')
  
    global pickle_model
    pickle_model = keras.models.load_model('model.h5')

    global vocab
    file = open("tfidf_vocab.pkl", 'rb') 
    vocab = pickle.load(file)



def check_review(reviewText):

    vectorizer = TfidfVectorizer(vocabulary=vocab,decode_error='replace')
    vectorised_review = vectorizer.fit_transform([reviewText]).todense()
    return pickle_model.predict(vectorised_review)



def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    

    

def get_freq_words():
    
    rconn = sql.connect('extracted_reviews.db')
    df = pd.read_sql("SELECT * FROM scraped_table",rconn,columns='Reviews')
    df = df.sample(500)
    all_words=list(df['Reviews'])
    
    most_freq_wrds=[wrd.lower().split( ) for wrd in all_words]
    most_freq_wrds=list(itertools.chain(*most_freq_wrds))
    most_freq_wrds=[wrd for wrd in most_freq_wrds if not wrd in stopwords.words('english')]
    most_freq_wrds = Counter(most_freq_wrds).most_common(500)
    
    dfm=pd.DataFrame({'word':[i for i,j in most_freq_wrds],'freq':[j for i,j in most_freq_wrds]})
    
    return dfm




def plot_cloud(data):
    d = {a: x for a, x in data.values}
    cloud = WordCloud (
                    background_color = 'white',
                    width = 512,
                    height = 384
                        )
    cloud.fit_words(d)
    return cloud.to_image()
    



def get_etsy_labels():
    rcon = sql.connect('etsy_labels_only.db')
    df1 = pd.read_sql("SELECT * FROM labels_table",rcon)
    df1 = df1.iloc[:,-1]
    label_count=Counter(df1)
    count_list=[j for (i,j) in label_count.items()]
    return count_list


