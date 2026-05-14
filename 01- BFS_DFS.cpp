#include <iostream>
using namespace std;

class Graph{
    int vertices;
    vector<int> *adj;
    public:
        Graph(int v){
            vertices = v;
            adj = new vector<int>[v];
        }

        void addEdge(int u, int v){
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        void DFS(int v, vector<bool> &visited){
            visited[v] = true;
            cout<<v<<" ";
            for(int a:adj){
                if(!visited[a]){
                     DFS(a, visited);
                }
            }
        }

        void BFS(int v){
            vector<bool> visited(v, false);
            queue<int> q;

            visited[v]=true;
            queue.push(v);
            while(!q.empty()){
                int vv = q.front();
                q.pop();
                cout<< vv <<" ";
                for(int a : adj){
                    if(!visited[a]){
                        visited[a] = true;
                        q.push(a);
                    }
                }
            }
        }
}

int main(){
    Graph g(5);
    vector<int> visited(5, false);

    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,3);
    g.addEdge(2,4);
    g.addEdge(3,4);
    
    cout<<"DFS: ";
    DFS(0, visited);

    cout<<endl;
    cout<<"BFS: ";
    BFS(0);

    return 0;
}
