file = open("example/definition.txt", 'r', encoding='UTF-8', newline='')
text = file.read() # Finding defintions from Definition page in Wikipedia
file.close()

nobracket = ""

# Removing reference note
bracket = False
for ch in list(text):
    if ch == '[':
        ch = ''
        bracket = True
    if ch == ']':
        ch = ''
        bracket = False
    if bracket == True:
        ch = ''
    nobracket += ch

words = nobracket.split()

wordcount = len(words)

last = "non-period"
sentences = [""]
titles = ["Mrs.", "Mr.", "Dr.", "Mx.", "Ms."]
endsyms = ['.', '!', '?']
commons = ["How", "Does", "Other", "People", "Thing", "Chapter", "About", "Do", "Also", "To", "I", "You", "We", "They", "On", "One", "He", "She", "It", "Us", "The", "That", "This", "Than", "More", "Not", "By", "Yes", "No", "A", "An", "In", "At", "With", "Be", "Is", "Are", "Was", "Were", "Been", "Its", "Who", "Whose", "Where", "What", "Which", "When", "Whose", "As", "Of", "Their", "For", "While", "Since", "And", "Or", "Either", "Why", "Her", "His", "Them", "Him", "Hers", "There"]
defined = ["Is", "Are"]
adj = ["al", "ic", "ed", "ve", "er"]

# Spliting text into sentences
for word in words:
    if word.replace(',', '') in titles or last.replace(',', '') in titles:
        pass
    elif last[len(last)-1] in endsyms and word[0].isupper():
        sentences.append("")
    sentences[len(sentences)-1] += " " + word
    last = word

keywords = {}

# Counting keywords that are not common
for sentence in sentences:
    for word in sentence.split():
        actual = word.capitalize().replace(",", "").replace(".", "").replace("(", "").replace(")", "")
        if actual in commons:
            pass
        elif actual.isdigit():
            pass
        elif actual not in keywords:
            keywords[actual] = 1
        else:
            keywords[actual] += 1

# Sorting keywords by value
keywords = sorted(keywords.items(), key=lambda x:x[1], reverse=True)

# Keeping the most frequent keywords 
mostkeywords = []
for i in range(int(len(keywords) * min(200, wordcount) / wordcount)):
    mostkeywords.append(keywords[i])

# Finding the definitions for keywords
for sentence in sentences:
    s = ""
    for word in sentence.split():
        s += ' ' + word.capitalize()
    for keyword in mostkeywords:
        if keyword[0] in s.split() and (defined[0] in s.split() or defined[1] in s.split()) and (s.find(defined[0]) - s.find(keyword[0]) == len(keyword[0]) + 1 or s.find(defined[1]) - s.find(keyword[0]) == len(keyword[0]) + 1):
            adjective = ""
            i = s.find(keyword[0])
            if s[i-3:i-1] in adj:
                s_adj = s[:i-1].split()
                word = s_adj[len(s_adj)-1]
                if word[len(word)-2:] in adj:
                        adjective = word
                        break
                print("Definition of " + adjective + ' ' + keyword[0] + ":" + sentence + '\n')
            elif s[i-3:i-1] == "Of":
                s_of = s[:i-1].split()
                whichof = s_of[len(s_of)-2]
                print("Definition of " + whichof + ' of ' + keyword[0] + ":" + sentence + '\n')
            else:   
                print("Definition of " + keyword[0] + ":" + sentence + '\n')
            break
