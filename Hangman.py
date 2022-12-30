print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
input("Let's play hangman (click enter to continue)")
input("Pick someone to choose the word and someone to guess (click enter to continue)")
input("Guesser please look away (click enter to continue)")
word = input("Word Chooser, Enter Your Word:").strip().lower()
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
answer = []
for i in range(len(word)):
    answer.append(' _ ')
checker = 0
num = 0
respo = ''
for ele in answer:
    respo  = respo + ele
print('The word has this many characters: ' + str(len(word)))
input('Your goal is to guess all of the right letters befor your stick man gets hanged\nevery wrong answer will reult in another body part on your stick man being drawn\nwhen the whole man is drawn, he gets hanged and you lose (hit enter to continue)')
print('you can start filling in the letters now')
print(respo)

while num <6: 
    guess = input('Enter your guess: ').strip().lower()
    list = []
    ind = 0
    if (guess in word) and (guess not in answer):
        for char in word:
            if guess.lower() == char.lower():
                answer[ind] = char
            ind +=1
        resp = ''
        for el in answer:
            resp  = resp + el
        if resp == word:
            num = 100
        print(resp)
    elif (guess in word) and (guess in answer):
        print("You've already guessed this")
    else:
        num+=1
        if num == 1:
            print('o')
        elif num ==2:
            print('o\n|')
        elif num ==3:
            print('o\nT')
        elif num == 4:
            print(' o\n T\n/')
        elif num == 5:
            print(' o\n T\n/\\')

if num == 100:
    print('Congratulations!!')
else:
    print('Off to the gallows...')
    








