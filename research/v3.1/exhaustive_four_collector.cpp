// Standalone exhaustive original-order chronology falsifier.
// All connected labelled simple unicyclic v-edge graphs, every permutation,
// v=4,5,6. Do not confuse local component with successful global gossip.
#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct DSU {
 array<int,7> p{};
 DSU(){iota(p.begin(),p.end(),0);}
 int root(int x){return p[x]==x?x:p[x]=root(p[x]);}
 void join(int x,int y){p[root(x)]=root(y);}
};
int main(){
 for(int n=4;n<=6;n++){
  vector<pair<int,int>> all;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)all.emplace_back(u,v);
  int m=(int)all.size();
  vector<int> picked(m);fill(picked.begin(),picked.begin()+n,1);
  long long graphs=0,histories=0,four=0,non_strict=0;
  do {
   vector<pair<int,int>> edge;
   for(int i=0;i<m;i++)if(picked[i])edge.push_back(all[i]);
   DSU conn;for(auto [a,b]:edge)conn.join(a,b);
   bool connected=true;
   for(int x=1;x<n;x++)if(conn.root(x)!=conn.root(0))connected=false;
   if(!connected)continue;
   graphs++;
   vector<int> order(n);iota(order.begin(),order.end(),0);
   do {
    histories++;
    array<int,7> know{};
    for(int x=0;x<n;x++)know[x]=1<<x;
    for(int z:order){
     auto [a,b]=edge[z];know[a]=know[b]=know[a]|know[b];
    }
    int complete=0;
    for(int x=0;x<n;x++)complete+=(know[x]==(1<<n)-1);
    if(complete!=4)continue;
    four++;
    auto [u,v]=edge[order[n-2]];
    auto [w,z]=edge[order[n-1]];
    if(u==w||u==z||v==w||v==z){cerr<<"FAIL shared full root\n";return 2;}
    DSU halves;
    for(int k=0;k<n-2;k++){auto [a,b]=edge[order[k]];halves.join(a,b);}
    if(halves.root(u)==halves.root(v)||halves.root(w)==halves.root(z)){
      cerr<<"FAIL invalid two-tree division\n";return 3;
    }
    int wu=(halves.root(w)==halves.root(u))?w:z;
    int zv=(halves.root(w)==halves.root(v))?w:z;
    int core[4]={-1,-1,n-2,n-1};
    for(int k=0;k<n-2;k++){
      auto [a,b]=edge[order[k]];
      if((a==u&&b==wu)||(a==wu&&b==u))core[0]=k;
      if((a==v&&b==zv)||(a==zv&&b==v))core[1]=k;
    }
    if(core[0]<0||core[1]<0){cerr<<"FAIL missing side last-edge\n";return 4;}
    DSU arms;
    for(int k=0;k<n-2;k++)if(k!=core[0]&&k!=core[1]){
      auto [a,b]=edge[order[k]];arms.join(a,b);
    }
    vector<int> roots={u,wu,v,zv};
    for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)
      if(arms.root(roots[i])==arms.root(roots[j])){
        cerr<<"FAIL arms not separated\n";return 5;
      }
    int last[7];fill(last,last+n,-1);
    int earliest_core=min({core[0],core[1],core[2],core[3]});
    bool strict=true;
    for(int k=0;k<n;k++){
      if(k==core[0]||k==core[1]||k==core[2]||k==core[3])continue;
      auto [a,b]=edge[order[k]];
      if(arms.root(a)!=arms.root(b)){cerr<<"FAIL arm edge split\n";return 6;}
      last[arms.root(a)]=max(last[arms.root(a)],k);
      if(k>earliest_core)strict=false;
    }
    non_strict+=!strict;
    for(int root:roots){
      int first=n;
      for(int k:core){
        auto [a,b]=edge[order[k]];
        if(root==a||root==b)first=min(first,k);
      }
      if(last[arms.root(root)]>=first){cerr<<"FAIL causal precedence\n";return 7;}
    }
    for(int x=0;x<n;x++){
      if(find(roots.begin(),roots.end(),x)!=roots.end())continue;
      int own=0;
      for(int y=0;y<n;y++)if(arms.root(x)==arms.root(y))own|=1<<y;
      if(know[x]&~own){cerr<<"FAIL secret leaked into nonroot\n";return 8;}
    }
   }while(next_permutation(order.begin(),order.end()));
  }while(prev_permutation(picked.begin(),picked.end()));
  cout<<"PASS n="<<n<<" graphs="<<graphs<<" ordered histories="<<histories
      <<" 4-collector="<<four<<" non-strict="<<non_strict
      <<" all causally sealed\n";
  if(!four || (n>=5 && !non_strict))return 9;
 }
}
