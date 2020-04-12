#include <iostream>
#include <string>

int main(void) {
  std::string n;
  std::getline(std::cin, n);
  std::string vote;
  std::getline(std::cin, vote);
  std::cout << (vote.find("1") != std::string::npos ? "hard" : "easy") << std::endl;
  return 0;
}


