#include <iostream>
#include <cstdio>
#include <string>

int main(void) {
  int n;
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    std::string word;
    std::cin >> word;
    auto size = word.size();
    std::string res = size <= 10 ? word : word[0] + std::to_string(word.size() - 2) + word[word.size()-1];
    std::cout << res << std::endl;
  }
  return 0;
}

