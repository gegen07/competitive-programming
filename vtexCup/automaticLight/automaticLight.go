package main

import (
	"fmt"
)

func automaticLight(tin, tout []int64, numFunc int64) int64 {
	lightTime := (tout[0] - tin[0])
	interval := [2]int64{tin[0], tout[0]}

	for index := 1; index < int(numFunc); index++ {
		if tin[index] > interval[1] {
			lightTime -= tout[index] - tin[index]
			interval[0] = tin[index]
			interval[1] = lightTime*int64(index)
		} else if tin[index] < interval[1] && tout[index] > interval[1] {	
			lightTime -= tout[index] - interval[1]
			interval[1] = lightTime*int64(index+1) 
		}
	}

	return lightTime
}

func main() {
	var numFunc int64
	
	fmt.Scanln(&numFunc)

	tin := make([]int64, numFunc)
	tout := make([]int64, numFunc)

	for index := 0; index < int(numFunc); index++ {
		var tempIn, tempOut int64

		fmt.Scanln(&tempIn, &tempOut)
		
		tin[index] = tempIn
		tout[index] = tempOut
	}
	
	fmt.Println(automaticLight(tin, tout, numFunc))

}
