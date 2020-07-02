from DataPreparation import DataPreparation
import numpy as np


class ANN:
    def __init__(self):
        self.neuralNetwork = NeuralNetwork()

    def trainNetwork(self, numberOfIteration):
        dataPreparation = DataPreparation()
        # testData = dataPreparation.prepareTestData()
        trainData = dataPreparation.prepareTrainData()
        trainingInputs = trainData.drop("Survived", axis=1).to_numpy(int)
        trainingOutputs = trainData["Survived"].to_numpy(int)
        trainingOutputs = trainingOutputs.reshape(1, trainingOutputs.size).T
        trainingInputs = np.array(trainingInputs, dtype=np.float128)
        trainingOutputs = np.array(trainingOutputs, dtype=np.float128)
        # print(trainingInputs)
        # print(trainingOutputs)
        self.neuralNetwork.train(trainingInputs, trainingOutputs, numberOfIteration)

    def accuracy(self):
        dataPreparation = DataPreparation()
        testData = dataPreparation.prepareTestData().to_numpy(int)
        testOutput = dataPreparation.prepareSubmissionData().to_numpy(int)
        testOutput = testOutput.reshape(testOutput.size, 1)
        # print(testData)
        # print(testOutput)
        calculated = self.neuralNetwork.think(testData)
        accuracy = (testOutput.size - np.sum(np.abs(testOutput - calculated)))/testOutput.size

        accuracy = accuracy * 100
        print(accuracy)
        return accuracy * 100

    #
    # def accuracy(self, testInput, testOutput):
    #     calculated = self.neuralNetwork.think(testInput)
    #     calculated = self.neuralNetwork.think(testInput)
    #     # return np.sum(accuracy)


class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator
        np.random.seed(1)

        # Set synaptic weights to a 3x1 matrix,
        # with values from -1 to 1 and mean 0
        self.synaptic_weights = 2 * np.random.random((7, 1)) - 1

    def sigmoid(self, x):
        """
        Takes in weighted sum of the inputs and normalizes
        them through between 0 and 1 through a sigmoid function
        """
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """
        The derivative of the sigmoid function used to
        calculate necessary weight adjustments
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # print('testy')
        # print(self.synaptic_weights.shape)
        # print(training_inputs.shape)
        # print(training_outputs.reshape(training_outputs.size, 1))
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result
        """
        for iteration in range(training_iterations):
            # print(iteration)
            # Pass training set through the neural network
            output = self.think(training_inputs)

            # Calculate the error rate
            error = training_outputs - output

            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of the function
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            # Adjust synaptic weights
            self.synaptic_weights += adjustments

    def think(self, inputs):
        """
        Pass inputs through the neural network to get output
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output

if __name__ == "__main__":
    ann = ANN()
    # ann.trainNetwork(10000)
    ann.trainNetwork(10000)
    ann.accuracy()
    # print('wynikkk')
    # print(ann.neuralNetwork.think(np.array([1, 3, 0, 22, 1, 0, 7])))
    # print(ann.neuralNetwork.think(np.array([2, 1, 1, 38, 1, 0, 71])))
    # print(ann.neuralNetwork.think(np.array([3, 3, 1, 26, 0, 0, 7])))
    # ann.calculateAccuracy()
    # print(ann.calculateAccuracy())
# if __name__ == "__main__":
#     # Initialize the single neuron neural network
#     neural_network = NeuralNetwork()
#
#     print("Random starting synaptic weights: ")
#     print(neural_network.synaptic_weights)
#
#     # The training set, with 4 examples consisting of 3
#     # input values and 1 output value
#     training_inputs = np.array([[0, 0, 1],
#                                 [1, 1, 1],
#                                 [1, 0, 1],
#                                 [0, 1, 1]])
#     # dataPreparation = DataPreparation()
#     # trainingInput = dataPreparation.prepareTrainData()
#
#     training_outputs = np.array([[0, 1, 1, 0]]).T
#
#     # Train the neural network
#     neural_network.train(training_inputs, training_outputs, 10000)
#
#     print("Synaptic weights after training: ")
#     print(neural_network.synaptic_weights)
#
#     A = str(input("Input 1: "))
#     B = str(input("Input 2: "))
#     C = str(input("Input 3: "))
#
#     print("New situation: input data = ", A, B, C)
#     print("Output data: ")
#     print(neural_network.think(np.array([A, B, C])))