class RAKE:

    __syms = [',', '.', '!', '?', '"']
    
    __candidates = []
    __phrases = []
    __keywords = []

    __result = []
    
    def __init__(self, text, stoplist):
        self.__text = text
        self.__stoplist = stoplist
        self.getresult()
            
    def getresult(self, toppercent=1.0/3.0):
        self.__phrases = self.__split2phrases(self.__text, self.__stoplist)
        print(self.__phrases)
        print(self.__split2words(self.__phrases))

    def __split2phrases(self, text, stopwords):
        symless = ""
        for char in text:
            if char in RAKE.__syms:
                symless += ' '
            else:
                symless += char
        result = [""]
        for word in symless.split():
            if word.capitalize() in stopwords:
                result[-1] = result[-1].strip(' ')
                result.append("")
            else:
                result[-1] += word + ' '
        result[-1] = result[-1].strip(' ') # TODO - Fix this if broken
        return result

    def __split2words(self, phrases):
        result = []
        for phrase in phrases:
            for word in phrase.split():
                result.append(word)
        return result
    
    def __frequency(self, keywords):
        pass



