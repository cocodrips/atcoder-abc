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
#include <iomanip>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

using namespace std;

int main(int argc, const char * argv[]){
    int N, K;
    vector<double> Rs;
    cin >> N >> K;
    double r = 0;
    REP(i, N){
        cin >> r;
        Rs.push_back(r);
    }

    sort(Rs.begin(), Rs.end());
    double score = 0;

    FOR(i, N - K, N){
        score = (score + Rs[i]) / 2.0;
    }

    printf("%f\n", score);

    return 0;
}

