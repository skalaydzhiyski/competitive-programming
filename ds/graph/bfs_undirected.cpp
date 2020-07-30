#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void print_visited(const vector<bool>& visited) {
  for (int i=0; i<visited.size(); ++i) {
    cout << i << ": " << visited[i] << ", ";
  }
  cout << endl;
}

void bfs(const vector<vector<int>>& graph,
         vector<bool>& visited,
         int source)
{
  queue<int> q;
  q.push(source);
  while (!q.empty()) {
    int current = q.front();
    q.pop();
    if (!visited[current]) {
      cout << current << ",";
      visited[current] = 1;
      for (const int child: graph[current]) {
        q.push(child);
      }
    }
  }
}

int main(void) {
  int N = 10;
  vector<bool> visited(N, 0);
  vector<vector<int>> graph(N, vector<int>{});
  vector<pair<int, int>> edges {
    {0,1},{1,2},{1,3},{1,4},{2,5},{2,6},{3,8},{3,9},{6,7}
  };
  for (auto e: edges) {
    graph[e.first].push_back(e.second);
    graph[e.second].push_back(e.first);
  }
  for (int i=0; i<N; ++i) {
    cout << i << ": ";
    for (auto node: graph[i]) {
      cout << node << ",";
    }
    cout << endl;
  }
  //cout << "---------------- DFS -----------------" << endl;
  //dfs(graph, visited, 0);
  //cout << endl;
  cout << "---------------- BFS -----------------" << endl;
  bfs(graph, visited, 0);
  cout << endl;
  return 0;
}
