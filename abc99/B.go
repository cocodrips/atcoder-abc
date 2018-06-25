package main

import (
	"os"
	"bufio"
	"strings"
	"strconv"
	"fmt"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	line := strings.Split(nextLine(), " ")
	a, _ := strconv.Atoi(line[0])
	b, _ := strconv.Atoi(line[1])

	n := b - a

	fmt.Println(n*(n-1)/2 - a)
}
