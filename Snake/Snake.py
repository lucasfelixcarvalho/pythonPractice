import Layout as l


class Snake:
    def __init__(self):
        row_position = 1
        column_position = 3

        self.snake = [(column_position, row_position, l.Snake.SNAKE_HEAD),
                      (column_position - 1, row_position, l.Snake.SNAKE_BODY),
                      (column_position - 2, row_position, l.Snake.SNAKE_BODY)]
