// Independent exhaustive original-order Type T tree verifier, all n=4..6.
// Includes ALL labelled trees, each distinct-edge chronology and ALL
// unordered noncollector pairs collectively covering the tree's secrets.
// Local components only, not complete two-half gossip schedules.
#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct UF {
 array<int,7> p{};
 UF(){iota(p.begin(),p.end(),0);}
 int root(int x){return p[x]==x?x:p[x]=root(p[x]);}
 void join(int x,int y){p[root(x)]=root(y);}
};
int main(){
 for(int n=4;n<=6;n++){
  vector<pair<int,int>> all;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)all.emplace_back(a,b);
  vector<int> chosen(all.size());
  fill(chosen.begin(),chosen.begin()+n-1,1);
  long long trees=0,histories=0,marked=0,non_strict=0;
  do {
   vector<pair<int,int>> edges;
   for(size_t x=0;x<all.size();x++)if(chosen[x])edges.push_back(all[x]);
   UF conn;for(auto [a,b]:edges)conn.join(a,b);
   bool ok=true;for(int x=1;x<n;x++)if(conn.root(x)!=conn.root(0))ok=false;
   if(!ok)continue;
   trees++;
   vector<int> perm(n-1);iota(perm.begin(),perm.end(),0);
   do {
    histories++;
    array<int,7> know{};
    for(int x=0;x<n;x++)know[x]=1<<x;
    for(int t:perm){auto [a,b]=edges[t];know[a]=know[b]=know[a]|know[b];}
    int allmask=(1<<n)-1;
    vector<int> complete;
    for(int x=0;x<n;x++)if(know[x]==allmask)complete.push_back(x);
    if(complete.size()!=2)continue;
    auto [u,v]=edges[perm[n-2]];
    if(find(complete.begin(),complete.end(),u)==complete.end()||
       find(complete.begin(),complete.end(),v)==complete.end())return 2;
    UF halves;
    for(int t=0;t<n-2;t++){auto [a,b]=edges[perm[t]];halves.join(a,b);}
    for(int w=0;w<n;w++)for(int z=w+1;z<n;z++){
      if(w==u||w==v||z==u||z==v)continue;
      if((know[w]|know[z])!=allmask)continue;
      marked++;
      if(halves.root(w)==halves.root(z))return 3;
      int wu=(halves.root(w)==halves.root(u))?w:z;
      int zv=(halves.root(w)==halves.root(v))?w:z;
      int sideLinks[2]={-1,-1};
      for(int t=0;t<n-2;t++){
        auto [a,b]=edges[perm[t]];
        if((a==u&&b==wu)||(b==u&&a==wu))sideLinks[0]=t;
        if((a==v&&b==zv)||(b==v&&a==zv))sideLinks[1]=t;
      }
      if(sideLinks[0]<0||sideLinks[1]<0)return 4;
      UF arms;
      for(int t=0;t<n-2;t++)if(t!=sideLinks[0]&&t!=sideLinks[1]){
        auto [a,b]=edges[perm[t]];arms.join(a,b);
      }
      vector<int> roots={u,wu,v,zv};
      for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)
        if(arms.root(roots[i])==arms.root(roots[j]))return 5;
      int core[3]={sideLinks[0],sideLinks[1],n-2};
      int earliest=min({core[0],core[1],core[2]});
      int lastArm[7];fill(lastArm,lastArm+n,-1);
      bool strict=true;
      for(int t=0;t<n-1;t++){
       if(t==core[0]||t==core[1]||t==core[2])continue;
       auto [a,b]=edges[perm[t]];
       if(arms.root(a)!=arms.root(b))return 6;
       lastArm[arms.root(a)]=max(lastArm[arms.root(a)],t);
       if(t>earliest)strict=false;
      }
      non_strict+=!strict;
      for(int root:roots){
        int first=n;
        for(int t:core){auto [a,b]=edges[perm[t]];if(a==root||b==root)first=min(first,t);}
        if(lastArm[arms.root(root)]>=first)return 7;
      }
      for(int x=0;x<n;x++){
        if(find(roots.begin(),roots.end(),x)!=roots.end())continue;
        int own=0;
        for(int y=0;y<n;y++)if(arms.root(x)==arms.root(y))own|=1<<y;
        if(know[x]&~own)return 8;
      }
    }
   }while(next_permutation(perm.begin(),perm.end()));
  }while(prev_permutation(chosen.begin(),chosen.end()));
  cout<<"PASS n="<<n<<" labelled trees="<<trees
      <<" chronological histories="<<histories
      <<" marked TypeT cover pairs="<<marked
      <<" strict failures="<<non_strict
      <<" all causally sealed\n";
  const long long expected[]={24,720,25920}, failures[]={0,240,11520};
  if(marked!=expected[n-4] || non_strict!=failures[n-4])return 9;
 }
}
