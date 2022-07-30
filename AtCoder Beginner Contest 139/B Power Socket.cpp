#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A,B;
  // 変数aで入力を受け取る
  cin >> A;
  cin >> B;
  int sum = 1;
  int count =0;

  //cout << B;

  for(int i =0;true;i++){
      sum = sum + A-1;
      //cout << i;
      if(sum >= B){
          //cout << sum;
          count = i;
          break;
      }
  }
  if(B == 1){
      cout << 0 << endl;
  }else{
      cout << count+1 << endl;
  }
}