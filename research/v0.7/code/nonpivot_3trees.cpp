#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int N,M; vector<pair<int,int>> ed; int idx[10][10];
U initclique(const vector<int>& S) {U mask=0;for(int a:S) for(int b:S)if(a<b)mask |= U(1)<<idx[a][b];return mask;}
struct S{U mask;int used;};
void rec(U mask,int used,unordered_set<U>& out,int k){
 if(__builtin_popcount((unsigned)used)==N){out.insert(mask);return;}
 vector<int> verts;for(int v=0;v<N;v++)if(used>>v&1)verts.push_back(v);
 for(int v=0;v<N;v++)if(!(used>>v&1)){
  for(int aa=0;aa<(int)verts.size();aa++)for(int bb=aa+1;bb<(int)verts.size();bb++)for(int cc=bb+1;cc<(int)verts.size();cc++){
   int a=verts[aa],b=verts[bb],c=verts[cc];
   if((mask>>idx[a][b]&1)&&(mask>>idx[a][c]&1)&&(mask>>idx[b][c]&1)){
      U x=mask|(U(1)<<idx[min(v,a)][max(v,a)])|(U(1)<<idx[min(v,b)][max(v,b)])|(U(1)<<idx[min(v,c)][max(v,c)]);
      rec(x,used|(1<<v),out,k);
   }
  }
 }
}
bool connected(U mask,const vector<int> &order){
 U info[10];for(int v=0;v<N;v++)info[v]=U(1)<<v;
 for(int i:order) if(mask>>i&1){auto [a,b]=ed[i];U k=info[a]|info[b];info[a]=info[b]=k;}
 U full=(U(1)<<N)-1;for(int v=0;v<N;v++)if(info[v]!=full)return false;
 return true;
}
int main(int argc,char**argv){N=argc>1?atoi(argv[1]):7;int trials=argc>2?atoi(argv[2]):100;int seed=argc>3?atoi(argv[3]):271828;for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){idx[a][b]=idx[b][a]=ed.size();ed.push_back({a,b});}M=ed.size();
 unordered_set<U> out;int k=3;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){
  vector<int>S={a,b,c,d};rec(initclique(S),(1<<a)|(1<<b)|(1<<c)|(1<<d),out,k);
 }
 vector<U> trees(out.begin(),out.end());sort(trees.begin(),trees.end());cerr<<"n="<<N<<" candidates="<<trees.size()<<"\n";

 mt19937 rng(seed);vector<int> order(M);iota(order.begin(),order.end(),0);
 auto pivot=[&](const vector<int>& tim){
  U info[10];for(int i=0;i<N;i++) info[i]=U(1)<<i;
  U full=(U(1)<<N)-1;
  for(int t=0;t<M;t++){
   auto [a,b]=ed[tim[t]];
   if((info[a]|info[b])==full){
    U x=(U(1)<<a)|(U(1)<<b);
    for(int j=t+1;j<M;j++){auto [c,d]=ed[tim[j]];if((x>>c&1)||(x>>d&1))x|=(U(1)<<c)|(U(1)<<d);}
    if(x==full)return t+1;
   }
   U k=info[a]|info[b];info[a]=info[b]=k;
  }
  return 0;
 };
 int nonpivot=0,pivots=0,minnp=INT_MAX,maxnp=0;vector<int> best_np;
 auto begin=chrono::steady_clock::now();
 for(int t=0;t<trials;t++){
  shuffle(order.begin(),order.end(),rng);
  int p=pivot(order);if(p){pivots++;continue;}
  nonpivot++;int hits=0;for(U mask:trees) hits+=connected(mask,order);
  if(hits<minnp){minnp=hits;best_np=order;}
  maxnp=max(maxnp,hits);
  if(hits==0){cerr<<"REFUTED n="<<N<<" t="<<t<<"\n";break;}
 }
 cerr<<"RESULT n="<<N<<" trials="<<trials<<" pivots="<<pivots<<" nonpivot="<<nonpivot<<" nonpivot_min3trees="<<minnp<<" nonpivot_max3trees="<<maxnp<<"\n";
 for(int i:best_np){auto [a,b]=ed[i];cerr<<"("<<a<<","<<b<<") ";}cerr<<"\n";
}
