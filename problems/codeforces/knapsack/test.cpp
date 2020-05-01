/* Knapsack is also called the subset sum problem 
 * Given array of N numbers is it possible to get ot sum 0 <= T <= W
 * */
#include <iostream>
#include <bitset>
#include <cstdio>
using namespace std;

#define MAXN 16

int main(void) {
  int n, target;
  scanf("%d %d", &n, &target);
  bitset<MAXN> can(1);
  for (int i=0; i<n; ++i) {
    int x;
    can |= (can<<x);
  }
  printf("%s", can[target] ? "YES" : "NO");
  return 0;
}

