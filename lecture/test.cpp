#include <iostream>
#include <string>
#include <map>
#include <utility>

int main(void) {
  int n, m;
  std::cin >> n >> m;
  std::string lecture[n], res[n], w1, w2, val;
  std::map<std::string, std::string> dict;
  for (int i=0; i<m; ++i) {
    std::cin >> w1 >> w2;
    val = w1.size() <= w2.size() ? w1 : w2;
    dict.insert(std::make_pair(w1, val));
    dict.insert(std::make_pair(w2, val));
  }
  for (int i=0; i<n; ++i) {
    std::cin >> w1;
    lecture[i] = w1;
  }
  for (int i=0; i<n; ++i) {
    if (i == n-1) {
      std::cout << dict.find(lecture[i])->second;
    } else {
      std::cout << dict.find(lecture[i])->second << " ";
    }
  }
  return 0;
}

