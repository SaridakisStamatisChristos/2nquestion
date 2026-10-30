// Exact connected local component chronology and collector/coverage oracle.
// Input rows: cell_size0 cell_size1 cell_size2 is_cyclic required0 required1 required2
#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int g0,g1,g2,cyc,r0,r1,r2;
 while(cin>>g0>>g1>>g2>>cyc>>r0>>r1>>r2){
  int m=g0+g1+g2,target=m-1+cyc;
  if(m>7){cout<<"UNSUPPORTED\n";continue;}
  vector<pair<int,int>> E;for(int i=0;i<m;i++)for(int j=i+1;j<m;j++)E.push_back({i,j});
  unsigned long long visited=0,conn=0,cover=0,collector=0,both=0;
  array<int,7> initial{},roots{};for(int i=0;i<m;i++){initial[i]=1<<i;roots[i]=i;}
  int groups[3]={g0,g1,g2},req[3]={r0,r1,r2};
  function<void(int,uint32_t,array<int,7>,array<int,7>)> dfs=
  [&](int depth,uint32_t used,array<int,7> state,array<int,7> parent){
   if(depth==target){
    ++visited;
    auto findroot=[&](int x){while(parent[x]!=x)x=parent[x];return x;};
    for(int i=1;i<m;i++)if(findroot(i)!=findroot(0))return;
    ++conn;
    bool goodcov=true,goodcol=true;int pos=0,full=(1<<m)-1;
    for(int k=0;k<3;k++){
     int uni=0,complete=0;
     for(int j=0;j<groups[k];j++){uni|=state[pos];complete+=state[pos]==full;pos++;}
     if(uni!=full)goodcov=false;
     if(complete<req[k])goodcol=false;
    }
    cover+=goodcov;collector+=goodcol;both+=(goodcov&&goodcol);
    return;
   }
   for(int t=0;t<(int)E.size();t++)if(!(used>>t&1)){
    auto [u,v]=E[t];auto nstate=state,nparent=parent;
    nstate[u]=nstate[v]=state[u]|state[v];
    auto findroot=[&](int x){while(nparent[x]!=x)x=nparent[x];return x;};
    nparent[findroot(u)]=findroot(v);
    dfs(depth+1,used|(1u<<t),nstate,nparent);
   }
  };
  dfs(0,0,initial,roots);
  cout<<"RESULT "<<m<<" "<<cyc<<" "<<visited<<" "<<conn<<" "<<cover<<" "<<collector<<" "<<both<<"\n";
 }
}
