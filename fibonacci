#include <stdio.h>

// Function to calculate the Fibonacci number at a given index
int fibonacci(int n) {
  if (n <= 1) {
    return n;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

// Driver function
int main() {
  int n;
  printf("Enter the number of terms: ");
  scanf("%d", &n);

  // Print the first n Fibonacci numbers
  for (int i = 0; i < n; i++) {
    printf("%d ", fibonacci(i));
  }

  printf("\n");
  return 0;
}
