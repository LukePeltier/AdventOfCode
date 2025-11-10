package solutions

import (
	"testing"
)

func TestDay03Solve(t *testing.T) {
	inputFile := "../../inputs/examples/03.txt"
	expected := 0 // Not yet implemented

	result := Day03Solve(inputFile)

	if result != expected {
		t.Errorf("Day03Solve() = %d; want %d", result, expected)
	}
}

func TestDay03Bonus(t *testing.T) {
	inputFile := "../../inputs/examples/03.txt"
	expected := 0 // Not yet implemented

	result := Day03Bonus(inputFile)

	if result != expected {
		t.Errorf("Day03Bonus() = %d; want %d", result, expected)
	}
}
