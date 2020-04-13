#include <iostream>
#include <string>
#include <cstdio>
#include <bitset>

#define MAX_BIT_LENGTH 128

int main(void) {
  std::string s1, s2, bin_res;
  std::cin >> s1 >> s2;
  long long resint = std::stol(s1, nullptr, 2) ^ std::stol(s2, nullptr, 2);
  int offset = MAX_BIT_LENGTH - s1.size();
  std::string res = std::bitset<MAX_BIT_LENGTH>(resint).to_string().substr(offset, MAX_BIT_LENGTH);
  printf("%s", res.c_str());
  return 0;
}

