def response(solution, guess):
    if len(guess) == 0:
        return 'False'
    solution = list(solution)
    guess = list(guess)
    response = {'Location':0, 'Color':0}
    length = len(solution)
    index = 0
    while(index < length):
        if solution[index] == guess[index]:
            solution.pop(index)
            guess.pop(index)
            response['Location'] = response.get('Location') + 1
            length -= 1
        else:
            index += 1

    if len(guess) == 0:
        return response.items()
    else:
        for i in range(len(guess)):
            if guess[i] in solution:
                response['Color'] = response.get('Color') + 1
                solution.pop(i)
    return response.items()

print(response('BGRR', 'BGRR'))