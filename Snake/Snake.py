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

        self.body = [_BodyPart(row_position + 2, column_position, l.Snake.SNAKE_HEAD),
                     _BodyPart(row_position + 1, column_position, l.Snake.SNAKE_BODY),
                     _BodyPart(row_position, column_position, l.Snake.SNAKE_BODY)]

    def move_snake(self, direction):
        curr_head = self.body[0]
        new_head = _BodyPart(0, 0, l.Snake.SNAKE_HEAD)

        if direction == 'LEFT':
            new_head = _BodyPart(curr_head.column_position, curr_head.row_position - 1, curr_head.visual_char)
        if direction == 'RIGHT':
            new_head = _BodyPart(curr_head.column_position, curr_head.row_position + 1, curr_head.visual_char)
        if direction == 'DOWN':
            new_head = _BodyPart(curr_head.column_position + 1, curr_head.row_position, l.Snake.SNAKE_HEAD)
        if direction == 'UP':
            new_head = _BodyPart(curr_head.column_position - 1, curr_head.row_position, curr_head.visual_char)

        self.body.insert(0, new_head)
        self.body[1].visual_char = l.Snake.SNAKE_BODY

    def remove_tail(self):
        return self.body.pop()

    def is_position_snake(self, row_position, column_position):
        for body_part in self.body:
            if body_part.row_position == row_position and body_part.column_position == column_position:
                return True

        return False
