#include <cstdio>

int main(void) {
  int n;
  int lucky[] {4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777};
  scanf("%d", &n);
  bool res = false;
  for (int i=0; i<sizeof(lucky)/sizeof(int); ++i) {
    res = !(n % lucky[i]);
    if (res)
      break;
  }
  printf("%s", res ? "YES" : "NO");
  return 0;
}

