#include <iostream>
#include <vector>
using namespace std;

void dfs(const vector<vector<int>>& g, int s) {
  cout << s << ",";
  for (const int c: g[s]) {
    dfs(g, c);
  }
}

int main(void) {
  int N = 10;
  vector<vector<int>> graph(N, vector<int>{});

  vector<pair<int, int>> edges {
    {0,1},{1,2},{1,3},{1,4},{2,5},{2,6},{3,8},{3,9},{6,7}
  };
  for (auto e: edges) {
    graph[e.first].push_back(e.second);
  }

  for (int i=0; i<N; ++i) {
    cout << i << ": ";
    for (auto node: graph[i]) {
      cout << node << ",";
    }
    cout << endl;
  }
  cout << "---------------- DFS -----------------" << endl;
  dfs(graph, 0);
  cout << endl;
  return 0;
}
