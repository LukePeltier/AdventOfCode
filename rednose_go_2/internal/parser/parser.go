package parser

import (
	"bufio"
	"os"
	"strconv"
	"strings"

	"github.com/lukepeltier/advent_2024/rednose_go_2/internal/report"
)

func stringToLevel(strSlice []string) (report.LevelSlice, error) {
	levelSlice := make(report.LevelSlice, len(strSlice))
	for i, str := range strSlice {
		num, err := strconv.ParseUint(str, 10, 8)
		if err != nil {
			return nil, err
		}
		levelSlice[i] = report.Level(num)
	}

	return levelSlice, nil
}

func InputFromFile(filename string) (report.Input, error) {

	value := make(report.Input, 1000)
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	i := 0

	for scanner.Scan() {
		line := scanner.Text()
		levels, err := stringToLevel(strings.Fields(line))
		if err != nil {
			return nil, err
		}
		// calculate if safe

		r := report.Report{
			Levels: levels,
			Safe:   levels.IsMostlySafe(),
		}
		value[i] = r
		i++
	}
	return value, nil

}
