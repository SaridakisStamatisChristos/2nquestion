// Exploratory n14 counterexample hunt ONLY; not a proof of nonexistence.
// Schedule is always 24 pairwise-distinct *unordered* contacts;
// gossip and both half cycle ranks checked on every candidate.
#include <bits/stdc++.h>
using namespace std;
using Edge=pair<int,int>;
uint64_t rng=20261025;
uint64_t nextint(){rng^=rng<<7;rng^=rng>>9;return rng;}
double unit(){return (nextint()%10000000)*1e-7;}
constexpr int n=14,m=2*n-4;
vector<Edge> starting(){
 vector<Edge> s={{0,1},{4,5},{3,7},{2,6},{2,3},{1,5},
                  {0,4},{1,2},{6,7},{4,6},{3,5},{0,7}};
 for(int v=8;v<n;v++){s.insert(s.begin(),{0,v});s.push_back({1,v});}
 return s;
}
int rankHalf(const vector<Edge>&s,int begin,int end){
 int p[n];iota(p,p+n,0);
 auto root=[&](int i){while(p[i]!=i)i=p[i];return i;};
 int rank=0;
 for(int i=begin;i<end;i++){
   int a=root(s[i].first),b=root(s[i].second);
   if(a==b)rank++;else p[a]=b;
 }
 return rank;
}
struct Result{int missing,left,right;double loss;};
Result evaluate(const vector<Edge>&s){
 unsigned masks[n];for(int i=0;i<n;i++)masks[i]=1u<<i;
 for(auto [u,v]:s){unsigned x=masks[u]|masks[v];masks[u]=masks[v]=x;}
 int missing=0;for(unsigned a:masks)missing+=n-__builtin_popcount(a);
 int a=rankHalf(s,0,n-2),b=rankHalf(s,n-2,m);
 return {missing,a,b,missing*2.5+(a==0?11:0)+(b==0?11:0)};
}
int main(int argc,char**argv){
 long long limit=5000000;
 if(argc>1)limit=atoll(argv[1]);
 vector<Edge> cur=starting(),best=cur;
 auto sc=evaluate(cur),bestsc=sc;
 cerr<<"start "<<sc.missing<<" "<<sc.left<<" "<<sc.right<<"\n";
 for(long long k=0;k<limit;k++){
  if(k%1000000==0)cerr<<"epoch="<<k/1000000<<" best="<<bestsc.loss
    <<" missing="<<bestsc.missing<<" ranks="<<bestsc.left<<","<<bestsc.right<<"\n";
  auto trial=cur;
  int t=nextint()%100;
  if(t<60){int a=nextint()%m,b=nextint()%m;if(a==b)continue;swap(trial[a],trial[b]);}
  else if(t<85){int a=nextint()%m,b=a+1+(nextint()%4);if(b>=m)b-=m;swap(trial[a],trial[b]);}
  else {
   int a=nextint()%m,u=nextint()%n,v=nextint()%n;
   if(u==v)continue;if(u>v)swap(u,v);
   bool dup=false;for(int j=0;j<m;j++)if(j!=a&&trial[j]==Edge(u,v))dup=true;
   if(dup)continue;trial[a]={u,v};
  }
  auto next=evaluate(trial);
  if(next.missing==0&&next.left>0&&next.right>0){
    set<Edge>distinct(trial.begin(),trial.end());
    if((int)distinct.size()!=m)abort();
    cout<<"FOUND "<<k<<"\n";
    for(auto [u,v]:trial)cout<<u<<" "<<v<<"\n";
    return 0;
  }
  if(next.loss<bestsc.loss){bestsc=next;best=trial;}
  double T=1.5+2.5*(1.0-((k%250000)/250000.0));
  if(next.loss<=sc.loss||unit()<exp((sc.loss-next.loss)/T)){cur=trial;sc=next;}
  if(k%250000==249999){cur=(nextint()%3==0)?best:starting();sc=evaluate(cur);}
 }
 cout<<"NO_WITNESS_IN_BOUNDED_SEARCH "<<limit<<" steps best="
     <<bestsc.loss<<" missing="<<bestsc.missing
     <<" first="<<bestsc.left<<" last="<<bestsc.right<<"\n";
}
