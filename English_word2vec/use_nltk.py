# import nltk
# nltk.download()
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')
import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence."
tokens = word_tokenize(text)
print(tokens)