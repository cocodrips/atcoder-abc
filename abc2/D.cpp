#include <iostream>
#include <map>
#include <string> 
#include <vector>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include <tuple>
#include <stack>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

using namespace std;

int main(int argc, const char * argv[]){
    int N = 0, M;
    cin >> N >> M;
    std::vector<int> nets(N);


    for (int i = 0; i < M; ++i){
        int v, d;
        cin >> v >> d;
        nets[v] += 2 << d;
    }

    int maximum = 0;
    for (int i = 0; i < 2 << N; ++i){
        cout << __builtin_popcount(i) << endl;
    }
    return 0;
}

// int count(){


// }

