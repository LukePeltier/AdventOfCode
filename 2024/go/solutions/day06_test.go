package solutions

import (
	"testing"
)

func TestDay06Solve(t *testing.T) {
	inputFile := "../../inputs/examples/06.txt"
	expected := 41

	result := Day06Solve(inputFile)

	if result != expected {
		t.Errorf("Day06Solve() = %d; want %d", result, expected)
	}
}

func TestDay06Bonus(t *testing.T) {
	inputFile := "../../inputs/examples/06.txt"
	expected := 6 // Not yet implemented

	result := Day06Bonus(inputFile)

	if result != expected {
		t.Errorf("Day06Bonus() = %d; want %d", result, expected)
	}
}
