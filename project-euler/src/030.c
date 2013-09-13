#include "stdio.h"

#define MAX 100000000
#define LEN 50
#define EXP 5

int main() {

  long count = 0;
  long sum = 0;
  long n = 0;
  int i = 0;
  int j = 0;
  char n_str[LEN]; 
  
  for (n = 2; n < MAX; ++n) {
    for (i = 0; i < LEN; ++i) {
      n_str[i] = '*';
    }
    sprintf(n_str, "%ld", n);

    sum = 0;
    for (i = 0; i < LEN; ++i) {
      if (n_str[i] == '*' || n_str[i] == 0) {
        break;
      }
      long digit = n_str[i] - 48;
      long tmp = 1;
      for (j = 0; j < EXP; ++j) {
        tmp *= digit; 
      }
      sum += tmp;
    }
    if (sum == n) {
      printf("%ld\n", n);
      count += n;
    }

  }

  printf("count: %ld\n", count);

  return 0;
}
