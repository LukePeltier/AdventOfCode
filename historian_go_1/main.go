package main

import (
	"bufio"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func abs(n int64) uint64 {
	if n < 0 {
		return uint64(-n)
	}
	return uint64(n)
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var leftList []int64
	var rightList []int64

	for scanner.Scan() {
		line := scanner.Text()
		items := strings.Fields(line)

		leftItem, err := strconv.ParseInt(items[0], 10, 64)
		if err != nil {
			log.Fatal(err)
		}

		leftList = append(leftList, int64(leftItem))

		rightItem, err := strconv.ParseInt(items[1], 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		rightList = append(rightList, int64(rightItem))
	}
	slices.Sort(leftList)
	slices.Sort(rightList)

	listLength := len(leftList)
	distanceSum := uint64(0)
	for i := 0; i < listLength; i++ {
		distance := leftList[i] - rightList[i]
		distanceSum += abs(distance)

	}

	log.Printf("Total distance: %d", distanceSum)
}
