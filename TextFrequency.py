class TextFrequency:
    def __init__(self, file_name):
        self.file_name = file_name;
        self.text = list();
        self.getText()
        

    def getText(self): 
        file = open(self.file_name, 'r')
        self.text = file.read()
        file.close()
    
    def letterFreq(self):
        dictionaryZ = {}
        count = 1
        #wordSplit = self.text.lower().split()
        for prints in self.text:
            if prints in dictionaryZ:
                dictionaryZ[prints] = dictionaryZ[prints] + count
            else:
                dictionaryZ[prints] = count
        return dictionaryZ

    def wordFreq(self):
        dictionaryZ = {}
        count = 1
        wordSplit = self.text.split()
        for prints in wordSplit:
            if prints in dictionaryZ:
                dictionaryZ[prints] = dictionaryZ[prints] + count
            else:
                dictionaryZ[prints] = count
        return dictionaryZ
    
    def toLower(self):
        self.text = self.text.lower()

class HistogramPrinter(TextFrequency):

    def __init__(self, file_name):
        TextFrequency.__init__(self, file_name)
        self.file_name = file_name;
        self.text = list();
        self.getText()
    
    def printLetterHist(self):
        freq = self.letterFreq()
        for item in freq:
            asterisk = ''
            for newitem in range(freq[item]):
                asterisk = asterisk + '*'
            print(item, asterisk)

    def printWordHist(self):
        freq = self.wordFreq()
        for item in freq:
            asterisk = ''
            for newitem in range(freq[item]):
                asterisk = asterisk + '*'
            print(item, asterisk)



mytext= HistogramPrinter('H:\Documents\lyrics.txt')
mytext.toLower()
print("-----------------------------------")

newval = mytext.letterFreq()
for bhbh in newval:
    print(newval[bhbh], bhbh)
print("-----------------------------------")
newval = mytext.wordFreq()
for bhbh in newval:
    print(newval[bhbh], bhbh)
print("-----------------------------------")

mytext.printLetterHist()
print("-----------------------------------")
mytext.printWordHist()
print("-----------------------------------")