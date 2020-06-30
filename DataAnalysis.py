import ImportTitanicData
import DataPreparation

# analiza danych przed preparacją danych
class DataAnaliysisBefore():
    def showTrain(self):
        importData = ImportTitanicData.DataImport()
        train = importData.importTrain()
        return train

    def shapeTrain(self):
        return self.showTrain().shape

    def dtypesTrain(self):
        return self.showTrain().dtypes

    def showTest(self):
        importData = ImportTitanicData.DataImport()
        test = importData.importTest()
        return test

    def shapeTest(self):
        return self.showTest().shape

    def dtypesTest(self):
        return self.showTest().dtypes

# analiza danych po preparacji danych
class DataAnaliysisAfter():
    def showTrain(self):
        dataPreparation = DataPreparation.DataPreparation()
        train = dataPreparation.prepareTrainData()
        return train

    def shapeTrain(self):
        return self.showTrain().shape

    def dtypesTrain(self):
        return self.showTrain().dtypes

    def showTest(self):
        dataPreparation = DataPreparation.DataPreparation()
        test = dataPreparation.prepareTestData()
        return test

    def shapeTest(self):
        return self.showTest().shape

    def dtypesTest(self):
        return self.showTest().dtypes

    #
    #
    # def showTest(self):
    #     test = ImportTitanicData.DataImport.importTest()
    #     return test.head()

    # def showTest ()



# dataAnaysis = DataAnaliysisBefore()
dataAnaysis = DataAnaliysisAfter()

# print('czesio')
# print('Analiza danych przed wypełnieniem NaN')
# print('Tabela Train\n', dataAnaysis.showTrain())
# print('\n\nshape Train\n', dataAnaysis.shapeTrain())
# print('\n\ndtypes Train\n', dataAnaysis.dtypesTrain())

print('Analiza danych po wypełnieniem NaN i preparacji danych')
print('Tabela Train\n', dataAnaysis.showTrain())
print('\n\nshape Train\n', dataAnaysis.shapeTrain())
print('\n\ndtypes Train\n', dataAnaysis.dtypesTrain())

# dataPreparation = DataPreparation.DataPreparation()
# print(dataPreparation.prepareTrainData().to_string())

