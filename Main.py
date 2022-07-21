letter = input('Please enter the letter : ').lower()
number_of_persons = int(input('Please enter the number of persons : '))

answer = [{} for _ in range(number_of_persons)] #To save the word that each person chooses

parts = ['name', 'city', 'food', 'color']

answers = {part:[] for part in parts} #To save all words selected in a part

print()

for i in range(number_of_persons):
    print(f'\nThe {i + 1}st person ->\n')
    for part in parts:
        word = input(f'Please enter the {part} : ').lower()
        answer[i][part] = word
        answers[part].append(word)

score = [0 for _ in range(number_of_persons)]

print()

for i in range(number_of_persons):
    for part in parts:
        ans = answer[i][part]

        if ans[0] != letter:
            pass
        elif answers[part].count(ans) > 1:
            score[i] += 5
        else:
            score[i] += 10
    

    if i + 1 == 1:
        print(f'The 1st persons score is : {score[i]}')
    elif i + 1 == 2:
        print(f'The 2nd persons score is : {score[i]}')
    elif i + 1 == 3:
        print(f'The 3rd persons score is : {score[i]}')
    else:
        print(f'The {i}th persons score is : {score[i]}')
