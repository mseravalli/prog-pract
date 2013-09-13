#include "stdio.h"

#define true 1
#define false 0

const int DGT = 10;
const int LEN = 32;
const int MAX = 10000;

int main(){

  long a = 0;
  long b = 0;
  long c = 0;
  long sum = 0;
  int i = 0;
  char res_str[LEN];
  char check[DGT];
  
  char all_check = true;

  for (i = 0; i < DGT; ++i) {
    check[i] = 0;
  }

  for (a = 0; a < MAX; ++a) {
    for (b = 0; b < MAX; ++b) {
      // reset string result
      for (i = 0; i < LEN; ++i) {
        res_str[i] = '\0';
      }

      c = a * b;
      sprintf(res_str, "%ld%ld%ld", a, b, c);
      
      // store the used numbers
      for (i = 0; res_str[i] != '\0'; ++i) {
        check[res_str[i] - 48] += 1; 
      }

      // check if all numbers are used and clean the array for the next cycle
      all_check = true;
      all_check &= (check[0]==0);
      check[0] = 0;
      for (i = 1; i < DGT; ++i) {
        all_check &= (check[i]==1);
        check[i] = 0;
      }

      if (all_check) {
        printf("%ld * %ld = %ld\n", a, b, c);
        sum += c;
      }
    }
  }

  printf("%ld\n", sum);

  return 0;
}
