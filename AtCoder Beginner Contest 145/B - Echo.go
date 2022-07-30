package main
 
import (
    "fmt"
)
 
func main() {
		var s, ans string
		var n,l int
		fmt.Scan(&n)
		fmt.Scan(&s)
		
		l = n/2
		if n%2 == 0{
			if s[:l] == s[l:]{
				ans = "Yes"
			}else{
				ans = "No"
			}
		}else{
			ans = "No"
		}
		fmt.Println(ans)
}