package report

import (
	"math"
)

type Level uint8
type LevelSlice []Level

type Report struct {
	Levels LevelSlice
	Safe   bool
}

type Input []Report

func (input Input) NumOfSafeReports() uint16 {
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

func (levels LevelSlice) IsMostlySafe() bool {
	if levels.IsSafe() {
		return true
	}

	for i, _ := range levels {
		removedIndex := removeIndex(levels, i)
		if removedIndex.IsSafe() {
			return true
		}
	}

	return false
}

func (levels LevelSlice) IsSafe() bool {
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
