package main
 
import (
		"fmt"
)
 
func main() {
		var a string
		fmt.Scan(&a)
		ans := "Good"
		for i:=0;i<3;i++{
			if a[i:i+1] == a[i+1:i+2]{
				ans = "Bad"
			}
		}
		fmt.Println(ans)
}