class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = list(secret)
        guess = list(guess)
        response = {'A':0, 'B':0}
        length = len(secret)
        index = 0
        while(index < length):
            if secret[index] == guess[index]:
                secret.pop(index)
                guess.pop(index)
                response['A'] = response.get('A') + 1
                length -= 1
            else:
                index += 1

        result = []
        if len(guess) != 0:
            for i in range(len(guess)):
                if guess[i] in secret:
                    response['B'] = response.get('B') + 1
                    secret.pop(secret.index(guess(i))[0])


        for k in response.keys():
            result.append(k)
            result.append(response.get(k))
        return list(result)

