
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
       int count=0,countfinal=0,flag=0, pos;
        vector<char> v;
        
        for(int i=0;i<s.size();i++)
        {
            if(v.size()==0)
            {
                v.push_back(s[i]);
                count++;
            }
            else
            {
                char ch=s.at(i);
                for(int j=0;j<v.size();j++)
                {
                    if(v[j]==ch)
                    {
                        flag=1;
                       
                        pos=j;
                         break;
                    } 
                    else
                    {
                        flag=2;
                    }
                }
                
                if(flag==1)
                {
                    if(count>=countfinal)
                    {
                        countfinal=count;
                       
                    }
                    v.erase(v.begin(),v.begin()+(pos+1));
                     count=count-(pos+1);
                    v.push_back(ch);
                    count++;
                }
                else
                {
                    v.push_back(ch);
                    count++;
                }
            }            
        }
        if(countfinal>count)
        return countfinal;
        else
            return count;
    }
};