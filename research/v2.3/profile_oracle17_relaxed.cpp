// RESEARCH v2.3: capacity-10 extension for the n17 residual frontier.
// Derived from the preserved v2.2 oracle; its audited finite n16 source
// remains unchanged. m=10 is allowed ONLY through the sound optimistic
// tree/cycle branch; exact walk remains restricted to m<=7.
// This intentionally copies and extends the v2.1 implementation in a NEW file.
// Exact component-local full-information gossip oracle and relaxed temporal-profile CSP.
// Only UNSAT is a certificate. SAT here may reuse an edge across chronological halves.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
struct Profile { array<uint64_t,3> b{};bool operator==(const Profile&o) const{return b==o.b;} };
struct PH {size_t operator()(const Profile &p) const {size_t h=1469598103934665603ULL;for(auto x:p.b)h=(h^x)*1099511628211ULL;return h;}};
struct State {uint32_t used;uint64_t k;bool operator==(const State&o)const{return used==o.used&&k==o.k;}};
struct SH {size_t operator()(const State&s)const{return hash<uint64_t>{}(s.k*0x9e3779b97f4a7c15ULL ^ s.used);}};
struct Key {array<int,3> g,req;bool cyc;bool optimistic;bool operator==(Key const&o)const{return g==o.g&&req==o.req&&cyc==o.cyc&&optimistic==o.optimistic;}};
struct KH {size_t operator()(Key const&k)const {size_t h=0;for(int x:k.g)h=h*31+x;for(int x:k.req)h=h*31+x;return h*7+int(k.cyc)*2+int(k.optimistic);}};
struct Domain {vector<Profile> b,d;uint64_t explored=0,terminal=0,valid=0;bool exact=true;};
struct Oracle {
 Key key;Domain out;int m,target,full,offs[4],grp[10];vector<pair<int,int>> edges;
 unordered_set<Profile,PH> B,D;
 unordered_set<State,SH> seen;
 Oracle(Key const &k):key(k){offs[0]=0;for(int i=0;i<3;i++)offs[i+1]=offs[i]+key.g[i];m=offs[3];if(m>10 || m<1){cerr<<"UNSUPPORTED component m="<<m<<" max=10\n";exit(2);}for(int g:key.g)if(g>6 || g<0){cerr<<"UNSUPPORTED cell group g="<<g<<" max=6\n";exit(2);}target=m-1+key.cyc;full=(1<<m)-1;for(int i=0;i<m;i++){for(int j=0;j<3;j++)if(offs[j]<=i&&i<offs[j+1])grp[i]=j;for(int j=i+1;j<m;j++)edges.push_back({i,j});}}
 void save(const array<int,10>&k){
  for(int j=0;j<3;j++){
   int unionall=0,collect=0;
   for(int x=offs[j];x<offs[j+1];x++){unionall|=k[x];collect+=k[x]==full;}
   if(unionall!=full || collect<key.req[j])return;
  }
  out.valid++;
  Profile p,q;
  for(int g=0;g<3;g++){
   int len=key.g[g];
   for(int mask=0;mask<(1<<len);mask++){
    int know=0;for(int x=0;x<len;x++)if(mask>>x&1)know|=k[offs[g]+x];
    if(know==full)p.b[g]|=1ULL<<mask;
   }
   for(int secret=0;secret<m;secret++){
    int entrymask=0;for(int x=0;x<len;x++)if(k[offs[g]+x]>>secret&1)entrymask|=1<<x;
    q.b[g]|=1ULL<<entrymask;
   }
  }
  B.insert(p);D.insert(q);
 }
 void opt(){
  out.exact=false;
  // Every real final tree edge xy splits the preceding calls into two sides.
  // Giving both endpoints all secrets, and each other vertex all of its side's
  // secrets, pointwise dominates actual midpoint knowledge.
  if(key.cyc){
   // Sound relaxation for an m-contact unicyclic component.
   // After the first m-2 calls the static contact graph is disconnected.
   // Select a union of its connected components as side A, the rest B.
   // Every earlier secret-knowledge set lies within its side. Giving each
   // vertex ALL of its side's secrets, then applying the actual last two
   // call endpoints, dominates the real final state pointwise.
   // Enumerate ALL side partitions and ALL ordered distinct last-pair
   // choices, even if no exact chronology realizes that configuration.
   for(int side=1;side<full;side++){
     if(!(side&1))continue; // complements have identical optimistic bounds
     array<int,10> prior{};
     for(int z=0;z<m;z++) prior[z]=(side>>z&1)?side:(full^side);
     for(size_t i=0;i<edges.size();i++)
       for(size_t j=0;j<edges.size();j++){
         if(i==j)continue;
         auto k=prior;
         auto [a,b]=edges[i];
         k[a]=k[b]=k[a]|k[b];
         auto [c,d]=edges[j];
         k[c]=k[d]=k[c]|k[d];
         save(k);out.explored++;
       }
   }
   return;
  }
  int need=key.req[0]+key.req[1]+key.req[2];
  if(need>2){cerr<<"UNSUPPORTED OPT REQUIREMENT "<<need<<"\n";exit(2);}
  for(int x=0;x<m;x++)for(int y=x+1;y<m;y++){
   bool ok=true;for(int g=0;g<3;g++){int count=(grp[x]==g)+(grp[y]==g);if(count<key.req[g])ok=false;}
   if(!ok)continue;
   for(int side=1;side<full;side++)if((side>>x&1)&&!(side>>y&1)){
    array<int,10> k{};
    for(int z=0;z<m;z++)k[z]=(z==x||z==y)?full:((side>>z&1)?side:full^side);
    save(k);out.explored++;
   }
  }
 }
 void walk(int depth,uint32_t used, const array<int,10>&k, int cc){
  out.explored++;
  // For m=7, used edges and all knowledge bits uniquely determine successors.
  if(m>=7 && depth<target-1){
   uint64_t state=0;for(int x=0;x<m;x++)state|=(uint64_t)k[x]<<(7*x);
   if(!seen.insert({used,state}).second)return;
  }
  if(depth==target){out.terminal++;if(cc==1)save(k);return;}
  for(size_t t=0;t<edges.size();t++){
   if(used>>t&1)continue;auto [u,v]=edges[t];
   // Each full collector of a tree must be an endpoint of its last call.
   if(!key.cyc&&depth==target-1){
    bool ok=true;for(int g=0;g<3;g++){int count=(grp[u]==g)+(grp[v]==g);if(count<key.req[g])ok=false;}
    if(!ok)continue;
   }
   if(key.cyc && depth==target-2){
    // After m-2 calls the static contact graph is disconnected, so zero
    // vertices know all m secrets. All mandated collectors must be endpoints
    // of the final two calls. Duplicate endpoints are OVERCOUNTED (safe).
    bool possible=false;
    for(size_t j=0;j<edges.size();j++)if(j!=t && !(used>>j&1)){
     int n[3]={};
     for(int w:{u,v,edges[j].first,edges[j].second})n[grp[w]]++;
     bool ok=true;for(int g=0;g<3;g++)if(n[g]<key.req[g])ok=false;
     if(ok){possible=true;break;}
    }
    if(!possible)continue;
   }
   array<int,10> next=k;next[u]=next[v]=k[u]|k[v];
   int comps=0;
   int parent[10];for(int i=0;i<m;i++)parent[i]=i;
   auto root=[&](int a){while(parent[a]!=a)a=parent[a];return a;};
   uint32_t nextused=used|(1U<<t);
   for(size_t ei=0;ei<edges.size();ei++)if(nextused>>ei&1){
    auto [a,b]=edges[ei];parent[root(a)]=root(b);
   }
   for(int i=0;i<m;i++)comps+=root(i)==i;
   if(!key.cyc && comps<m-depth-1)continue;
   if(key.cyc && comps<m-depth-2)continue;
   walk(depth+1,nextused,next,comps);
  }
 }
 Domain run(){
  if(key.optimistic){opt();}
  else {
   if(m>7){cerr<<"UNSUPPORTED exact m="<<m<<"\n";exit(2);}
   array<int,10> k{};for(int i=0;i<m;i++)k[i]=1<<i;walk(0,0,k,m);
  }
  out.b.assign(B.begin(),B.end());out.d.assign(D.begin(),D.end());return out;
 }
};
int main(int argc,char **argv){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int quick=argc>1?atoi(argv[1]):1;
 unordered_map<Key,Domain,KH> cache;
 auto get=[&](Key k)->Domain&{
  auto it=cache.find(k);if(it!=cache.end())return it->second;
  auto clock=chrono::steady_clock::now();
  Domain d=Oracle(k).run();auto [loc,ins]=cache.emplace(k,move(d));
  cerr<<"local "<<k.g[0]<<k.g[1]<<k.g[2]<<" cyc="<<k.cyc
      <<" req="<<k.req[0]<<k.req[1]<<k.req[2]
      <<" optimistic="<<k.optimistic
      <<" nodes="<<loc->second.explored<<" terminals="<<loc->second.terminal
      <<" valid="<<loc->second.valid
      <<" B="<<loc->second.b.size()<<" D="<<loc->second.d.size()
      <<" secs="<<chrono::duration<double>(chrono::steady_clock::now()-clock).count()<<"\n";
  return loc->second;
 };
 int number,mult,cr,cc,M[3][3];
 while(cin>>number>>mult>>cr>>cc){
  for(int r=0;r<3;r++)for(int c=0;c<3;c++)cin>>M[r][c];
  int rreq[3][3],creq[3][3];
  for(int r=0;r<3;r++)for(int c=0;c<3;c++)rreq[r][c]=creq[r][c]=M[r][c]==1;
  for(int c=0;c<3;c++)if(c!=cc){
   vector<int> singles;
   for(int r=0;r<3;r++)if(M[r][c]==1)singles.push_back(r);
   for(int r=0;r<3;r++)if(!singles.empty()&&M[r][c]!=1)rreq[r][c]=max(rreq[r][c],1);
   if(singles.size()==2)for(int r=0;r<3;r++)if(M[r][c]!=1){
    if(M[r][c]==2)rreq[r][c]=2;
    else if(M[r][c]==3)rreq[r][c]=max(rreq[r][c],1);
   }
  }
  for(int r=0;r<3;r++)if(r!=cr){
   vector<int> singles;
   for(int c=0;c<3;c++)if(M[r][c]==1)singles.push_back(c);
   for(int c=0;c<3;c++)if(!singles.empty()&&M[r][c]!=1)creq[r][c]=max(creq[r][c],1);
   if(singles.size()==2)for(int c=0;c<3;c++)if(M[r][c]!=1){
    if(M[r][c]==2)creq[r][c]=2;
    else if(M[r][c]==3)creq[r][c]=max(creq[r][c],1);
   }
  }
  array<Domain*,3> rows{},cols{};bool locallyunsat=false,relax=false;
  for(int r=0;r<3;r++){
   Key k{};
   for(int c=0;c<3;c++){k.g[c]=M[r][c];k.req[c]=rreq[r][c];}
   k.cyc=r==cr;
   k.optimistic=quick && ((!k.cyc && k.g[0]+k.g[1]+k.g[2]>=7) ||
                               (k.cyc && k.g[0]+k.g[1]+k.g[2]>=8));
   rows[r]=&get(k);relax|=k.optimistic;
   if(rows[r]->b.empty())locallyunsat=true;
  }
  for(int c=0;c<3;c++){
   Key k{};
   for(int r=0;r<3;r++){k.g[r]=M[r][c];k.req[r]=creq[r][c];}
   k.cyc=c==cc;
   k.optimistic=quick && ((!k.cyc && k.g[0]+k.g[1]+k.g[2]>=7) ||
                               (k.cyc && k.g[0]+k.g[1]+k.g[2]>=8));
   cols[c]=&get(k);relax|=k.optimistic;
   if(cols[c]->d.empty())locallyunsat=true;
  }
  bool sat=false;uint64_t proposals=0;
  if(!locallyunsat){
   // Suffix-first: exact compatibility test B_rj & D_jr == D_jr.
   for(auto &d0:cols[0]->d)for(auto &d1:cols[1]->d)for(auto &d2:cols[2]->d){
    proposals++;bool rowok=true;
    for(int r=0;r<3&&rowok;r++){
     bool ok=false;for(auto &p:rows[r]->b)
      if((p.b[0]&d0.b[r])==d0.b[r]&&(p.b[1]&d1.b[r])==d1.b[r]
          &&(p.b[2]&d2.b[r])==d2.b[r]){ok=true;break;}
     if(!ok)rowok=false;
    }
    if(rowok){sat=true;break;}
   }
  }
  cout<<"CASE "<<number<<" mult="<<mult<<" status="
      <<(locallyunsat?"LOCAL_UNSAT":(sat?"RELAXED_SAT":"PROFILE_UNSAT"))
      <<" optimistic="<<relax<<" combinations="<<proposals<<" rows=";
  for(auto d:rows)cout<<d->b.size()<<",";
  cout<<" cols=";for(auto d:cols)cout<<d->d.size()<<",";
  cout<<"\n"<<flush;
 }
 if(argc>2){
  vector<Key> ks;for(auto &[k,d]:cache)ks.push_back(k);
  sort(ks.begin(),ks.end(),[](Key const &a,Key const &b){
   return make_tuple(a.g,a.req,a.cyc,a.optimistic)<make_tuple(b.g,b.req,b.cyc,b.optimistic);
  });
  for(Key k:ks){
   Domain &dom=cache.at(k);
   sort(dom.b.begin(),dom.b.end(),[](Profile const&a,Profile const&b){return a.b<b.b;});
   sort(dom.d.begin(),dom.d.end(),[](Profile const&a,Profile const&b){return a.b<b.b;});
   cout<<"DOMAIN";for(int x:k.g)cout<<" "<<x;for(int x:k.req)cout<<" "<<x;
   cout<<" "<<int(k.cyc)<<" "<<int(k.optimistic)
       <<" "<<dom.b.size()<<" "<<dom.d.size()<<"\n";
   for(auto &p:dom.b)cout<<"B "<<p.b[0]<<" "<<p.b[1]<<" "<<p.b[2]<<"\n";
   for(auto &p:dom.d)cout<<"D "<<p.b[0]<<" "<<p.b[1]<<" "<<p.b[2]<<"\n";
   cout<<"END\n";
  }
 }
}