class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list):
        out = []
        for word in list:
            if ''.join(sorted(word)) == ''.join(sorted(self.word)):
                out.append(word)
        return out