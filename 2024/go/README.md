# Advent of Code 2024 - Go Solutions

This folder contains Go solutions for Advent of Code 2024.

## Structure

```
go/
├── aoc              # Single binary for running actual puzzle inputs
├── go.mod           # Go module definition
├── main.go          # CLI entry point
└── solutions/       # Day solutions and tests
    ├── day01.go
    ├── day01_test.go
    ├── day02.go
    ├── day02_test.go
    └── ...
```

## Running Tests

Tests use example inputs from `../inputs/examples/` and validate against known expected outputs.

```bash
# Run all tests
go test ./solutions

# Run tests with verbose output
go test ./solutions -v

# Run specific day's tests
go test ./solutions -run TestDay01
go test ./solutions -run TestDay02
```

## Running Solutions

The `aoc` binary runs solutions against actual puzzle inputs from `../inputs/inputs/`.

```bash
# Build the binary
go build -o aoc

# Run a specific day
./aoc -d 1

# Run bonus/part 2
./aoc -d 1 --bonus

# Show help
./aoc --help
```

### Available Flags

- `-d` or `--day <number>`: Day number (required)
- `--bonus`: Run part 2/bonus solution

## Adding a New Day

1. Create `solutions/dayXX.go` with these functions:
   ```go
   package solutions

   func DayXXSolve(inputFile string) <return_type> {
       // Part 1 implementation
       return result
   }

   func DayXXBonus(inputFile string) <return_type> {
       // Part 2 implementation
       return result
   }
   ```

2. Create `solutions/dayXX_test.go`:
   ```go
   package solutions

   import "testing"

   func TestDayXXSolve(t *testing.T) {
       inputFile := "../../inputs/examples/XX.txt"
       expected := <expected_value>

       result := DayXXSolve(inputFile)

       if result != expected {
           t.Errorf("DayXXSolve() = %v; want %v", result, expected)
       }
   }

   func TestDayXXBonus(t *testing.T) {
       inputFile := "../../inputs/examples/XX.txt"
       expected := <expected_value>

       result := DayXXBonus(inputFile)

       if result != expected {
           t.Errorf("DayXXBonus() = %v; want %v", result, expected)
       }
   }
   ```

3. Add the day to the switch statement in `main.go`:
   ```go
   case XX:
       if *bonus {
           result := solutions.DayXXBonus(inputFile)
           fmt.Printf("Day XX Bonus - Result: %v\n", result)
       } else {
           result := solutions.DayXXSolve(inputFile)
           fmt.Printf("Day XX - Result: %v\n", result)
       }
   ```

4. Add example input to `../inputs/examples/XX.txt`
5. Add actual input to `../inputs/inputs/XX.txt`

