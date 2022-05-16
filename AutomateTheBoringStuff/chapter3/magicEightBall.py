import random

def main():
    answerNumber = random.randint(1, 8)
    print(getAnswer(answerNumber))

def getAnswer(answerNumber):
    answers = [
        "It is certain",
        "It is decidedly so",
        "Yes",
        "Reply hazy try again",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook not so good",
        "Very doubtful"
    ]

    return answers[answerNumber - 1]

if __name__ == "__main__":
    main()