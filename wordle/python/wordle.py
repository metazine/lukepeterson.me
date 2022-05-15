import csv
import random

def main():
    wordList = []
    with open("5letterwords.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            wordList.append(row[0])
    
    randomWord = random.choice(wordList)    

    guesses = 0
    while True:
        guesses += 1
        word = getFiveLetterWord()
        if compareWords(word, randomWord):
            print("It took you", guesses, "to guess the word")
            break

def getFiveLetterWord():
    while True:
        word = input("Enter a five letter word")
        
        if len(word) == 5:
            return word

def compareWords(word1, word2):
    outputWord = []
    sameLetterPosition = []
    
    for i in range(len(word1)):
        outputWord.append(word1[i])
        sameLetterPosition.append(" ")
        
        if word1[i] in word2:
            outputWord[i] = word1[i].upper()
        
        if word1[i] == word2[i]:
            sameLetterPosition[i] = "^"
    
    print("".join(outputWord))
    print("".join(sameLetterPosition))

    if "^" * 5 in "".join(sameLetterPosition):
        return(True)
    return(False)
    

if __name__ == "__main__":
    main()
