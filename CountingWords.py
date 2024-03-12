import threading

class CountingWords :
    def __init__(self, fileName, numOfParts, split) :
        self.fileName = fileName
        self.numOfParts = numOfParts
        self.split = split
        self.listOfThreads = []
        self.dict= {}
        self.temp = open("./saidaTemp.txt", "a")
        self.contagem = open("./contagem.txt", "a") # Contagem final

        self.text = open(f"./{self.fileName}", "r") # Texto original
        self.divide()

        for t in range(self.numOfParts):
            file = open(f"./part{t+1}.txt", "r")
            thread = threading.Thread(target=self.map, args=(file.name, file.readlines()))
            thread.start()
            self.listOfThreads.append(thread)

        for thread in self.listOfThreads:
            thread.join()

        self.makeDict()
        for key in self.dict:
            self.reduce(key, self.dict[key])

    # Função map
    def map(self, name, content):
        for line in content:
            self.emitIntermediate(line.strip(), 1)        

    # Função reduce
    def reduce(self, word, list):
        result = 0
        for value in list:
            result+= int(value)

        self.emit(word, result)

    # Função auxiliar para dividir arquivo em partes
    def divide(self):
        contentSplit = self.text.read().split(self.split)
        for part in range(self.numOfParts):
            tempFile = open(f"./part{part+1}.txt", "a")

            numberOfWords = len(contentSplit)
            start = part*numberOfWords//self.numOfParts
            end = (part+1)*numberOfWords//self.numOfParts

            listOfWords = contentSplit[start:end]
            for index ,word in enumerate(listOfWords):
                if (index == len(listOfWords) - 1):
                    tempFile.write(f"{word}")
                else:
                    tempFile.write(f"{word}\n")
            tempFile.close()
    
    # Função auxiliar para fazer dict
    def makeDict(self):
        self.temp.close()
        temp = open("./saidaTemp.txt", "r").read().splitlines()

        for item in temp:
            word = item.split(" ")[0]
            number = item.split(" ")[1]
            if self.dict.get(word):
                self.dict[word].append(number)
            else:
                self.dict[word] = [number]
        
        print(self.dict)

    # Função para escrever arquivo final
    def emit(self, word, result):
        self.contagem.write(f'{word} {result}\n')

    # Função para escrever arquivo temporário
    def emitIntermediate(self, word, num):
        self.temp.write(f'{word} {num}\n')

count = CountingWords("generatedText.txt", 3, " ")