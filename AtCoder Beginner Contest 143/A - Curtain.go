package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a)
	fmt.Scan(&b)
	ans := 0
	if a > 2*b {
		ans = a - 2*b
	}
	fmt.Println(ans)
}
