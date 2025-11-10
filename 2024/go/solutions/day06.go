package solutions

type Direction uint8

const (
	North Direction = iota
	East
	South
	West
)

type Coord struct {
	xpos               uint16
	ypos               uint16
	visited_directions []Direction
}

func Day06Solve(inputFile string) int {
	// Not yet implemented
	return 0
}

func Day06Bonus(inputFile string) int {
	// Not yet implemented
	return 0
}
