#include <bits/stdc++.h>
using namespace std;
 
unsigned GetDigit(unsigned num){
    return std::to_string(num).length();
}

int main() {
    long long a;
    cin >> a;
    
    long long b;
    cin >> b;

    long long x;
    cin >> x;

    long long i;

    long long o = GetDigit(x);
    long long price = 0;
    while(true) {
      price =  a*i + b*o;
      if(x <= price || i == 1000000000){
        break;
      }
      i++;
    }
    cout << i << endl;
}