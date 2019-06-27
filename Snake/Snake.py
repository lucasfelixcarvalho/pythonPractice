import Layout as l


class _BodyPart:
    def __init__(self, column, row, visual):
        self.coord_y = column
        self.coord_x = row
        self.visual_char = visual


class Snake:
    def __init__(self):
        row_position = 1
        column_position = 1

        self.body = [_BodyPart(row_position + 2, column_position, l.Snake.SNAKE_HEAD),
                     _BodyPart(row_position + 1, column_position, l.Snake.SNAKE_BODY),
                     _BodyPart(row_position, column_position, l.Snake.SNAKE_BODY)]

        self.snake_head = self.body[0]

    def move_snake(self, direction):
        curr_head = self.body[0]
        new_head = _BodyPart(0, 0, l.Snake.SNAKE_HEAD)

        if direction == 'LEFT':
            new_head = _BodyPart(curr_head.coord_y, curr_head.coord_x - 1, curr_head.visual_char)
        if direction == 'RIGHT':
            new_head = _BodyPart(curr_head.coord_y, curr_head.coord_x + 1, curr_head.visual_char)
        if direction == 'DOWN':
            new_head = _BodyPart(curr_head.coord_y + 1, curr_head.coord_x, curr_head.visual_char)
        if direction == 'UP':
            new_head = _BodyPart(curr_head.coord_y - 1, curr_head.coord_x, curr_head.visual_char)

        self.body.insert(0, new_head)
        self.snake_head = self.body[0]
        self.body[1].visual_char = l.Snake.SNAKE_BODY

    def remove_tail(self):
        return self.body.pop()

    def is_position_snake(self, coord_y, coord_x):
        for body_part in self.body:
            if body_part.coord_x == coord_x and body_part.coord_y == coord_y:
                return True

        return False

    def collide_itself(self):
        curr_head = self.body[0]

        for body in self.body[1:]:
            if body.coord_y == curr_head.coord_y and body.coord_x == curr_head.coord_x:
                return True

        return False
