import pandas as pd
from nltk import sent_tokenize

"""
https://www.kaggle.com/datasets/manann/quotes-500k
"""

def quotes_iter(file: str):
    df = pd.read_csv(file, usecols=['quote'])['quote']
    for quote in list(df):
        for sentence in sent_tokenize(quote):
            yield sentence

    # for x in range(4):
    #     yield x

# i = iter(quotes_iter("C:\python_projects\chatgpt_data\quotes.csv"))
i = iter(quotes_iter("C:\python_projects\chatgpt_data\quotes.csv"))
for _ in range(10):
    print(next(i))
