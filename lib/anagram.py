class Anagram:
    def __init__(self, word):
        self.word=word
   

    def match (self, wordList):
         
        anagrams = [] 

        for candidate in wordList:
            if sorted(candidate) == sorted(self.word):
                anagrams.append(candidate)

        return anagrams

       

