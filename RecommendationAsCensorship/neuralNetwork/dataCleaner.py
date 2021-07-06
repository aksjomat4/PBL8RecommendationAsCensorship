import re
import gensim
from nltk.tokenize.treebank import TreebankWordDetokenizer


class DataCleaner:
    def __init__(self):
        pass

    stopWords = {
        'a', 'an', 'in', 'on', 'is', 'are', 'the', 'png', 'was', 'were'
    }

    def clean(self, comment):

        #Splitting pd.Series to list
        temp = self.depure_data(comment)

        data_words = self.sent_to_words(temp)

        sentences = [
            word for word in data_words if word not in DataCleaner.stopWords
        ]

        return self.detokenize(sentences)

    def depure_data(self, data):

        #Removing URLs with a regular expression
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        data = url_pattern.sub(r'', data)

        # Remove Emails
        data = re.sub('\S*@\S*\s?', '', data)

        # Remove new line characters
        data = re.sub('\s+', ' ', data)

        # Remove distracting single quotes
        data = re.sub("\'", "", data)

        return data

    def sent_to_words(self, comment):
        return gensim.utils.simple_preprocess(str(comment), deacc=True)
        # deacc=True removes punctuations

    def detokenize(self, text):
        return TreebankWordDetokenizer().detokenize(text)