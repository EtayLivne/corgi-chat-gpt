import pandas as pd
import json
from nltk import sent_tokenize


"""
download https://archive.org/details/twitter_cikm_2010
extract
"""

def tweeter_lines_iter(dataset_file: str, max_lines: int=None):

    with open(dataset_file, encoding="utf-8", mode="r") as handler:
        lines = handler.readlines()
    lengths = {i: 0 for i in range(240)}
    lengths["multiline"] = 0
    lengths["without_data"] = 0
    i = 0
    for l in lines:
        try:
            data = l.split("\t")[-2]
            for sentence in sent_tokenize(data):
                yield sentence
                i += 1
        except:
            pass
        if max_lines is not None:
            if i >= max_lines:
                break

print(len(list(tweeter_lines_iter(r"C:\python_projects\chatgpt_data\test_set_tweets.txt"))))

# def tweeter_lines_iter(dataset_file: str):
#
#     with open(dataset_file, encoding="utf-8", mode="r") as handler:
#         lines = handler.readlines()
#     lengths = {i: 0 for i in range(240)}
#     lengths["multiline"] = 0
#     lengths["without_data"] = 0
#     for i, l in enumerate(lines):
#         try:
#             data = l.split("\t")[-2]
#             lengths["multiline"] += int("\n" in data)
#             lengths[len(data)] += 1
#         except:
#             lengths["without_data"] += 1
#         if i % 5000 == 0:
#             print(i)
#     with open("lengths.json", "w") as handler:
#         json.dump(lengths, handler, indent=4)

# tweeter_lines_iter(r"C:\python_projects\chatgpt_data\test_set_tweets.txt")
# df = pd.read_csv("C:\python_projects\chatgpt_data\link_status_search_with_ordering_real.csv", nrows=10)
# print(len(df))
# print(list(df.columns))
# for k,v in dict(df.iloc[0]).items():
#     print(f"{k}: {v}")