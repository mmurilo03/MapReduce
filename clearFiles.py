import os

if (os.path.exists("./contagem.txt")):
    os.remove("./contagem.txt")
if (os.path.exists("./generatedText.txt")):
    os.remove("./generatedText.txt")
if (os.path.exists("./saidaTemp.txt")):
    os.remove("./saidaTemp.txt")

count = 1
while True:
    if (os.path.exists(f"./part{count}.txt")):
        os.remove(f"./part{count}.txt")
        count += 1
    else:
        break
    