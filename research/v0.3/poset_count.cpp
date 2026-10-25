#include <bits/stdc++.h>
using namespace std;using E=pair<int,int>;
int main(int argc,char**argv){int n=atoi(argv[1]);int m=n*(n-1)/2;vector<E> seq;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)seq.emplace_back(i,j);mt19937 rng(200);map<pair<int,int>,int> best;map<pair<int,int>,long>num;
auto conn=[&](int skip){uint16_t info[12];for(int i=0;i<n;i++)info[i]=1<<i;for(int t=0;t<m;t++){if(t==skip)continue;auto[u,v]=seq[t];info[u]|=info[v];info[v]=info[u];}for(int i=0;i<n;i++)if(info[i]!=(1<<n)-1)return false;return true;};long long z=0,total=n<=5?4000000:250000;
for(;z<total;z++){if(n<=5){if(z>0&&!next_permutation(seq.begin(),seq.end()))break;}else shuffle(seq.begin(),seq.end(),rng);
 int tm[12][12]={};for(int t=0;t<m;t++){auto[u,v]=seq[t];tm[u][v]=tm[v][u]=t;} bool p[12][12]={};for(int u=0;u<n;u++)for(int v=0;v<n;v++)if(u!=v){bool comp=true;for(int w=0;w<n;w++)if(w!=u&&w!=v&&tm[u][w]>=tm[v][w])comp=false;p[u][v]=comp;}
 int minc=0,maxc=0;for(int u=0;u<n;u++){bool mini=true,maxi=true;for(int v=0;v<n;v++){if(p[v][u])mini=false;if(p[u][v])maxi=false;}minc+=mini;maxc+=maxi;}
 int f=0;for(int i=0;i<m;i++)f+=!conn(i);auto k=make_pair(minc,maxc);best[k]=max(best[k],f);num[k]++;
}
cout<<"n="<<n<<" checked="<<z<<"\n";for(auto[k,v]:best){cout<<"min,max="<<k.first<<","<<k.second<<" max compelled="<<v<<" cases="<<num[k]<<"\n";}
}
