
from keras.optimizers import Adam
from tensorflow_core.python.keras.engine.sequential import Sequential
from tensorflow_core.python.layers.core import Dense, Dropout


class Network:

    def __init__(self):
        self.learning_rate = 0.000005
        self.model = self.createModel()

    def createModel(self, weights=None):
        model = Sequential()
        model.add(Dense(activation='relu', inputShape: [784], units=120))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=420, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=320, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=220, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=4, activation='softmax'))
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)

        if weights:
            model.load_weights(weights)
        return model