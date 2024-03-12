import random

class GenerateFile:
    def __init__(self, minSize, maxSize, wordCount, alphabet = "abcdefghijklmnopqrstuvwxyz"):
        self.minSize = minSize
        self.maxSize = maxSize
        self.wordCount = wordCount
        self.alphabet = alphabet
    
    def generate(self):
        text = open(f"./generatedText.txt", "a")
        for w in range(self.wordCount):
            numOfChars = random.randint(self.minSize, self.maxSize)
            word = ""
            word = word.join(random.choices(self.alphabet, k=numOfChars))
            if (w == self.wordCount - 1): 
                text.write(f"{word}")
            else:
                text.write(f"{word} ")

generateFile = GenerateFile(2, 4, 1000, "abcdef")

generateFile.generate()