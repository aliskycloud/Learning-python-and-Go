// Temperature Converter: Create a Python program that asks the user for a
// temperature in Celsius and converts it to Fahrenheit using variables to store the values.
package main 
// (0°C × 9/5) + 32 = 32°F

import (
    "fmt"
)

func main() {
    var input float64
    fmt.Println("Enter the tempreture in Celsius: ")
    fmt.Scanln(&input)
    result := (input * 9.5) + 32 
    fmt.Println("tempreture in Fahrenheit is: ", result)
}