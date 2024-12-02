package parser

import (
	"bufio"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

var rightListCache map[int64]uint16 = make(map[int64]uint16)

func ParseFile(name string) ([]int64, []int64, error) {
	file, err := os.Open(name)
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
			return nil, nil, err
		}

		leftList = append(leftList, int64(leftItem))

		rightItem, err := strconv.ParseInt(items[1], 10, 64)
		if err != nil {
			return nil, nil, err
		}
		rightList = append(rightList, rightItem)
		rightListCache[rightItem] += 1
	}
	slices.Sort(leftList)
	slices.Sort(rightList)
	return leftList, rightList, nil
}

func GetRightCacheNum(entry int64) uint16 {
	if value, ok := rightListCache[entry]; ok {
		return value
	}
	return 0
}
