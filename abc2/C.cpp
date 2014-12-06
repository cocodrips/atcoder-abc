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

#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define REP(i, n)  FOR(i,0,n)

using namespace std;

int main(int argc, const char *argv[]) {
    double x1, x2, x3;
    double y1, y2, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    double s = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2;
    cout << max(s, -s) << endl;

    return 0;
}

