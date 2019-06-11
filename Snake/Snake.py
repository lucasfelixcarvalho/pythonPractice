import Layout as l


class _BodyPart:
    def __init__(self, column, row, visual):
        self.column_position = column
        self.row_position = row
        self.visual_char = visual


class Snake:
    def __init__(self):
        row_position = 1
        column_position = 1

        self.snake = [_BodyPart(row_position + 2, column_position, l.Snake.SNAKE_HEAD),
                      _BodyPart(row_position + 1, column_position, l.Snake.SNAKE_BODY),
                      _BodyPart(row_position, column_position, l.Snake.SNAKE_BODY)]
