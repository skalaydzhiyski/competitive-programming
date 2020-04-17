#include <algorithm>
#include <cstdio>
#include <cstdlib>

int main(void) {
  int n, n_cubes[100];
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    scanf("%d", &n_cubes[i]);
  } 
  std::sort(n_cubes, n_cubes+n);
  for (int i=0; i<n; ++i) {
    if (i==n-1) {
      printf("%d", n_cubes[i]);
    } else {
      printf("%d ", n_cubes[i]);
    }
  }
  return 0;
}

