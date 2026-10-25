#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct Edge{int u,v;};
int n,m; vector<Edge> edges;

bool pivot(const vector<int>& seq){
 uint32_t future[6],past[6];for(int i=0;i<n;++i){future[i]=1U<<i;past[i]=1U<<i;}
 uint32_t suffix[16];
 for(int i=m-1;i>=0;--i){auto [u,v]=edges[seq[i]];suffix[i]=future[u]|future[v];future[u]=future[v]=suffix[i];}
 const uint32_t all=(1U<<n)-1;
 for(int i=0;i<m;i++){
  auto [u,v]=edges[seq[i]];
  if((past[u]|past[v])==all && suffix[i]==all)return true;
  uint32_t merge=past[u]|past[v];past[u]=past[v]=merge;
 }
 return false;
}
bool spanner(const vector<int>&seq,uint32_t chosen){
 uint32_t info[6];for(int i=0;i<n;i++)info[i]=(1U<<i);
 for(int eid:seq)if(chosen & (1U<<eid)){
  auto [u,v]=edges[eid];uint32_t x=info[u]|info[v];info[u]=info[v]=x;
 }
 uint32_t all=(1U<<n)-1;for(int i=0;i<n;i++)if(info[i]!=all)return false;
 return true;
}
vector<uint32_t> candidate_masks(int count){
 vector<uint32_t> masks;int bits=(1<<m);
 for(int i=0;i<bits;++i)if(__builtin_popcount((unsigned)i)==count)masks.push_back(i);
 return masks;
}
int main(int argc,char**argv){n=argc>1?atoi(argv[1]):5;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)edges.push_back({i,j});m=edges.size();
 auto candidates=candidate_masks(2*n-4);
 vector<int> seq(m);iota(seq.begin(),seq.end(),0);
 long long total=0, nonpivot=0, checked=0;bool ok=true;
 do{
  total++;
  if(pivot(seq))continue;
  nonpivot++;
  bool found=false;
  for(uint32_t mask:candidates){
   if(spanner(seq,mask)){found=true;break;}
  }
  if(!found){ok=false;cout<<"COUNTEREXAMPLE ";for(int e:seq)cout<<e<<" ";cout<<"\n";break;}
  checked++;
 }while(next_permutation(seq.begin(),seq.end()));
 cout<<"n="<<n<<" total="<<total<<" nonpivot="<<nonpivot<<" optimal_witness="<<checked<<" exhaustive="<<(ok?"pass":"REFUTED")<<"\n";
}
