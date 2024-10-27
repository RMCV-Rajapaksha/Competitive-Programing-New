#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    long long N;
    int K;
    cin >> N >> K;
    
    vector<int> E(K);
    for(int i = 0; i < K; i++) {
        cin >> E[i];
    }
    
    unordered_set<long long> hit_positions;
    
    for(int i = 0; i < K; i++) {
        long long pos = E[i];
        while(pos <= N) {
            hit_positions.insert(pos);
            pos += E[i];
        }
    }
    
    cout << hit_positions.size() << endl;
    
    return 0;
}