import spacy 
import pandas as pd 

wsb = pd.read_csv('/Users/jeremiahkamama/Desktop/Article Projects/Spacy-Sent/data/reddit_wsb.csv')

nlp = spacy.load("en_core_web_sm")
doc = nlp(wsb)

