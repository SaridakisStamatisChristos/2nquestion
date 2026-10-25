#include <bits/stdc++.h>
using namespace std;using E=pair<int,int>;
int main(int argc,char**argv){int n=atoi(argv[1]);if(n<3||n>5)return 2;vector<E>a;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)a.push_back({i,j});int m=a.size(),all=(1<<n)-1;long long count=0,intersect=0,min3=0;int maximalExtremeMin=0;do{
 int degree[8]={};
 for(int skip=0;skip<m;skip++){
  int info[8];for(int j=0;j<n;j++)info[j]=1<<j;
  for(int t=0;t<m;t++)if(t!=skip){auto[u,v]=a[t];info[u]|=info[v];info[v]=info[u];}
  bool isforced=0;for(int i=0;i<n;i++)if(info[i]!=all){isforced=true;break;}
  if(isforced){auto[u,v]=a[skip];degree[u]++;degree[v]++;}
 }
 auto [u,v]=a.front();auto [x,y]=a.back();int mini=min({degree[u],degree[v],degree[x],degree[y]});maximalExtremeMin=max(maximalExtremeMin,mini);
 if(u==x||u==y||v==x||v==y){intersect++;int s=u==x||u==y?u:v; if(degree[s]>2){cout<<"SHARED_FAIL order="<<count<<"\n";return 2;}}
 if(mini>=3){min3++;cout<<"FOUR_EXTREME_FAIL order="<<count<<"\n";for(auto [u,v]:a)cout<<u<<","<<v<<" ";cout<<"\n";return 3;}
 count++;
}while(next_permutation(a.begin(),a.end()));cout<<"PASS exhaustive n="<<n<<" orderings="<<count<<" overlapping-extremes="<<intersect<<" max-min-degree="<<maximalExtremeMin<<"\n";}
