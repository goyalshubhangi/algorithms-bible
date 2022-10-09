#include <bits/stdc++.h>
using namespace std;
void water(int arr[],int n){
    int left,right,sum = 0;
    for(int i=1;i<n-1;i++){
        left = arr[i];
        for(int j=0;j<i;j++){
            if(arr[j] > left)
                left = max(arr[j],left);
        }
        right = arr[i];
        for(int k=i+1;k<n;k++){
            if(arr[k] > right)
                right = max(arr[k],right);
        }
        sum += (min(left,right) - arr[i]);
    }
    cout<<sum<<endl;
}
int main(){
    int t,n,arr[n];
    cin>>t;
    while(t--){
      cin>>n;
      for(int i=0;i<n;i++)
          cin>>arr[i];
      water(arr,n);
    }
}
