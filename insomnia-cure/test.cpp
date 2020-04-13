#include <iostream>
#include <cstdio>

int main(void) {
  // todo: do not forget to handle overcounting!
  int k, l, m, n, d;
  std::cin >> k >> l >> m >> n >> d;
  int onehot[d];
  for (int i=0; i<d; ++i) {
    onehot[i] = 1;
  }
  for (int i=0; i<d; ++i) {
    int idx = i+1;
    if (idx >= k && idx % k == 0) {
      onehot[i] = 0;
    }
    if (idx >= l && idx % l == 0) {
      onehot[i] = 0;
    }
    if (idx >= m && idx % m == 0) {
      onehot[i] = 0;
    }
    if (idx >= n && idx % n == 0) {
      onehot[i] = 0;
    }
  }
  int sum = 0;
  for (int i=0; i<d; ++i) {
    sum += onehot[i];
  }
  printf("%d", d-sum);
  return 0;
}

