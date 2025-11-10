package solutions

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

type Level uint8
type LevelSlice []Level

type Report struct {
	Levels LevelSlice
	Safe   bool
}

type Input []Report

func (input Input) numOfSafeReports() uint16 {
	count := uint16(0)
	for _, report := range input {
		if report.Safe {
			count++
		}
	}
	return count
}

func removeIndex(s LevelSlice, index int) LevelSlice {
	temp := make(LevelSlice, len(s))
	copy(temp, s)
	if (index + 1) == len(s) {
		return temp[:index]
	}
	if index == 0 {
		return temp[1:]
	}
	return append(temp[:index], temp[index+1:]...)
}

func (levels LevelSlice) isMostlySafe() bool {
	if levels.isSafe() {
		return true
	}

	for i := range levels {
		removedIndex := removeIndex(levels, i)
		if removedIndex.isSafe() {
			return true
		}
	}

	return false
}

func (levels LevelSlice) isSafe() bool {
	ascending := true
	previousLevel := levels[0]
	for i, level := range levels {
		if i == 0 {
			continue
		}
		difference := int16(level) - int16(previousLevel)
		if difference == 0 || math.Abs(float64(difference)) > 3 {
			return false
		}
		if i == 1 {
			// determine order
			ascending = difference > 0
		} else {
			if ascending != (difference > 0) {
				return false
			}
		}
		previousLevel = level
	}
	return true
}

func stringToLevel(strSlice []string) (LevelSlice, error) {
	levelSlice := make(LevelSlice, len(strSlice))
	for i, str := range strSlice {
		num, err := strconv.ParseUint(str, 10, 8)
		if err != nil {
			return nil, err
		}
		levelSlice[i] = Level(num)
	}

	return levelSlice, nil
}

func parseDay02File(filename string, useBonus bool) (Input, error) {
	value := make(Input, 0, 1000)
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		levels, err := stringToLevel(strings.Fields(line))
		if err != nil {
			return nil, err
		}

		// calculate if safe
		safe := levels.isSafe()
		if useBonus {
			safe = levels.isMostlySafe()
		}

		r := Report{
			Levels: levels,
			Safe:   safe,
		}
		value = append(value, r)
	}
	return value, nil
}

func Day02Solve(inputFile string) uint16 {
	input, err := parseDay02File(inputFile, false)
	if err != nil {
		log.Fatal(err)
	}

	return input.numOfSafeReports()
}

func Day02Bonus(inputFile string) uint16 {
	input, err := parseDay02File(inputFile, true)
	if err != nil {
		log.Fatal(err)
	}

	return input.numOfSafeReports()
}
