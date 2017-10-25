class RAKE:
    __syms = [',', '.', '!', '?', '"', '(', ')']
    
    __candidates = []
    __phrases = []
    __keywords = []
    
    __frequencies = {}
    __degrees = {}
    __wordscores = {}
    __phrasescores = {}
    
    __result = []
    
    def __init__(self, text, stoplist):
        self.__text = text
        self.__stoplist = stoplist
            
    def getresult(self, toppercent=1.0/3.0):
        self.__phrases = self.__split2phrases(self.__text, self.__stoplist)
        self.__keywords = self.__split2words(self.__phrases)
        self.__frequencies = self.__frequency(self.__keywords)
        self.__degrees = self.__degree(self.__phrases)
        self.__wordscores = self.__wordscore(self.__degrees, self.__frequencies)
        self.__phrasescores = self.__phrasescore(self.__phrases, self.__wordscores)
        print(self.__phrases)
        print(self.__frequencies)
        print(self.__degrees)
        print(self.__wordscores)
        print(self.__phrasescores)

    def __split2phrases(self, text, stopwords):
        result = [""]
        for word in text.split():
            if word.capitalize() in stopwords:
                result[-1] = result[-1].strip(' ')
                result.append("")
            elif word[-1] in RAKE.__syms:
                result[-1] = result[-1].strip(' ')
                result.append("")
            elif word[0] in RAKE.__syms:
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
        frequencies = {}
        for word in keywords:
            if word.capitalize() not in frequencies:
                frequencies[word.capitalize()] = 1
            else:
                frequencies[word.capitalize()] += 1
        return frequencies
    
    def __degree(self, phrases):
        degrees = {}
        for phrase in phrases:
            words = phrase.split()
            for word in words:
                if word.capitalize() not in degrees:
                    degrees[word.capitalize()] = len(words)
                else:
                    degrees[word.capitalize()] += len(words)
        return degrees
    
    def __wordscore(self, degrees, frequencies):
        scores = {}
        for keyword in frequencies:
                scores[keyword] = float(degrees[keyword]) / float(frequencies[keyword])
        return scores
    
    def __phrasescore(self, phrases, wordscores):
        scores = {}
        for phrase in phrases:
            for word in phrase.split():
                if phrase not in scores:
                    scores[phrase] = wordscores[word.capitalize()]
                else:
                    scores[phrase] += wordscores[word.capitalize()]
        return scores
