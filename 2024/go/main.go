package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/lukepeltier/AdventOfCode/2024/go/solutions"
)

func getInputFile(day int) string {
	return fmt.Sprintf("../inputs/inputs/%02d.txt", day)
}

func main() {
	day := flag.Int("day", 0, "Day number (required)")
	dayShort := flag.Int("d", 0, "Day number (short form)")
	bonus := flag.Bool("bonus", false, "Run the bonus solution")

	flag.Parse()

	// Support both --day and -d
	selectedDay := *day
	if selectedDay == 0 {
		selectedDay = *dayShort
	}

	if selectedDay == 0 {
		fmt.Println("Error: --day or -d flag is required")
		flag.Usage()
		os.Exit(1)
	}

	inputFile := getInputFile(selectedDay)

	// Check if input file exists
	if _, err := os.Stat(inputFile); os.IsNotExist(err) {
		log.Fatalf("Input file does not exist: %s", inputFile)
	}

	switch selectedDay {
	case 1:
		if *bonus {
			result := solutions.Day01Bonus(inputFile)
			fmt.Printf("Day 1 Bonus - Score: %d\n", result)
		} else {
			result := solutions.Day01Solve(inputFile)
			fmt.Printf("Day 1 - Total distance: %d\n", result)
		}
	case 2:
		if *bonus {
			result := solutions.Day02Bonus(inputFile)
			fmt.Printf("Day 2 Bonus - Safe reports (with Problem Dampener): %d\n", result)
		} else {
			result := solutions.Day02Solve(inputFile)
			fmt.Printf("Day 2 - Safe reports: %d\n", result)
		}
	case 3:
		if *bonus {
			result := solutions.Day03Bonus(inputFile)
			fmt.Printf("Day 3 Bonus - Result: %d\n", result)
		} else {
			result := solutions.Day03Solve(inputFile)
			fmt.Printf("Day 3 - Result: %d\n", result)
		}
	default:
		log.Fatalf("Day %d not implemented yet", selectedDay)
	}
}
