from loguru import logger

EXAMPLE_ANSWER = 13
EXAMPLE_BONUS_ANSWER = 43


class Coordinate:
    def __init__(self, has_roll: bool):
        self.has_roll = has_roll
        self.touching_rolls = 0
        self.marked_for_removal = False

    def add_adjacent_roll(self):
        self.touching_rolls += 1

    def remove_adjacent_roll(self):
        self.touching_rolls -= 1

    def set_has_roll(self, has_roll: bool):
        self.has_roll = has_roll

    def can_be_removed(self):
        return self.touching_rolls < 4


class Warehouse:
    def __init__(self, max_x: int, max_y: int):
        self.grid: list[list[Coordinate]] = [
            [Coordinate(False) for _ in range(max_x + 1)] for _ in range(max_y + 1)
        ]
        self.max_x = max_x
        self.max_y = max_y

    def add_spot(self, x: int, y: int, has_roll: bool):
        removing_roll = (
            self.grid[y][x].has_roll
            and not has_roll
            and self.grid[y][x].marked_for_removal
        )
        self.grid[y][x].set_has_roll(has_roll)

        if has_roll:
            if y > 0:
                self.grid[y - 1][x].add_adjacent_roll()
                if x > 0:
                    self.grid[y - 1][x - 1].add_adjacent_roll()
                if x < self.max_x:
                    self.grid[y - 1][x + 1].add_adjacent_roll()
            if y < self.max_y:
                self.grid[y + 1][x].add_adjacent_roll()
                if x < self.max_x:
                    self.grid[y + 1][x + 1].add_adjacent_roll()
                if x > 0:
                    self.grid[y + 1][x - 1].add_adjacent_roll()
            if x > 0:
                self.grid[y][x - 1].add_adjacent_roll()
            if x < self.max_x:
                self.grid[y][x + 1].add_adjacent_roll()
        elif removing_roll:
            if y > 0:
                self.grid[y - 1][x].remove_adjacent_roll()
                if x > 0:
                    self.grid[y - 1][x - 1].remove_adjacent_roll()
                if x < self.max_x:
                    self.grid[y - 1][x + 1].remove_adjacent_roll()
            if y < self.max_y:
                self.grid[y + 1][x].remove_adjacent_roll()
                if x < self.max_x:
                    self.grid[y + 1][x + 1].remove_adjacent_roll()
                if x > 0:
                    self.grid[y + 1][x - 1].remove_adjacent_roll()
            if x > 0:
                self.grid[y][x - 1].remove_adjacent_roll()
            if x < self.max_x:
                self.grid[y][x + 1].remove_adjacent_roll()

    def count_free_rolls(self) -> int:
        sum = 0
        for row in range(self.max_y + 1):
            for col in range(self.max_x + 1):
                if (
                    self.grid[row][col].has_roll
                    and self.grid[row][col].touching_rolls < 4
                ):
                    sum += 1
                    self.grid[row][col].marked_for_removal = True
        return sum

    def remove_free_rolls(self):
        for row in range(self.max_y + 1):
            for col in range(self.max_x + 1):
                if self.grid[row][col].marked_for_removal:
                    self.add_spot(col, row, False)
                    self.grid[row][col].marked_for_removal = False

    def __str__(self):
        val: list[str] = []
        for row in range(self.max_y + 1):
            row_val: list[str] = []
            for col in range(self.max_x + 1):
                if not self.grid[row][col].has_roll:
                    row_val.append(".")
                elif self.grid[row][col].touching_rolls < 4:
                    row_val.append("X")
                else:
                    row_val.append("@")
            val.append("".join(row_val))

        return "\n".join(val)


def solve(input_data: str):
    max_y = input_data.count("\n") - 1
    max_x = len(input_data.split()[0])
    warehouse = Warehouse(max_x, max_y)
    y = 0
    for row in input_data.split():
        x = 0
        for char in row:
            warehouse.add_spot(x, y, char == "@")
            x += 1
        y += 1

    logger.debug(f"\n{warehouse}")
    return warehouse.count_free_rolls()


def bonus(input_data: str):
    max_y = input_data.count("\n") - 1
    max_x = len(input_data.split()[0])
    warehouse = Warehouse(max_x, max_y)
    y = 0
    for row in input_data.split():
        x = 0
        for char in row:
            warehouse.add_spot(x, y, char == "@")
            x += 1
        y += 1

    sum = 0
    while barrels_to_remove := warehouse.count_free_rolls():
        sum += barrels_to_remove
        warehouse.remove_free_rolls()

    return sum
