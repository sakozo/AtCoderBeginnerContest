#include <bits/stdc++.h>


using namespace std;
typedef long long unsigned int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))

class BMinorChange {
public:
void solve(std::istream& cin, std::ostream& cout) {
    string a,b;
    int ans = 0;
    cin >> a;
    cin >> b;

    for(int i =0;i<a.size();i++){
        if(a[i] != b[i]){
            ans++;
        }
    }

    cout << ans << endl;
}
};
