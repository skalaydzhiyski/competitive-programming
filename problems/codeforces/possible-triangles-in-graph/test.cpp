#include <iostream>
#include <bitset>
#include <vector>
#include <cstdio>

using namespace std;

static vector<vector<int>> graph = {
  {1,2},
  {0,2},
  {0,1},
  {0,1}
};

int main(void) {
  int n = graph.size();
  bitset<4> bits[n];
  for (int i=0; i<n; ++i) {
    for (auto& c: graph[i]) {
      bits[i][c] = 1;
    }
  }
  int res = 0;
  for (int i=0; i<n; ++i) {
    for (int j=i+i; j<n; ++j) {
      res += (bits[i] & bits[j]).count();
    }
  }
  cout << res / 3 << endl;
  return 0;
}
 
