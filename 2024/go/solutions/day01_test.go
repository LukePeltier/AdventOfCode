package solutions

import (
	"testing"
)

func TestDay01Solve(t *testing.T) {
	inputFile := "../../inputs/examples/01.txt"
	expected := uint64(11)

	result := Day01Solve(inputFile)

	if result != expected {
		t.Errorf("Day01Solve() = %d; want %d", result, expected)
	}
}

func TestDay01Bonus(t *testing.T) {
	inputFile := "../../inputs/examples/01.txt"
	expected := uint64(31)

	result := Day01Bonus(inputFile)

	if result != expected {
		t.Errorf("Day01Bonus() = %d; want %d", result, expected)
	}
}
