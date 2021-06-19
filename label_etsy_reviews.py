'''

This code is to convert etsy.com scraped reviews into positive or negative..
This will be used for pie chart depicting pos and neg reviews 

'''


import sqlite3 as sql
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from webapp_functions import load_model, check_review


load_model()

def label_etsy_reviews():
    rconn2 = sql.connect('extracted_reviews.db')
    df = pd.read_sql("SELECT * FROM scraped_table",rconn2,columns='Reviews')
    all_reviews=df['Reviews'].iloc[:,]
    labels=pd.Series([check_review(i) for i in all_reviews])
    print(labels)
    labels=[1 if i>=0.9 else 0 for i in labels]
    return labels


labels=pd.Series(label_etsy_reviews())

conn = sql.connect('etsy_labels_only.db')

labels.to_sql('labels_table', conn)
