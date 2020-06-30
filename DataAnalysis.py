import ImportTitanicData
import DataPreparation

class DataAnaliysis():
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


    #
    #
    # def showTest(self):
    #     test = ImportTitanicData.DataImport.importTest()
    #     return test.head()

    # def showTest ()




dataAnaysis = DataAnaliysis()

# print('czesio')
print('Analiza danych przed wypełnieniem NaN')
print('Tabela Train\n', dataAnaysis.showTrain())
print('\n\nshape Train\n', dataAnaysis.shapeTrain())
print('\n\ndtypes Train\n', dataAnaysis.dtypesTrain())
