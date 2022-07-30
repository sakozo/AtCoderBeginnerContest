package main

import (
	"strings"
		"fmt"
)

func main() {
		var a string
		fmt.Scan(&a)
		ans := "Yes"
		for i:=0;i<4;i++{
			if strings.Count(a, a[i:i+1]) != 2{
				ans = "No"
			}
		}
			fmt.Println(ans)
}
