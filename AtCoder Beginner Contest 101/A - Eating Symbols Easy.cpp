/**
 * code generated by JHelper
 * More info: https://github.com/AlexeyDmitriev/JHelper
 * @author
 */

#include <iostream>
#include <fstream>

#include <bits/stdc++.h>


using namespace std;
typedef long long unsigned int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))

class AEatingSymbolsEasy {
public:
void solve(std::istream& cin, std::ostream& cout) {
    //int a,b;
    int ans = 0;
    //string ans = "";
    string a;
    cin >> a;
    int count;
    for(int i=0;i<4;i++){
        if(a[i]=='+') { ans++; }
        else{ ans--; }
    }

    cout << ans << endl;
}
};


int main() {
	AEatingSymbolsEasy solver;
	std::istream& in(std::cin);
	std::ostream& out(std::cout);
	solver.solve(in, out);
	return 0;
}
