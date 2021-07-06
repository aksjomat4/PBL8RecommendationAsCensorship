import json
import neuralNetwork
from dataCleaner import DataCleaner

with open("data.json", "r") as f:
    data = json.load(f)

bodyList = []

scoreList = []

for d in data:
    bodyList.append(d['body'])
    scoreList.append([d['score']])

data = []

cleaner = DataCleaner()

for comment in bodyList:
    data.append(cleaner.clean(comment))

commentList = []
wordsInComments = set()
wordsOccurencesPerComment = []

for comments in data:
    wordsWithCounts = dict()
    for word in comments.split(' '):
        if word in wordsWithCounts:
            wordsWithCounts[word] += 1
        else:
            wordsWithCounts[word] = 1
        wordsInComments.add(word)
    wordsOccurencesPerComment.append(wordsWithCounts)

# for word, count in wordsWithCounts.items():
#     print(word + " -> " + str(count))

sortedWords = list(wordsInComments)
sortedWords.sort()
# with open("words.json", "w") as f:
#     json.dump(sortedWords, f, indent=4, sort_keys=True)

for i in range(len(sortedWords)):
    print("{} -> {}".format(i, sortedWords[i]))

MLInputPerComment = []
for wordsOccurences in wordsOccurencesPerComment:
    wordsOccurencesVector = [0] * len(sortedWords)
    for word, count in wordsOccurences.items():
        wordsOccurencesVector[sortedWords.index(word)] = count
    MLInputPerComment.append(wordsOccurencesVector)

#print(MLInputPerComment)

#Sharing date to test and train part
testVSTrainSeparator = int(len(MLInputPerComment) / 2)

MLInputTrain = MLInputPerComment[:testVSTrainSeparator]
MLInputTest = MLInputPerComment[testVSTrainSeparator:]

MLResultTrain = scoreList[:testVSTrainSeparator]
MLResultTest = scoreList[testVSTrainSeparator:]

# trainData, trainResult, testData, testResult

if __name__ == '__main__':
    e = neuralNetwork.Evaluator(MLInputTrain, MLResultTrain, MLInputTest,
                                MLResultTest)
    e.run()