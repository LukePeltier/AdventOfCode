package solutions

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

func parseDay01File(filename string) ([]int64, []int64, map[int64]uint16, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, nil, nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var leftList []int64
	var rightList []int64
	rightListCache := make(map[int64]uint16)

	for scanner.Scan() {
		line := scanner.Text()
		items := strings.Fields(line)

		leftItem, err := strconv.ParseInt(items[0], 10, 64)
		if err != nil {
			return nil, nil, nil, err
		}
		leftList = append(leftList, int64(leftItem))

		rightItem, err := strconv.ParseInt(items[1], 10, 64)
		if err != nil {
			return nil, nil, nil, err
		}
		rightList = append(rightList, rightItem)
		rightListCache[rightItem] += 1
	}

	slices.Sort(leftList)
	slices.Sort(rightList)

	return leftList, rightList, rightListCache, nil
}

func Day01Solve(inputFile string) uint64 {
	leftList, rightList, _, err := parseDay01File(inputFile)
	if err != nil {
		log.Fatal(err)
	}

	listLength := len(leftList)
	distanceSum := uint64(0)
	for i := 0; i < listLength; i++ {
		distance := leftList[i] - rightList[i]
		distanceSum += abs(distance)
	}

	return distanceSum
}

func Day01Bonus(inputFile string) uint64 {
	leftList, _, rightListCache, err := parseDay01File(inputFile)
	if err != nil {
		log.Fatal(err)
	}

	score := uint64(0)

	for _, v := range leftList {
		if count, ok := rightListCache[v]; ok {
			score += uint64(v) * uint64(count)
		}
	}

	return score
}
