#include <bits/stdc++.h>


using namespace std;
typedef long long unsigned int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))

class CTsundoku {
public:
void solve(std::istream& cin, std::ostream& cout) {
    ll n,m,k;
    ll a[200001]={0},b[200001]={0};
    ll ans = 0;
    cin >> n >> m >> k;
    for(ll i=0;i<n;i++) cin >> a[i];
    for(ll i=0;i<m;i++) cin >> b[i];
    ll ai = 0;
    ll bi = 0;
    for(ll i=0; true; i++){
        ll tmp;
        if(a[ai] == 0 && b[bi] == 0) {
            break;
        }else if (a[ai] == 0){
            tmp = b[bi];
            bi++;
        }else if (b[bi] == 0){
            tmp = a[ai];
            ai++;
        }
        else if(a[ai] == b[bi]){
            bool flg = true;
            ll j = 1;
            while(flg) {
                if(a[ai+j]==b[bi+j]) {
                    j++;
                    continue;
                }
                else if(a[ai+j] == 0){
                    tmp = b[bi];
                    bi++;
                    flg = false;
                }
                else if(b[bi+j] == 0){
                    tmp=a[ai];
                    ai++;
                    flg = false;
                }
                else if(a[ai+j]<b[bi+j]) {
                    tmp=a[ai];
                    ai++;
                    flg = false;
                }else {
                    tmp = b[bi];
                    bi++;
                    flg = false;
                }
            }
        }
        else if(a[ai] <b[bi]){
            tmp = a[ai];
            ai++;
        }
        else{
            tmp = b[bi];
            bi++;
        }
        if (k>=tmp){
            k -=tmp;
            ans++;
        }else{
            break;
        }
    }

    //    ll n,m,k;
//    vector<ll> a,b;
//    ll ans = 0;
//    cin >> n >> m >> k;
//    for(ll i=0;i<n;i++){
//        ll tmp;
//        cin >> tmp;
//        a.push_back(tmp);
//    }
//    for(ll i=0;i<m;i++){
//        ll tmp;
//        cin >> tmp;
//        b.push_back(tmp);
//    }
//    for(ll i =0; i<10000000000;i++){
//        ll tmp;
//            if (a.size()==0 && b.size()==0){
//                break;
//            }else if(a.size()==0){
//                tmp = b[0];
//                b.erase(b.begin());
//            }else if(b.size()==0){
//                tmp = a[0];
//                a.erase(a.begin());
//            }
//            else if(a[0] <= b[0]){
//                tmp = a[0];
//                a.erase(a.begin());
//            } else{
//                tmp = b[0];
//                b.erase(b.begin());
//            }
//        if(k>=tmp){
//            k -= tmp;
//            ans++;
//        }else{
//            break;
//        }
//    }
    cout << ans << endl;
}
};
