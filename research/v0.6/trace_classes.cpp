// Count temporal edge-order equivalence classes under swaps of adjacent disjoint edges.
// For n=4,5 exhaustive; depends only on relative ordering of incident edges.
#include <bits/stdc++.h>
using namespace std;
static bool tc(int n, const vector<pair<int,int>>& ed, const vector<int>& ord, unsigned mask){
    unsigned info[6]; for(int v=0;v<n;v++)info[v]=1U<<v;
    for(int i=0;i<(int)ord.size();i++) if(mask&(1U<<ord[i])){
       auto [u,v]=ed[ord[i]]; unsigned z=info[u]|info[v]; info[u]=info[v]=z;
    }
    unsigned full=(1U<<n)-1; for(int v=0;v<n;v++) if(info[v]!=full)return false;return true;
}
int main(int argc,char**argv){
  int n=argc>=2?atoi(argv[1]):4; if(n<3||n>5){cerr<<"n 3..5\n";return 1;}
  vector<pair<int,int>> ed;for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)ed.push_back({u,v});
  int m=ed.size(); vector<pair<int,int>> deps;
  for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){
    auto [u,v]=ed[a];auto [x,y]=ed[b];
    if(u==x||u==y||v==x||v==y)deps.push_back({a,b});
  }
  if(deps.size()>32){cerr<<"too many bits\n";return 1;}
  vector<int> ord(m);iota(ord.begin(),ord.end(),0);unordered_set<uint32_t> seen;
  long long permutations=0;long long equivalence=0;int histogram[12]={0};int invariant_fail=0;
  do{
    ++permutations;int pos[10];for(int i=0;i<m;i++)pos[ord[i]]=i;
    uint32_t sig=0;
    for(int j=0;j<(int)deps.size();j++) if(pos[deps[j].first]<pos[deps[j].second])sig|=uint32_t(1)<<j;
    if(!seen.insert(sig).second)continue;
    ++equivalence;
    int opt=m+1;
    // Enumerate feasible subsets by cardinality, minimal 2n-4 (for n>=4).
    for(int size=max(n==3?2:2*n-4,0);size<=m;size++){
      bool found=false;
      for(unsigned bits=0;bits<(1U<<m);bits++) if((int)__builtin_popcount(bits)==size && tc(n,ed,ord,bits)){
        found=true;break;
      }
      if(found){opt=size;break;}
    }
    if(opt>m){cerr<<"BUG:no spanner\n"; return 2;}histogram[opt]++;
  }while(next_permutation(ord.begin(),ord.end()));
  cout<<"n="<<n<<" edges="<<m<<" local_dependencies="<<deps.size()<<" permutations="<<permutations<<" trace_classes="<<equivalence<<"\n";
  for(int j=0;j<=m;j++)if(histogram[j])cout<<"optimal_size="<<j<<" equivalence_classes="<<histogram[j]<<"\n";
}
