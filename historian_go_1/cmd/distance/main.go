package main

import (
	"github.com/lukepeltier/advent_2024/historian_go_1/internal/parser"
	"log"
)

func abs(n int64) uint64 {
	if n < 0 {
		return uint64(-n)
	}
	return uint64(n)
}

func main() {
	leftList, rightList, err := parser.ParseFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	listLength := len(leftList)
	distanceSum := uint64(0)
	for i := 0; i < listLength; i++ {
		distance := leftList[i] - rightList[i]
		distanceSum += abs(distance)

	}

	log.Printf("Total distance: %d", distanceSum)
}
