#include <iostream>

int main(void) {
  long long n, pos;
  std::cin >> n >> pos;
  if (pos == 1) {
    printf("1");
    return 0;
  }
  // n even
  long long len_odds = n % 2 == 0 ? n/2 : n/2 + 1;
  // compute evens
  if (pos > len_odds) {
    long long n_steps = pos - len_odds;
    std::cout << 2 * n_steps;
  }
  // compute odds
  else {
    long long n_steps = pos;
    std::cout << 2 * n_steps - 1;
  }
  return 0;
}

