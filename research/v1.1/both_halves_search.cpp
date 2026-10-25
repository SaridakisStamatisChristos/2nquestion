// Heuristic falsifier for the stronger conjecture: at least one half is a forest.
// All candidate protocols have 2n-4 distinct calls and are checked for success.
#include <bits/stdc++.h>
using namespace std;
struct X{
 int n,k,m;mt19937_64 rng; vector<pair<int,int>> edges;vector<int> schedule;
 X(int N,uint64_t seed):n(N),k(2*N-4),m(N*(N-1)/2),rng(seed){
 for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edges.push_back({a,b});
 auto ix=[&](int a,int b){if(a>b)swap(a,b);return a*(2*n-a-1)/2+b-a-1;};
 vector<pair<int,int>> base={{0,1},{4,5},{3,7},{2,6},{2,3},{1,5},{0,4},{1,2},{6,7},{4,6},{3,5},{0,7}};
 for(auto [a,b]:base)schedule.push_back(ix(a,b));
 for(int v=8;v<n;v++){schedule.insert(schedule.begin(),ix(v,0));schedule.push_back(ix(v,1));}
 }
 bool connected()const{
 vector<uint64_t> info(n);for(int i=0;i<n;i++)info[i]=1ull<<i;
 for(auto j:schedule){auto[a,b]=edges[j];info[a]|=info[b];info[b]=info[a];}
 for(auto w:info)if(w!=((1ull<<n)-1))return false;
 return true;
 }
 int cycles(bool first)const{
 vector<int>p(n);iota(p.begin(),p.end(),0);
 auto root=[&](int x){while(p[x]!=x)x=p[x];return x;};
 int cnt=0;
 for(int t=first?0:k/2;t<(first?k/2:k);t++){
 auto [a,b]=edges[schedule[t]];int x=root(a),y=root(b);
 if(x==y)cnt++;else p[x]=y;
 }
 return cnt;
 }
 void run(int limit){
 assert(connected());int c1=cycles(true),c2=cycles(false);int best=min(c1,c2),accepts=0;
 uniform_real_distribution<double>unit(0,1);
 for(int t=0;t<limit;t++){
 auto prev=schedule;
 if(rng()%4<=1){int a=rng()%k,b=rng()%k;swap(schedule[a],schedule[b]);}
 else {int a=rng()%k,b=rng()%m; if(find(schedule.begin(),schedule.end(),b)==schedule.end())schedule[a]=b;}
 if(!connected()){schedule=prev;continue;}
 int a=cycles(true),b=cycles(false);
 if(a>0&&b>0){cout<<"BOTH_CYCLIC n="<<n<<" t="<<t<<" first="<<a<<" last="<<b<<"\n";for(auto j:schedule)cout<<edges[j].first<<","<<edges[j].second<<" ";cout<<"\n";return;}
 double temp=.15 + (1.0-1.0*(t%100000)/100000.0)*.85;
 double delta=(min(a,b)-min(c1,c2))*8.0 + ((a+b)-(c1+c2))*0.25;
 if(delta>=0||unit(rng)<exp(delta/temp)){c1=a;c2=b;accepts++;best=max(best,min(a,b));}else schedule=prev;
 }
 cout<<"NONE n="<<n<<" steps="<<limit<<" accepts="<<accepts<<" best="<<best<<" final="<<c1<<","<<c2<<"\n";
 }
};
int main(int argc,char**argv){int n=atoi(argv[1]),steps=atoi(argv[2]);X(n,20261025+n).run(steps);}
