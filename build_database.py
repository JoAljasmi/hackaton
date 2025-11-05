from wordfetcher import WordFetcher
import pandas as pd

wordfetcher = WordFetcher(word_length=5, word_amount=10000)

words_list = wordfetcher.return_word()
pd.DataFrame(words_list).to_csv("word_data.csv", index=False)