package main

import (
	"log"

	"github.com/lukepeltier/aoc/2024/day2/internal/parser"
)

func main() {
	// f, err := os.OpenFile("output.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	// if err != nil {
	// 	log.Fatalf("Error opening log file: %v", err)
	// }
	// defer f.Close()
	// log.SetOutput(f)
	input, err := parser.InputFromFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("Number of reports: %d\n", len(input))
	log.Printf("Number of safe reports: %d\n", input.NumOfSafeReports())
}
