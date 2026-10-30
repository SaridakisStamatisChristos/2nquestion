// Independent Stage 9 exact exhaustion of every ordered distinct-edge TREE
// gossip chronology on m=4,5,6,7, using Prüfer codes and edge permutations.
// At m<=7, four disjoint collectively complete groups must consist of
// either (2 singleton full collectors + 2 covering pairs) or
// (1 singleton full collector + 3 covering pairs); leftover vertices can
// be assigned to any covering group without invalidating coverage.
// This is equivalent to the full 4-group partition existence condition,
// not just a heuristic necessary test.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
using namespace std;
bool pair_two(const array<int,8>&k,int n,int full,int forbidden){
 for(int a=0;a<n;a++)if(!(forbidden>>a&1))
  for(int b=a+1;b<n;b++)if(!(forbidden>>b&1)&&(k[a]|k[b])==full)
   for(int c=0;c<n;c++)if(!((forbidden|(1<<a)|(1<<b))>>c&1))
    for(int d=c+1;d<n;d++)if(!((forbidden|(1<<a)|(1<<b))>>d&1)&&(k[c]|k[d])==full)
     return true;
 return false;
}
bool pair_three(const array<int,8>&k,int n,int full,int forbidden){
 for(int a=0;a<n;a++)if(!(forbidden>>a&1))
  for(int b=a+1;b<n;b++)if(!(forbidden>>b&1)&&(k[a]|k[b])==full)
   if(pair_two(k,n,full,forbidden|(1<<a)|(1<<b)))return true;
 return false;
}
bool four_groups(const array<int,8>&k,int n){
 int full=(1<<n)-1,collect=0;
 for(int i=0;i<n;i++)if(k[i]==full)collect|=1<<i;
 if(__builtin_popcount((unsigned)collect)>2){
  cerr<<"TREE_COLLECTOR_CAPACITY_VIOLATION\n";return true;
 }
 if(n<6)return false;
 if(__builtin_popcount((unsigned)collect)==2&&pair_two(k,n,full,collect))return true;
 if(n==7)for(int v=0;v<n;v++)if(collect>>v&1)
  if(pair_three(k,n,full,1<<v))return true;
 return false;
}
int main(){
 for(int n=4;n<=7;n++){
  int ntrees=1;for(int i=0;i<n-2;i++)ntrees*=n;
  uint64_t histories=0;
  int perm[8];iota(perm,perm+n-1,0);
  for(int id=0;id<ntrees;id++){
   int z=id,degrees[8];fill(degrees,degrees+n,1);
   int code[8]{};
   for(int i=0;i<n-2;i++){code[i]=z%n;z/=n;degrees[code[i]]++;}
   array<pair<int,int>,7>edges{};
   for(int i=0;i<n-2;i++){
    int leaf=-1;for(int j=0;j<n;j++)if(degrees[j]==1){leaf=j;break;}
    if(leaf<0)return 2;
    edges[i]={leaf,code[i]};--degrees[leaf];--degrees[code[i]];
   }
   int a=-1,b=-1;for(int j=0;j<n;j++)if(degrees[j]==1){
    if(a<0)a=j;else b=j;
   }
   if(b<0)return 2;
   edges[n-2]={a,b};
   iota(perm,perm+n-1,0);
   do{
    array<int,8>k{};for(int j=0;j<n;j++)k[j]=1<<j;
    for(int i=0;i<n-1;i++){
     auto [u,v]=edges[perm[i]];
     k[u]=k[v]=k[u]|k[v];
    }
    ++histories;
    if(four_groups(k,n)){
     cerr<<"FALSIFIED m="<<n<<" tree="<<id<<" order=";
     for(int i=0;i<n-1;i++)cerr<<perm[i]<<",";
     cerr<<"\n";return 3;
    }
   }while(next_permutation(perm,perm+n-1));
  }
  uint64_t expected=ntrees;
  for(int i=2;i<n;i++)expected*=i;
  if(histories!=expected){
   cerr<<"FAIL count "<<histories<<" expected "<<expected<<"\n";return 2;
  }
  cout<<"PASS m="<<n<<" labelled_trees="<<ntrees
      <<" ordered_distinct_tree_chronologies="<<histories
      <<" four_cover_groups=IMPOSSIBLE\n"<<flush;
 }
 cout<<"LIMIT: exact small-tree falsification only; all-n theorem uses separate human induction\n";
}