#include <iostream>
using namespace std;

#define V 5

int minDistance(int dist[], bool visited[]) {
    int min = 9999, minIndex;

    for(int i = 0; i < V; i++) {
        if(!visited[i] && dist[i] < min) {
            min = dist[i];
            minIndex = i;
        }
    }

    return minIndex;
}

int main() {

    int graph[V][V] = {
        {0, 10, 0, 5, 0},
        {0, 0, 1, 2, 0},
        {0, 0, 0, 0, 4},
        {0, 3, 9, 0, 2},
        {7, 0, 6, 0, 0}
    };

    int dist[V];
    bool visited[V];

    for(int i = 0; i < V; i++) {
        dist[i] = 9999;
        visited[i] = false;
    }

    dist[0] = 0;

    for(int count = 0; count < V - 1; count++) {

        int u = minDistance(dist, visited);
        visited[u] = true;

        for(int v = 0; v < V; v++) {

            if(!visited[v] &&
               graph[u][v] &&
               dist[u] != 9999 &&
               dist[u] + graph[u][v] < dist[v]) {

                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    cout << "Vertex\tDistance from Source\n";

    for(int i = 0; i < V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }

    return 0;
}