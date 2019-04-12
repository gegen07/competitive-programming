#include <iostream>

using namespace std;

int bruteForce(int *arr, int length) {
  int best = 0;
  
  for(int i = 0; i < length; i++) {
    for(int j = i; j < length; j++) {
      int sum = 0;
      for(int k = i; k <= j; k++) {
        sum += arr[k]; 
      }
      best = max(best, sum);
    }
  }  
  return best;
}

int bruteForceFast(int *arr, int length) {
  int best = 0;

  for(int i = 0; i < length; i++) {
    int sum = 0;
    for(int j = i; i < length; i++) {
      sum += arr[j];
      best = max(best, sum);
    }
  }
  return best;
}

int kadaneAlgorithm(int *arr, int length) {
  int best = 0;
  int sum = 0;

  for(int k = 0; k < length; k++) {
    sum = max(arr[k], sum+arr[k]);
    best = max(best, sum);
  }

  return best;
}

int main () {
  int arr[10] = {-1,2,4,-3,2,5,-5, 2};

  cout << kadaneAlgorithm(arr, 10);

  return 0;
}