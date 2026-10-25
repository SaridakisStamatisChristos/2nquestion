// Minimum-length gossip protocol search for butterfly-free schedules.
// Useful as a falsifier: no claim of general theorem from negative searches.
#include <bits/stdc++.h>
using namespace std;
struct Search {
 int n,k,m; mt19937_64 rng; vector<pair<int,int>> all; vector<array<int,4>> cycles;
 Search(int N,unsigned seed):n(N),k(2*n-4),m(n*(n-1)/2),rng(seed){
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)all.push_back({i,j});
  auto ix=[&](int a,int b){if(a>b)swap(a,b);return a*(2*n-a-1)/2+(b-a-1);};
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)for(int d=c+1;d<n;d++){
   cycles.push_back({ix(a,b),ix(b,c),ix(c,d),ix(a,d)});
   cycles.push_back({ix(a,b),ix(b,d),ix(c,d),ix(a,c)});
   cycles.push_back({ix(a,c),ix(b,c),ix(b,d),ix(a,d)});
  }
 }
 int edge(int a,int b)const{if(a>b)swap(a,b);return a*(2*n-a-1)/2+(b-a-1);}
 bool connected(const vector<int>&seq) const {
  vector<uint32_t> know(n);
  for(int i=0;i<n;i++)know[i]=1u<<i;
  for(int t:seq){auto [a,b]=all[t];auto p=know[a]|know[b];know[a]=know[b]=p;}
  for(auto mask:know)if(mask!=((1u<<n)-1u))return false;
  return true;
 }
 int count(const vector<int>&seq)const{
  vector<int> pos(m,999);for(int i=0;i<k;i++)pos[seq[i]]=i;
  int ans=0;
  for(auto cy:cycles){
   array<int,4> p={pos[cy[0]],pos[cy[1]],pos[cy[2]],pos[cy[3]]};
   if(p[0]>=k||p[1]>=k||p[2]>=k||p[3]>=k)continue;
   // order within 4 cycle; opposite pair -> first two and last two calls disjoint
   // cycles[0],cycles[2] opposite; cycles[1],cycles[3] opposite.
   if(max(p[0],p[2])<min(p[1],p[3]) || max(p[1],p[3])<min(p[0],p[2]))ans++;
  }
  return ans;
 }
 vector<int> initial()const{
  vector<int> seq;
  for(int x=4;x<n;x++)seq.push_back(edge(0,x));
  seq.push_back(edge(0,1));seq.push_back(edge(2,3));seq.push_back(edge(0,2));seq.push_back(edge(1,3));
  for(int x=4;x<n;x++)seq.push_back(edge(3,x));
  return seq;
 }
 void go(int iter){
  auto seq=initial();if(!connected(seq)){cerr<<"Bad seed";exit(1);}
  int now=count(seq),best=now;long accepted=0;
  uniform_real_distribution<double> unit(0,1);
  for(int t=0;t<iter;t++){
   auto old=seq;int typ=rng()%4;
   if(typ==0 || typ==1){int a=rng()%k,b=rng()%k;swap(seq[a],seq[b]);}
   else {int a=rng()%k;int x=rng()%m;bool duplicate=false;for(int e:seq)if(e==x)duplicate=true;if(!duplicate)seq[a]=x;}
   if(!connected(seq)){seq=old;continue;}
   int score=count(seq);
   double T=0.2 + 2.0*(1.0-(t%100000)/100000.0);
   if(score<=now || unit(rng)<exp((now-score)/T)){
    now=score;accepted++;
    if(now<best){best=now;cerr<<"n="<<n<<" iteration="<<t<<" minimum butterflies="<<best<<"\n";}
    if(best==0){
     cout<<"COUNTEREXAMPLE n="<<n<<" steps="<<t<<"\n";
     for(auto e:seq)cout<<all[e].first<<" "<<all[e].second<<"\n";
     return;
    }
   }else seq=old;
  }
  cout<<"SURVIVED n="<<n<<" steps="<<iter<<" accepted="<<accepted<<" best_butterflies="<<best<<"\n";
 }
};
int main(int argc,char**argv){int n=argc>1?atoi(argv[1]):8,it=argc>2?atoi(argv[2]):500000;Search(n,20261025+n).go(it);}
