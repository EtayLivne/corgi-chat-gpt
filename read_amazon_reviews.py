from itertools import chain

"""
download https://www.kaggle.com/datasets/bittlingmayer/amazonreviews?resource=download
extract, and then extract again.
"""


def amazon_review_lines_iter(dataset_path: str):
    prefix_len = len("__label__2 ")
    with open(dataset_path, encoding="utf-8", mode="r") as handler:
        lines = handler.readlines()

    return chain(
        [[s.strip() + "." for s in l[prefix_len:].split(".")] for l in lines]
    )