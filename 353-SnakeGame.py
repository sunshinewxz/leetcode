from collections import *
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = deque([[0,0]])
        self.food = deque(food)
        self.width = width
        self.height = height
        self.direct = {'U':[-1,0], 'L':[0,-1], 'R':[0,1], 'D':[1,0]}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        newhead = [self.snake[0][0] + self.direct[direction][0], self.snake[0][1] + self.direct[direction][1]]
        if newhead[0] < 0 or newhead[0] >= self.height or newhead[1] < 0 or newhead[1] >= self.width or (newhead in self.snake and newhead != self.snake[-1]):
            return -1
        if len(self.food)>0 and newhead == self.food[0]:
            self.food.popleft()
            self.snake.appendleft(newhead)
        else:
            self.snake.appendleft(newhead)
            self.snake.pop()
        return len(self.snake)-1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)