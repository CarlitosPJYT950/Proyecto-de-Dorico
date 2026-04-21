package main

import "fmt"

func main() {
    var numbers[3] int
    numbers[0] = 21
    numbers[1] = 2
    numbers[2] = 3
    fmt.Println(numbers[2])

    favNums := [4] int {50, 25, 30, 33}
    fmt.Println(favNums[1])
}