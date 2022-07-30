#include <bits/stdc++.h>
using namespace std;
 typedef long long unsigned int ll;
int main() {
    int N;
    cin >> N;

    map<int, int> m;
    //++m[0]; // 初期値 0

    int num;

    for(int i=1;i<N+1;i++){
        cin >> num;
        m[num] = i;
    }

    for(int i=1;i<N+1;i++){
        cout << m[i] << " ";
    }

    cout << endl;
}
