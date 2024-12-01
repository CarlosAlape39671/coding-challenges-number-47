class Day:
    def __init__(self, x=4, y=3):
        self.validate_size(x, y)
        self.x = x
        self.y = y
        self.xmid = x//2
        self.ymid = y//2
        self.value = 0
        self.gift = ""
        self.board = [["*" for i in range(x)] for j in range(y)]
    
    def set_value(self, value) -> None:
        self.value = value
        if value <= 9:
            self.board[self.ymid][self.xmid -1] = "0"
            self.board[self.ymid][self.xmid] = str(value)
        else:
            self.board[self.ymid][self.xmid - 1] = str(value // 10)
            self.board[self.ymid][self.xmid] = str(value % 10)

    def select(self):
        self.value = 0
        self.board[self.ymid][self.xmid -1] = "*"
        self.board[self.ymid][self.xmid] = "*"
    
    def board_to_string(self) -> str:
        return "\n".join(["".join(row) + " " for row in self.board])
    
    @staticmethod
    def validate_size(x, y) -> None:
        if x < 1 or x % 2 != 0 or y < 1 or y % 3 != 0:
            raise ValueError("Invalid grid size")