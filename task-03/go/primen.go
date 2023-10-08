package main

import "fmt"

func main() {
    var x int
    fmt.Print("Enter a number: ")
    fmt.Scan(&x)

    for i := 2; i <= x; i++ {
        f := 0
        for j := 2; j < i; j++ {
            if i%j == 0 {
                f = 1
                break
            }
        }
        if f == 0 {
            fmt.Printf("%d : Prime\n", i)
        }
    }
}
