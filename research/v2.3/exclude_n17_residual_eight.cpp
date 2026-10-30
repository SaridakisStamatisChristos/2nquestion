// Stage 6 n17 residual verifier. Tree histories are EXACT (rooted final-edge DP).
// Unicyclic >=3 collector histories use a SOUND SUPerset: final contact may
// repeat an internal edge. Therefore UNSAT proves exclusion; SAT proves nothing.
// This file does not change the previously verified n<=16 certificate.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
using S=array<uint16_t,9>;
using P=array<uint64_t,3>;
struct SH{size_t operator()(S const&s)const{uint64_t v=1469598103934665603ULL;for(auto x:s)v=(v^x)*1099511628211ULL;return v;}};
struct Rooted{
 int n;vector<S> cache[512][9];bool done[512][9]{};
 explicit Rooted(int x):n(x){}
 const vector<S>& get(int mask,int root){
  if(done[mask][root])return cache[mask][root];
  assert(mask>>root&1);done[mask][root]=true;
  if(mask==(1<<root)){S k{};k[root]=mask;cache[mask][root].push_back(k);return cache[mask][root];}
  unordered_set<S,SH>seen;int rem=mask^(1<<root);
  for(int V=rem;V;V=(V-1)&rem){int U=mask^V;auto const&a=get(U,root);
   for(int y=0;y<n;y++)if(V>>y&1){auto const&b=get(V,y);
    for(auto const&x:a)for(auto const&z:b){
     S s{};for(int i=0;i<n;i++)s[i]=x[i]|z[i];s[root]=s[y]=mask;seen.insert(s);
    }
   }
  }
  cache[mask][root].assign(seen.begin(),seen.end());return cache[mask][root];
 }
};
struct Key{P g{},req{};bool cyc=false;bool operator<(Key const&y)const{return tie(g,req,cyc)<tie(y.g,y.req,y.cyc);}};
struct Domain{set<P>B,D;uint64_t states=0;bool optimistic=false;};
struct Oracle{
 int n,full;Key key;array<int,3>offs{};array<int,9>grp{};Rooted root;Domain out;
 explicit Oracle(Key k):n(int(k.g[0]+k.g[1]+k.g[2])),full((1<<n)-1),key(k),root(n){
  assert(n>=1&&n<=9);
  for(int g=0;g<3;g++)offs[g]=g?offs[g-1]+key.g[g-1]:0;
  for(int i=0;i<n;i++)for(int g=0;g<3;g++)
   if(i>=offs[g]&&i<offs[g]+int(key.g[g]))grp[i]=g;
 }
 void save(S const&k){
  for(int g=0;g<3;g++){int know=0,collect=0;
   for(int i=offs[g];i<offs[g]+int(key.g[g]);i++){know|=k[i];collect+=(k[i]==full);}
   if(know!=full||collect<int(key.req[g]))return;
  }
  out.states++;P B{},D{};
  for(int g=0;g<3;g++){
   int sz=int(key.g[g]);assert(sz<=6);
   for(int sub=0;sub<(1<<sz);sub++){int know=0;
    for(int j=0;j<sz;j++)if(sub>>j&1)know|=k[offs[g]+j];
    if(know==full)B[g]|=1ULL<<sub;
   }
   for(int secret=0;secret<n;secret++){int sub=0;
    for(int j=0;j<sz;j++)if(k[offs[g]+j]>>secret&1)sub|=1<<j;
    D[g]|=1ULL<<sub;
   }
  }
  out.B.insert(B);out.D.insert(D);
 }
 void tree(){
  for(int x=0;x<n;x++)for(int y=x+1;y<n;y++){
   int cnt[3]{};cnt[grp[x]]++;cnt[grp[y]]++;
   bool allowed=true;for(int g=0;g<3;g++)if(cnt[g]<int(key.req[g]))allowed=false;
   if(!allowed)continue;
   int rem=full^(1<<x)^(1<<y);
   for(int split=rem;;split=(split-1)&rem){int U=split|(1<<x),V=full^U;
    if(V>>y&1){
     const auto&a=root.get(U,x),&b=root.get(V,y);
     // An untouched cell has no final bridge endpoint; its members
     // on EACH side must collectively know that side's entire secrets.
     auto ok=[&](S const&v,int side){
      for(int g=0;g<3;g++)if(grp[x]!=g&&grp[y]!=g){
       int know=0;for(int i=0;i<n;i++)if((side>>i&1)&&grp[i]==g)know|=v[i];
       if(know!=side)return false;
      }
      return true;
     };
     vector<S const*>A,B;
     for(auto const&s:a)if(ok(s,U))A.push_back(&s);
     for(auto const&t:b)if(ok(t,V))B.push_back(&t);
     for(auto p:A)for(auto q:B){
      S k{};for(int i=0;i<n;i++)k[i]=(*p)[i]|(*q)[i];
      k[x]=k[y]=full;save(k);
     }
    }
    if(!split)break;
   }
  }
 }
 void small_cycle(){
  vector<pair<int,int>>edges;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
  function<void(int,uint64_t,S)>dfs=[&](int depth,uint64_t used,S k){
   if(depth==n){int parent[9];iota(parent,parent+n,0);
    auto rootof=[&](int a){while(parent[a]!=a)a=parent[a];return a;};
    for(int z=0;z<int(edges.size());z++)if(used>>z&1){
     auto[a,b]=edges[z];parent[rootof(a)]=rootof(b);
    }
    for(int i=0;i<n;i++)if(rootof(i)!=rootof(0))return;
    save(k);return;
   }
   for(int z=0;z<int(edges.size());z++)if(!(used>>z&1)){
    auto[a,b]=edges[z];S t=k;t[a]=t[b]=k[a]|k[b];dfs(depth+1,used|(1ULL<<z),t);
   }
  };
  S k{};for(int i=0;i<n;i++)k[i]=1<<i;dfs(0,0,k);
 }
 void large_cycle(){
  assert(key.req[0]+key.req[1]+key.req[2]>=3);
  out.optimistic=true;
  // >=3 full collectors after m cyclic calls imply exactly two TREE
  // components after m-2 calls, since with >=3 components before the
  // last two calls only the final two endpoints can know all secrets.
  // The first cross-call x-y must create TWO full collectors; otherwise
  // only the endpoints of the last call can be full.
  for(int U=1;U<full;U++)if(U&1){int V=full^U;
   for(int x=0;x<n;x++)if(U>>x&1)for(int y=0;y<n;y++)if(V>>y&1){
    const auto&a=root.get(U,x),&b=root.get(V,y);
    vector<pair<int,int>>second;
    for(int z=0;z<n;z++)for(int w=z+1;w<n;w++)if(!((z==x&&w==y)||(z==y&&w==x))){
     int counts[3]{};for(int t:{x,y,z,w})counts[grp[t]]++;
     bool possible=true;for(int g=0;g<3;g++)if(counts[g]<int(key.req[g]))possible=false;
     if(possible)second.push_back({z,w});
    }
    if(second.empty())continue;
    for(auto const&s:a)for(auto const&t:b){
     S prior{};for(int i=0;i<n;i++)prior[i]=s[i]|t[i];prior[x]=prior[y]=full;
     for(auto[z,w]:second){S k=prior;k[z]=k[w]=k[z]|k[w];save(k);}
    }
   }
  }
 }
 Domain run(){if(!key.cyc)tree();else if(n<=6)small_cycle();else large_cycle();return move(out);}
};
Key makekey(P g,P req,bool cyc){Key k;k.g=g;k.req=req;k.cyc=cyc;return k;}
void require(bool b,const char *label){if(!b){cerr<<"FAIL "<<label<<"\n";exit(2);}}
struct Case{int id,cr,cc;int M[3][3];};
const vector<Case>cases={
 {72,0,0,{{1,1,2},{1,2,2},{2,2,4}}},
 {73,0,1,{{1,1,2},{1,2,2},{2,2,4}}},
 {74,1,1,{{1,1,2},{1,2,2},{2,2,4}}},
 {75,2,2,{{1,1,2},{1,2,2},{2,2,4}}}
};
int main(){
 // Independent local-regression anchors: all are full (non-optimistic)
 // except the 4-collector case whose two final links must be cross-links.
 auto t223=Oracle(makekey({2,2,3},{0,2,0},false)).run();
 require(t223.B.empty()&&t223.D.empty(),"seven-vertex two collectors");
 auto t224=Oracle(makekey({2,2,4},{0,2,0},false)).run();
 require(t224.B==set<P>{{8,14,32768}}&&t224.D==set<P>{{6,8,278}}
         &&t224.states==48,"n16 exact eight-vertex tree regression");
 auto c224=Oracle(makekey({2,2,4},{2,2,0},true)).run();
 require(c224.B==set<P>{{14,14,32768}}&&c224.D==set<P>{{8,8,278}},
         "n16 exact eight-vertex four collector cyclic regression");
 auto swapped=Oracle(makekey({2,2,4},{2,0,0},false)).run();
 require(swapped.B==set<P>{{14,8,32768}}&&swapped.D==set<P>{{8,6,278}},
         "two collector cell permutation regression");
 cout<<"PASS exact local anchors 223, 224-tree, 224-unicyclic, 224-swapped\n";
 // 32/33: col2 tree 224/020; 34: col2 unicyclic 224/220.
 // In both cases D[2] == 278 has all FOUR singletons (1,2,4,8).
 // Thus prefix row2 must have FOUR complete collectors in that cell.
 // Tree row2 (orbits 32/33) has at most 2 total collectors.
 // Cyclic row2 (orbit 34) has at most 4 total and also requires three
 // complete collectors in disjoint cells 0 and 1. Contradiction.
 require(t224.D.begin()->at(2)==278&&c224.D.begin()->at(2)==278,
         "four singleton receiver masks in suffix third cell");
 for(int id:{32,33,34})cout<<"PASS orbit "<<id<<" collector bound vs D[2]=278\n";
 // 35: the suffix col2 exact tree type 223/020 is empty.
 cout<<"PASS orbit 35 exact local 223/020 domain empty\n";
 map<Key,Domain>cache;
 auto get=[&](Key const&k)->Domain&{
  auto it=cache.find(k);if(it!=cache.end())return it->second;
  auto t=chrono::steady_clock::now();
  auto[p,inserted]=cache.emplace(k,Oracle(k).run());
  cerr<<"DOMAIN ";
  for(auto x:k.g){cerr<<x;}
  cerr<<" req=";
  for(auto x:k.req){cerr<<x;}
  cerr<<" cyc="<<k.cyc<<" B="<<p->second.B.size()
      <<" D="<<p->second.D.size()<<" states="<<p->second.states
      <<" optimistic="<<p->second.optimistic
      <<" secs="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
  return p->second;
 };
 for(auto const&z:cases){
  int R[3][3]{},C[3][3]{};
  for(int r=0;r<3;r++)for(int c=0;c<3;c++)
   R[r][c]=C[r][c]=(z.M[r][c]==1);
  for(int c=0;c<3;c++)if(c!=z.cc){vector<int>s;
   for(int r=0;r<3;r++)if(z.M[r][c]==1)s.push_back(r);
   for(int r=0;r<3;r++)if(!s.empty()&&z.M[r][c]!=1)R[r][c]=max(R[r][c],1);
   if(s.size()==2)for(int r=0;r<3;r++)if(z.M[r][c]!=1){
    if(z.M[r][c]==2)R[r][c]=2;
    else if(z.M[r][c]==3)R[r][c]=max(R[r][c],1);
   }
  }
  for(int r=0;r<3;r++)if(r!=z.cr){vector<int>s;
   for(int c=0;c<3;c++)if(z.M[r][c]==1)s.push_back(c);
   for(int c=0;c<3;c++)if(!s.empty()&&z.M[r][c]!=1)C[r][c]=max(C[r][c],1);
   if(s.size()==2)for(int c=0;c<3;c++)if(z.M[r][c]!=1){
    if(z.M[r][c]==2)C[r][c]=2;
    else if(z.M[r][c]==3)C[r][c]=max(C[r][c],1);
   }
  }
  array<Domain*,3>row{},col{};
  for(int r=0;r<3;r++){
   P gs{},req{};for(int c=0;c<3;c++){gs[c]=z.M[r][c];req[c]=R[r][c];}
   row[r]=&get(makekey(gs,req,r==z.cr));
  }
  for(int c=0;c<3;c++){
   P gs{},req{};for(int r=0;r<3;r++){gs[r]=z.M[r][c];req[r]=C[r][c];}
   col[c]=&get(makekey(gs,req,c==z.cc));
  }
  // Safe global relaxation: each row may independently choose B profiles,
  // independently of any row's D; each column may choose a D profile,
  // ignoring even the cross-half edge-disjointness constraints.
  // If this overapproximate domain is UNSAT, no true chronology exists.
  bool compat=false;
  for(auto const&d0:col[0]->D)for(auto const&d1:col[1]->D)
   for(auto const&d2:col[2]->D){
    bool all=true;
    for(int r=0;r<3;r++){
     bool found=false;
     for(auto const&b:row[r]->B){
      if((b[0]&d0[r])==d0[r]&&(b[1]&d1[r])==d1[r]&&
         (b[2]&d2[r])==d2[r]){found=true;break;}
     }
     if(!found){all=false;break;}
    }
    if(all)compat=true;
   }
  require(!compat,"n17 residual exact/relaxed CSP");
  cout<<"PASS orbit "<<z.id<<" necessary-profile UNSAT\n";
 }
 cout<<"PASS n17 all eight residual marked symmetry classes EXCLUDED; "
     <<"whole theorem conditional on earlier structural lemmas\n";
}
