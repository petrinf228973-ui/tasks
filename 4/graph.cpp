#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <limits>
using namespace std;

typedef pair<int,string> pis;

map<string, vector<pair<string,int>>> g = {
    {"A", {{"B",1},{"C",4}}},
    {"B", {{"A",1},{"C",2},{"D",5}}},
    {"C", {{"A",4},{"B",2},{"D",1}}},
    {"D", {{"B",5},{"C",1}}}
};

map<string,int> dijkstra(string start) {
    map<string,int> dist;
    for (auto &p : g) dist[p.first] = INT_MAX;
    dist[start] = 0;
    priority_queue<pis, vector<pis>, greater<pis>> pq;
    pq.push({0,start});
    while(!pq.empty()) {
        auto [cd,u] = pq.top(); pq.pop();
        if (cd > dist[u]) continue;
        for (auto &edge : g[u]) {
            string v = edge.first;
            int w = edge.second;
            int nd = dist[u] + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                pq.push({nd,v});
            }
        }
    }
    return dist;
}

int main() {
    auto res = dijkstra("A");
    for (auto &p : res) cout << p.first << ": " << p.second << endl;
}
