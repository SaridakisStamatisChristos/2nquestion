// Stage-3 adversarial component oracle.
// Independent two-phase search: enumerate the first (m-2) distinct contacts
// while maintaining a static union-find and information state, then independently
// enumerate the final two contacts. No memoization of (used edges, knowledge).
// A m-1-contact tree is separately handled by an ordinary distinct-edge DFS.
// Input: g0 g1 g2 req0 req1 req2 cyclic, one case per line.
// Output: DOMAIN...B...D...END in sorted deterministic order.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

using Sig = array<uint64_t,3>;
struct Exam {
  array<int,3> sizes, quotas;
  int cyclic, n, full, goal, group[9], left[3], right[3];
  vector<pair<int,int>> edge;
  set<Sig> B,D;
  uint64_t leaves=0, valid=0, states=0;
  Exam(array<int,3> s,array<int,3> q,int cy):sizes(s),quotas(q),cyclic(cy) {
    n=s[0]+s[1]+s[2];goal=n-1+cy;full=(1<<n)-1;left[0]=0;
    if(n<3||n>7||cy<0||cy>1){cerr<<"BAD SIZE/CYCLE\n";exit(3);}
    for(int i=0;i<3;i++){right[i]=left[i]+s[i];if(i<2)left[i+1]=right[i];}
    for(int v=0;v<n;v++){for(int g=0;g<3;g++)if(left[g]<=v&&v<right[g])group[v]=g;}
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edge.emplace_back(a,b);
  }
  void record(const array<unsigned char,9>&state) {
    int complete[3]={}, coverage[3]={};
    for(int v=0;v<n;v++){int g=group[v];coverage[g]|=state[v];if(state[v]==full)complete[g]++;}
    for(int g=0;g<3;g++)if(coverage[g]!=full||complete[g]<quotas[g])return;
    valid++;
    Sig suff{}, ances{};
    for(int g=0;g<3;g++){
      int width=sizes[g];
      for(int subset=0;subset<(1<<width);subset++){
        int seen=0;
        for(int j=0;j<width;j++)if(subset&(1<<j))seen|=state[left[g]+j];
        if(seen==full)suff[g]|=uint64_t(1)<<subset;
      }
      // For each original source secret the vertices of this cell which carry
      // the secret form one destination-ancestry requirement subset.
      for(int secret=0;secret<n;secret++){
        int receivers=0;
        for(int j=0;j<width;j++)
          if(state[left[g]+j]&(1<<secret))receivers|=1<<j;
        ances[g]|=uint64_t(1)<<receivers;
      }
    }
    B.insert(suff);D.insert(ances);
  }
  static void merge(array<unsigned char,9>&k,int a,int b){
    unsigned char all=k[a]|k[b];k[a]=all;k[b]=all;
  }
  int get(const array<unsigned char,9>&par,int i) const{
    while(par[i]!=i)i=par[i];return i;
  }
  // parent copied to child to make the graph test entirely local.
  void add(const array<unsigned char,9>&parent, int a,int b,
           array<unsigned char,9>&out,int&closes) const{
    out=parent;
    int ra=get(out,a),rb=get(out,b);
    closes=(ra==rb);
    if(!closes)out[ra]=rb;
  }
  bool collector_endpoints(int a,int b,int c,int d)const{
    bool marked[9]={};
    for(int v:{a,b,c,d})marked[v]=true;
    int counts[3]={};
    for(int v=0;v<n;v++)if(marked[v])counts[group[v]]++;
    for(int i=0;i<3;i++)if(counts[i]<quotas[i])return false;
    return true;
  }
  // In a unicyclic schedule m-2 calls leave the graph disconnected, hence
  // no participant can be globally informed before the final two contacts.
  void finish_two(uint32_t used,const array<unsigned char,9>&knowledge,
                  const array<unsigned char,9>&par,int cycles,int components){
    for(int e=0;e<(int)edge.size();e++){
      if(used&(1u<<e))continue;
      auto [a,b]=edge[e];
      array<unsigned char,9> p1;
      int firstcloses;add(par,a,b,p1,firstcloses);
      if(cycles+firstcloses>1)continue;
      for(int f=0;f<(int)edge.size();f++){
        if(f==e || (used&(1u<<f)))continue;
        auto [c,d]=edge[f];
        if(!collector_endpoints(a,b,c,d))continue;
        array<unsigned char,9> p2;
        int secondcloses;add(p1,c,d,p2,secondcloses);
        if(cycles+firstcloses+secondcloses!=1)continue;
        if(components-firstcloses*0-(1-firstcloses)-(1-secondcloses)!=1)
          continue;
        // Check an independent graph invariant from the final DSU:
        bool connected=true;int root=get(p2,0);
        for(int v=1;v<n;v++)if(get(p2,v)!=root)connected=false;
        if(!connected)continue;
        auto k=knowledge;merge(k,a,b);merge(k,c,d);
        leaves++;record(k);
      }
    }
  }
  void dfs_cyclic(int depth,uint32_t used,array<unsigned char,9>knowledge,
                  array<unsigned char,9>parent,int cyc,int cc) {
    states++;
    if(depth==n-2) {
      finish_two(used,knowledge,parent,cyc,cc);return;
    }
    for(int e=0;e<(int)edge.size();e++){
      if(used&(1u<<e))continue;
      auto [a,b]=edge[e];
      array<unsigned char,9> nextParent;
      int closes;add(parent,a,b,nextParent,closes);
      if(cyc+closes>1)continue;
      // Can the remaining contacts still join every component?
      int newcc=cc-(1-closes);
      if(newcc-1>n-(depth+1))continue;
      auto next=knowledge;merge(next,a,b);
      dfs_cyclic(depth+1,used|(1u<<e),next,nextParent,cyc+closes,newcc);
    }
  }
  void dfs_tree(int depth,uint32_t used,array<unsigned char,9>knowledge,
                array<unsigned char,9>parent,int cc) {
    states++;
    if(depth==n-1) {
      if(cc!=1){cerr<<"BAD TREE CONNECTIVITY\n";exit(4);}
      leaves++;record(knowledge);return;
    }
    for(int e=0;e<(int)edge.size();e++){
      if(used&(1u<<e))continue;
      auto [a,b]=edge[e];
      array<unsigned char,9> nextParent;
      int closes;add(parent,a,b,nextParent,closes);
      if(closes)continue;
      if(depth==n-2){
        // Every final full collector must be incident to last tree contact.
        if(!collector_endpoints(a,b,a,b))continue;
      }
      auto next=knowledge;merge(next,a,b);
      dfs_tree(depth+1,used|(1u<<e),next,nextParent,cc-1);
    }
  }
  void run() {
    array<unsigned char,9> k{},parent{};
    for(int i=0;i<n;i++){k[i]=(unsigned char)(1<<i);parent[i]=i;}
    if(cyclic)dfs_cyclic(0,0,k,parent,0,n);
    else dfs_tree(0,0,k,parent,n);
  }
  void report()const{
    cout<<"DOMAIN";
    for(int a:sizes)cout<<" "<<a;
    for(int a:quotas)cout<<" "<<a;
    cout<<" "<<cyclic<<" 0 "<<B.size()<<" "<<D.size()<<"\n";
    for(auto x:B)cout<<"B "<<x[0]<<" "<<x[1]<<" "<<x[2]<<"\n";
    for(auto x:D)cout<<"D "<<x[0]<<" "<<x[1]<<" "<<x[2]<<"\n";
    cout<<"END\n";
    cerr<<"STAGE3 "<<sizes[0]<<sizes[1]<<sizes[2]<<" req="
        <<quotas[0]<<quotas[1]<<quotas[2]<<" cycle="<<cyclic
        <<" prefix_nodes="<<states<<" terminal_schedules="<<leaves
        <<" valid="<<valid<<" B="<<B.size()<<" D="<<D.size()<<"\n";
  }
};
int main(){
  ios::sync_with_stdio(false);cin.tie(nullptr);
  int a,b,c,x,y,z,cy;
  while(cin>>a>>b>>c>>x>>y>>z>>cy){
    Exam e({a,b,c},{x,y,z},cy);
    e.run();e.report();
  }
}
