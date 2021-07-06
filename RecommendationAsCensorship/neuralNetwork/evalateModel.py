import tensorflow as tf
import numpy
from dataCleaner import DataCleaner
import json

model = tf.keras.models.load_model('model')


def toTensor(testData):
    testData = tf.constant(testData, dtype=tf.float32)
    return testData


# using existing comment for testing saved neural network. This comment originally got score 616
testingComment = "What a tragedy this is and probably will remain for the coming decade. The silence from governments all around the world is symbolic for the lack of balls to speak out against the atrocities."

cleaner = DataCleaner()

cleanComment = cleaner.clean(testingComment)

#print(cleanComment)

commentList = []
wordsInComments = set()
wordsWithCountsPerComment = []

comments = cleanComment

wordsWithCounts = dict()
for word in comments.split(' '):
    if word in wordsWithCounts:
        wordsWithCounts[word] += 1
    else:
        wordsWithCounts[word] = 1
    wordsInComments.add(word)

sortedWords = list(wordsInComments)
sortedWords.sort()

with open("words.json", "r") as f:
    sortedWords = json.load(f)

for i in range(len(sortedWords)):
    print("{} -> {}".format(i, sortedWords[i]))

MLInputPerComment = []

wordsWithCountsVector = [0] * len(sortedWords)
for word, count in wordsWithCounts.items():
    wordsWithCountsVector[sortedWords.index(word)] = count
MLInputPerComment.append(wordsWithCountsVector)

# result = model.call(toTensor([[1, 0]]))
# print(result[0][0].numpy())

result = model.call(toTensor(MLInputPerComment))
print(result[0][0].numpy())