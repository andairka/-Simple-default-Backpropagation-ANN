import ImportTitanicData

class DataPreparation:
    def prepareTestData(self):
        dataImport = ImportTitanicData.DataImport()

        dataSet = dataImport.importTest()

        # kolumny 'Embarked', 'Ticket', 'Name', 'Cabin' według mnie dane nie są istotne
        # dla uczenia sieci neuronowej dlatego pomijam ich uzupełnianie oraz usuwam je z danych wejściowych

        dataSet.drop(['Embarked'], axis=1, inplace=True)
        dataSet.drop(['Ticket'], axis=1, inplace=True)
        # dataSet.drop(['Sex'], axis=1, inplace=True)
        dataSet.drop(['Name'], axis=1, inplace=True)
        dataSet.drop(['Cabin'], axis=1, inplace=True)

        # kolumnę 'Survived' pomijamy, bo to jest wynik uczenia się naszej sieci
        # dataSet.drop(['Survived'], axis=1, inplace=True)

        # w kolumnach 'PasengerId', 'Pclass', 'SibSp', 'Parch' nie brakuje danych i ich nie zmieniam

        # zmiana NaN w kolumnie 'Fare', poprzez medianę
        dataSet['Fare'].fillna(dataSet['Fare'].mean(), inplace=True)

        # zmiana NaN w kolumnie 'Age', poprzez medianę
        dataSet['Age'].fillna(dataSet['Age'].mean(), inplace=True)

        # zmiana typu danych w kolumnie 'Sex'
        genders = {"male": 0, "female": 1}
        dataSet['Sex'] = dataSet['Sex'].map(genders)

        # print(dataSet.to_string())
        return dataSet

    def prepareTrainData(self):
        dataImport = ImportTitanicData.DataImport()

        dataSet = dataImport.importTrain()

        # kolumny 'Embarked', 'Ticket', 'Name', 'Cabin' według mnie dane nie są istotne
        # dla uczenia sieci neuronowej dlatego pomijam ich uzupełnianie oraz usuwam je z danych wejściowych

        dataSet.drop(['Embarked'], axis=1, inplace=True)
        dataSet.drop(['Ticket'], axis=1, inplace=True)
        # dataSet.drop(['Sex'], axis=1, inplace=True)
        dataSet.drop(['Name'], axis=1, inplace=True)
        dataSet.drop(['Cabin'], axis=1, inplace=True)

        # kolumnę 'Survived' pomijamy, bo to jest wynik uczenia się naszej sieci
        # dataSet.drop(['Survived'], axis=1, inplace=True)

        # w kolumnach 'PasengerId', 'Pclass', 'SibSp', 'Parch' nie brakuje danych i ich nie zmieniam

        # zmiana NaN w kolumnie 'Fare', poprzez medianę
        dataSet['Fare'].fillna(dataSet['Fare'].mean(), inplace=True)

        # zmiana NaN w kolumnie 'Age', poprzez medianę
        dataSet['Age'].fillna(dataSet['Age'].mean(), inplace=True)

        # zmiana typu danych w kolumnie 'Sex'
        genders = {"male": 0, "female": 1}
        dataSet['Sex'] = dataSet['Sex'].map(genders)

        # print(dataSet.to_numpy(int))
        # print(dataSet.astype(int).to_string())
        return dataSet


# dataPreparaion = DataPreparation()
#
# print(dataPreparaion.prepareTrainData())


