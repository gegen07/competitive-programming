package main

import (
	"fmt"
	"math"
)

func isValid(mat [][]int64, num int64) rune {
	for i := int(num)-2; i >= 0; i-- {
		if math.Sqrt(float64(mat[i][0] * mat[i][0] + mat[i][1] * mat[i][1] + mat[i][2] * mat[i][2])) < 
		math.Sqrt(float64(mat[i+1][0] * mat[i+1][0] + mat[i+1][1] * mat[i+1][1] + mat[i+1][2] * mat[i+1][2])) {
			
		} else {
			return 'N'
		}
	}
	return 'S'
}

func main() {
	var num int64

	fmt.Scanf("%d", &num)

	mat := make([][]int64, num)
	for i := range mat {
		mat[i] = make([]int64, 3)
	}
 
	for i := 0; i < int(num); i++ {
		fmt.Scanln(&mat[i][0], &mat[i][1], &mat[i][2])
	}

	fmt.Println(string(isValid(mat, num)))

}