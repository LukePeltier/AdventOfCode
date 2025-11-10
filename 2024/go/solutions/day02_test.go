package solutions

import (
	"testing"
)

func TestDay02Solve(t *testing.T) {
	inputFile := "../../inputs/examples/02.txt"
	expected := uint16(2)

	result := Day02Solve(inputFile)

	if result != expected {
		t.Errorf("Day02Solve() = %d; want %d", result, expected)
	}
}

func TestDay02Bonus(t *testing.T) {
	inputFile := "../../inputs/examples/02.txt"
	expected := uint16(4)

	result := Day02Bonus(inputFile)

	if result != expected {
		t.Errorf("Day02Bonus() = %d; want %d", result, expected)
	}
}
