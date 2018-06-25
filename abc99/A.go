package main

import (
"os"
"bufio"
"strconv"
"fmt"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	n, _ := strconv.Atoi(nextLine())

	if n < 1000 {
		fmt.Println("ABC");
	} else {
		fmt.Println("ABD");
	}

}
