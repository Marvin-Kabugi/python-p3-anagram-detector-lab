# your code goes here!
class Anagram:
    def __init__(self, word) -> None:
        self.word = set(word)
    
    def match(self, word_list):
        anagram = []
        for word in word_list:
            if set(word) == self.word:
                anagram.append(word)
        return anagram


