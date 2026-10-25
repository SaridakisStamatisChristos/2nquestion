#include <bits/stdc++.h>
using namespace std;using E=pair<int,int>;
bool conn(int n,const vector<E>&s,uint64_t mask){int in[12];for(int i=0;i<n;i++)in[i]=1<<i;for(int i=0;i<(int)s.size();i++)if(mask>>i&1){auto[u,v]=s[i];in[u]|=in[v];in[v]=in[u];}for(int i=0;i<n;i++)if(in[i]!=(1<<n)-1)return false;return true;}
int main(int argc,char**argv){int n=atoi(argv[1]),limit=argc>2?atoi(argv[2]):50000;vector<E> b;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)b.push_back({i,j});int m=b.size();mt19937 rng(8675309);long long exact=0,notSp=0,maxF=0;
for(int z=0;z<limit;z++){if(z==0&&n<=5){} else if(n<=5){if(!next_permutation(b.begin(),b.end()))break;}else{shuffle(b.begin(),b.end(),rng);}
 uint64_t fm=0,full=(1ull<<m)-1;for(int i=0;i<m;i++)if(!conn(n,b,full^(1ull<<i)))fm|=1ull<<i;int f=__builtin_popcountll(fm);maxF=max(maxF,(long long)f);if(f==2*n-3){exact++;if(!conn(n,b,fm)){notSp++;if(notSp==1){cout<<"WITNESS forced "<<f<<" not spanner seq ";for(auto [u,v]:b)cout<<u<<","<<v<<" ";cout<<"\n";}}}}
cout<<"tested "<<limit<<" maxForced "<<maxF<<" exact "<<exact<<" nonsp "<<notSp<<"\n";}
