#include <iostream>
#include <string>
#include <bitset>
#include <cstdio>

int main(int argc, char** argv) {
  int x, total = 0;
  scanf("%d", &x);
  std::bitset<32> bx(x);
  std::string bx_str = bx.to_string();
  for (int i=0; i<bx_str.size(); ++i) {
    if (bx_str[i] == '1') {
      total++;
    }
  }
  printf("%d", total);
  return 0;
}

