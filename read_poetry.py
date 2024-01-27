import pandas as pd


"""
download: https://www.kaggle.com/datasets/terminate9298/gutenberg-poetry-dataset/data
extract
"""

def poetry_iter(path: str):
    df = pd.read_csv(path, usecols=["s"])["s"]
    for line in list(df):
        yield line

i = iter(poetry_iter(r"C:\python_projects\chatgpt_data\Gutenberg-Poetry.csv"))
for _ in range(10):
    print(next(i))