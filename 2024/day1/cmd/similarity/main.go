package main

import (
	"log"

	"github.com/lukepeltier/aoc/2024/day1/internal/parser"
)

func main() {
	leftList, _, err := parser.ParseFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	score := uint64(0)

	for _, v := range leftList {
		score += uint64(v) * uint64(parser.GetRightCacheNum(v))
	}

	log.Printf("Score: %d\n", score)
}
