#include <cstdio>
#include <cstdlib>
#include <iostream>

int f(int x[4], bool flag) {
  int res = 0;
  int new_[4]  = {x[0], x[1], x[2], x[3]};
  while (true) {
    int a = new_[0];
    int b = new_[1];
    int c = new_[2];
    int d = new_[3];
    if (a == 0 and b == 0 and c == 0 and d == 0)
      break;

    if (flag)
      printf("current = [%d,%d,%d,%d]\n", a,b,c,d);

    new_[0] = abs(a-b);
    new_[1] = abs(b-c);
    new_[2] = abs(c-d);
    new_[3] = abs(d-a);
    res += 1;
  }
  return res+1;
}

int main(void) {
  int m = 0;
  int db = 0;
  int dc = 0;
  int upper = 100;
  int x[4] = {0,1,2,4};
  //printf("%d\n", f(x, true));
  int i = 0;
  //for (int i=0; i<upper; ++i) {
    for (int j=0; j<upper; ++j) {
      for (int k=0; k+db<upper; ++k) {
        for (int l=0; l+dc<upper; ++l) {
          int x[4] = {i,j,k,l};
          int fx = f(x, false);
          if (fx > m) {
            m = fx;
            db = abs(j-k);
            dc = abs(k-l);
            printf("current = [%d,%d,%d,%d], fx = %d\n", i,j,k,l, fx);
          }
        }
      }
    }
  //}
}
