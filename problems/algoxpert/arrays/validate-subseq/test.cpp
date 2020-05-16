#include <iostream>
#include <vector>
using namespace std;

bool solve(const vector<int>& a, const vector<int>& seq) {
  int current = 0;
  for (int i=0; i<a.size(); ++i) {
    if (a[i] == seq[current]) {
      current++;
    }
  }
  return current == seq.size();
}

int main(void) {
  vector<int> a{5, 1, 22, 25, 6, -1, 8, 10};
  vector<int> seq{1,6,-1,10};
  cout << solve(a, seq) << endl;
  return 0;
}

