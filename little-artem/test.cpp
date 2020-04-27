#include <vector>
#include <cstdio>

using namespace std;

void disp(vector<vector<bool>> matrix) {
  for (int i=0; i<matrix.size(); ++i) {
    for (int j=0; j<matrix[i].size(); ++j) {
      printf("%c", matrix[i][j] ? 'W':'B');
    }
    printf("\n");
  }
}

void solve(vector<vector<bool>>& m) {
  m[0][0] = 1;
}

int main(void) {
  int t;
  scanf("%d", &t);
  for (int i=0; i<t; ++i) {
    int m, n;
    scanf("%d %d", &m, &n);
    vector<vector<bool>> matrix(m, vector<bool>(n));
    solve(matrix);
    disp(matrix);
  }
  return 0;
}

