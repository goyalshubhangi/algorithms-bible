/**
 * @author: Jatin Garg 
 * github(https://github.com/jatin-773762)
 **/

#include<bits/stdc++.h>
using namespace std;

/**
 * Test Cases:
 * 1) s= "abcabcbb" 
 *    output: 3 (abc)
 * 2) s="bbbbb"
 *    output: 1 (b)
 **/

int lengthOfLongestSubstring(string s) {

    // check if the string is empty or not
    if(s.empty()){
        return 0;
    }
    // vector to store the presence of character 
    vector<bool> vis(256);
    for(int i=0;i<256;i++){
        vis[i]=false;
    }
    int ans=1;
    int count=0;
    for(int i=0;i<s.length();i++){
        for(int i=0;i<256;i++){
            vis[i]=false;
        }
        vis[s[i]]=true;
        int j;
        for(j=i+1;j<s.length();j++){
            if(vis[s[j]]==false){
                vis[s[j]]=true;
                continue;
            }
            // if the character in substring repeats the loop breaks
            break;
        }   
        // "j-i" is the length of the current substring
        ans = max(ans,j-i);
    }
    return ans;
        
}

int main(){

    
    string s;
    // input string
    cin>>s;

    // prints the length of the longest substring with no repeating characters
    cout<<lengthOfLongestSubstring(s);
}