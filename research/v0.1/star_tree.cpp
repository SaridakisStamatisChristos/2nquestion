#include <bits/stdc++.h>
using namespace std;
struct Pair {int u,v;};
static vector<Pair> ed;
uint64_t adjacency_mask(int u,int v){ if(u>v)swap(u,v);for(int k=0;k<(int)ed.size();k++)if(ed[k].u==u&&ed[k].v==v)return 1ULL<<k;return 0;}
vector<uint64_t> make_cands(int n){
 vector<uint64_t> masks;
 for(int hub=0;hub<n;hub++){
  vector<int> other;for(int j=0;j<n;j++)if(j!=hub)other.push_back(j);
  int z=other.size();
  uint64_t star=0;for(int j:other)star|=adjacency_mask(hub,j);
  int total=1;for(int k=0;k<z-2;k++)total*=z;
  for(int i=0;i<total;i++){
   int x=i;vector<int> prufer;vector<int> deg(z,1);
   for(int k=0;k<z-2;k++){int c=x%z;x/=z;prufer.push_back(c);deg[c]++;}
   uint64_t mask=star;
   for(int c:prufer){int leaf=0;while(deg[leaf]!=1)leaf++;mask|=adjacency_mask(other[c],other[leaf]);deg[c]--;deg[leaf]--;}
   int a=-1,b=-1;for(int k=0;k<z;k++)if(deg[k]==1){if(a<0)a=k;else b=k;}
   mask|=adjacency_mask(other[a],other[b]);masks.push_back(mask);
  }
 }
 sort(masks.begin(),masks.end());masks.erase(unique(masks.begin(),masks.end()),masks.end());return masks;
}
bool spanner(int n,const vector<int>&seq,uint64_t keep){uint32_t masks[12]; for(int i=0;i<n;i++)masks[i]=1U<<i;for(int id:seq)if(keep>>id &1){auto [a,b]=ed[id];uint32_t q=masks[a]|masks[b];masks[a]=q;masks[b]=q;}uint32_t full=(1U<<n)-1;for(int i=0;i<n;i++)if(masks[i]!=full)return false;return true;}
int main(int argc,char**argv){int n=argc>=2?atoi(argv[1]):6;unsigned long long tries=argc>=3?atoll(argv[2]):100000;uint64_t seed=argc>=4?stoull(argv[3]):2177;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)ed.push_back({i,j});
 auto cand=make_cands(n);cerr<<"candidates "<<cand.size()<<"\n";
 mt19937_64 gen(seed);vector<int>seq(ed.size());iota(seq.begin(),seq.end(),0);
 auto t=chrono::steady_clock::now();
 for(unsigned long long z=0;z<tries;z++){
  shuffle(seq.begin(),seq.end(),gen);
  bool ok=false;for(uint64_t k:cand){if(spanner(n,seq,k)){ok=true;break;}}
  if(!ok){cout<<"COUNTEREXAMPLE n "<<n<<" trial "<<z<<" seed "<<seed<<"\n";for(int e:seq)cout<<"("<<ed[e].u<<","<<ed[e].v<<") ";cout<<"\n";return 0;}
  if((z+1)%10000==0)cerr<<"tried "<<z+1<<" secs "<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
 }
 cout<<"No counterexample in "<<tries<<" trials\n";
}
