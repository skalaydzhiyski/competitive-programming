#include <iostream>
#include <vector>
#include <vector> 
using namespace std;

static vector<vector<int>> a {
	{27, 12, 35, 26},
	{25, 21, 94, 11},
	{19, 96, 43, 56},
	{55, 36, 10, 18},
	{96, 83, 31, 94},
	{93, 11, 90, 99}
};

void solve(vector<int>& res, int start_row, int end_row, int start_col, int end_col) {
  if (start_row > end_row || start_col > end_col) {
    return;
  }
  for (int i=start_col; i<=end_col; ++i) {
    res.push_back(a[start_row][i]);
  }
  for (int i=start_row+1; i<=end_row; ++i) {
    res.push_back(a[i][end_col]);
  }
  for (int i=end_col-1; i>=start_col; --i) {
    if (start_row == end_row) {
      break;
    }
    res.push_back(a[end_row][i]);
  }
  for (int i=end_row-1; i>=start_row+1; --i) {
    if (start_col == end_col) {
      break;
    }
    res.push_back(a[i][start_col]);
  }
  solve(res, start_row+1, end_row-1, start_col+1, end_col-1);
}

int main(int argc, char** argv) {
  vector<int> res;
  solve(res,0,a.size()-1,0,a[0].size()-1);
  for (const auto& n: res) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}

