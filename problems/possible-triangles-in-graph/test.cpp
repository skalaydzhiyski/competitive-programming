#include <iostream>
#include <sstream>
#include <bitset>
#include <vector>
#include <string>
#include <utility>
#include <map>
#include <cstdio>

using namespace std;

void input(map<int, vector<int>>& g, int n);
void disp(map<int, vector<int>>& g);

int main(void) {
  int n;
  scanf("%d", &n);
  map<int, vector<int>> g;
  input(g, n);

  return 0;
}

void disp(map<int, vector<int>>& g) {
  for (auto& c : g) {
    cout << c.first << ": ";
    for (auto& n : c.second) {
      cout << n << ",";
    }
    cout << endl;
  }
}

void input(map<int, vector<int>>& g, int n) {
  for (int i=0; i<n; ++i) {
    int c;
    cin >> c;
    // get connections
    string s;
    getline(cin, s);
    istringstream iss(s);
    vector<int> conn;
    char ch;
    while (iss >> ch) {
      conn.push_back(ch - '0');
    }
    g.insert(make_pair(c, conn));
  }
}


