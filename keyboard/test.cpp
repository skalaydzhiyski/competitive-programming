#include <iostream>
#include <string>
#include <map>
#include <utility>

#define N 30
static char board[N] = {
  'q','w','e','r','t','y','u','i','o','p',
  'a','s','d','f','g','h','j','k','l',';',
  'z','x','c','v','b','n','m',',','.','/'
};

void solve(bool direction, const std::string& chars) {
  std::map<char, int> m,m_inv;
  for (int i=0; i<N; ++i) {
    m.insert(std::pair<char, int>(board[i], i));
    m_inv.insert(std::pair<char, int>(i, board[i]));
  }
  for (int i=0; i<chars.size(); ++i) {
    int pos = m[chars[i]] + (direction ? -1 : 1);
    printf("%c", m_inv[pos]);
  }
}

int main(void) {
  std::string direction, chars;
  std::cin >> direction >> chars;
  solve(direction == "R", chars);
  return 0;
}

