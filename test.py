from flair.models import TextClassifier,SequenceTagger
from flair.data import Sentence

# load tagger
classifier = TextClassifier.load('sentiment')
# tagger = SequenceTagger.load('sentiment')
# make example sentence
sentence = Sentence("The new Apple iPhone is out to all. But I don't think it is worth the cost and the hype")

# call predict
classifier.predict(sentence)
# tagger.predict(sentence)
a = 492942336
b = 1241977025

# check prediction
for lable in sentence.labels:
    print(f'{lable.value} scored {lable.score}')
