from keras.models import Sequential
from keras.layers import Dense
import numpy


class Evaluator:
    def __init__(self, trainData, trainResult, testData, testResult) -> None:
        self.trainData = trainData
        self.trainResult = trainResult
        self.testData = testData
        self.testResult = testResult

        self.epochs = 6

    def run(self):
        x_train, y_train, x_test, y_test = self.getInput()
        print('x_train shape:', x_train.shape)
        print(x_train.shape[0], 'train samples')
        print(x_test.shape[0], 'test samples')

        model = Sequential()
        model.add(Dense(x_train.shape[0], activation='relu'))
        model.add(Dense(50000, activation='relu'))
        model.add(Dense(1, activation='linear'))

        model.compile(loss='categorical_crossentropy')
        model.fit(x_train,
                  y_train,
                  epochs=self.epochs,
                  verbose=1,
                  shuffle=True,
                  validation_data=(x_test, y_test))
        # score = model.evaluate(x_test, y_test, verbose=0)
        # print('Test loss:', score[0])
        # print('Test accuracy:', score[1])
        model.save('model')

    def getInput(self):
        self.trainData = numpy.array(self.trainData).astype('float32')
        self.trainResult = numpy.array(self.trainResult).astype('float32')
        self.testData = numpy.array(self.testData).astype('float32')
        self.testResult = numpy.array(self.testResult).astype('float32')
        return self.trainData, self.trainResult, self.testData, self.testResult


if __name__ == '__main__':
    e = Evaluator([[1, 0]], [[32]], [[1, 0]], [[32]])
    e.run()