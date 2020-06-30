import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.inf)

#GenderSubmission = pd.read_csv("titanic/gender_submission.csv", header=0, nrows=420)
#Train = pd.read_csv("titanic/train.csv", header=0, nrows=893)
Test = pd.read_csv("titanic/test.csv", header=0, nrows=420)

#print(Test.to_string())
#print(GenderSubmission.to_string())
#print(Train.to_string())

# dataGS = GenderSubmission.to_numpy()
# dataTrain = Train.to_numpy()
#dataTest = Test.to_numpy()

class DataImport:
    def importTest(self):
        return pd.read_csv("titanic/test.csv", header=0, nrows=420)

    def importTrain(self):
        return pd.read_csv("titanic/train.csv", header=0, nrows=893)

    def importGenderSubmission(self):
        return pd.read_csv("titanic/gender_submission.csv", header=0, nrows=420)

#dataGS.fillna(0)
#dataTrain.fillna(0)
#dataTest = dataTest.fillna(0)