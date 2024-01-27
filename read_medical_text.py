import pandas as pd
from nltk import sent_tokenize

"""
follow instructions in: https://www.kaggle.com/datasets/xhlulu/medal-emnlp
"""
def read_medical_iter(file: str):
    text_series = pd.read_csv(file, usecols=["TEXT"])["TEXT"]
    for text in text_series:
        for sentence in sent_tokenize(text):
            yield sentence

i = iter(read_medical_iter("C:\python_projects\chatgpt_data\medal-test.csv.csv"))
for j in range(50):
    print(f"j: {next(i)}\n\n")
