package main
 
import (
    "fmt"
)
 
func main() {
		var a,b int
		fmt.Scan(&a)
		fmt.Scan(&b)
		ans := -1

		if a < 10 && b < 10{
			ans = a*b
		}
		fmt.Println(ans)
}