#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Input
int N;


const int MAX = 10001;
bool yoko[MAX] = {0};
bool tate[MAX] = {0};
bool naname[MAX] = {0};
bool naname2[MAX] = {0};
bool table[5001][5001] = {0};

int main() {
	// Step #1. Input
	cin >> N;
  int r, c;

	for (int i = 0; i < N-1; i++) {
    cin >> r >> c;
    table[r-1][c-1] = true;
  }


  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
        yoko[i] |= table[i][j];
        tate[j] |= table[i][j];
        naname[i + (N - j)] |= table[i][j];
        naname2[i + j] |= table[i][j];
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
        if (!yoko[i]
               && !tate[j]
               && !naname[i + (N - j)]
               && !naname2[i + j]) {
                  cout << i+1 << " " << j+1 << endl;
                  return 0;
                }
    }
  }
                  cout << "-1" << endl;
}
