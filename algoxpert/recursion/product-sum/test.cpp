#include <iostream>
#include <vector>
#include <any>
using namespace std;

int productSum(vector<any> a, int multi=1) {
  int n = a.size();
  int res = 0;
  for (const auto& item: a) {
    if (item.type() == typeid(vector<int>)) {
      res += productSum(any_cast<vector<any>>(item), multi+1);
    } else {
      res += any_cast<int>(item);
    }
  }
  return res;
}

int main(void) {
  vector<any> input;
  input.push_back(5);
  input.push_back(2);
  input.push_back(vector<int>{7, -1});
  input.push_back(3);
  input.push_back(vector<any>{6, vector<int>{-13, 8}, 4});
  cout << productSum(input) << endl;
  return 0;
}

