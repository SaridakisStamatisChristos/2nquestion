// Deterministic local search for difficult non-pivotable K9 temporal cliques.
// Heuristic-only: no counterexample to POD or 2n-3 is certified by a failure.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
const int N=9,M=36;
vector<pair<int,int>> edge;
using Order=array<int,M>;
U full=(1ull<<N)-1;
bool connected(const Order& order,U mask){
 U info[N];for(int i=0;i<N;i++)info[i]=U(1)<<i;
 for(int j=0;j<M;j++)if((mask>>j)&1){auto [a,b]=edge[order[j]];U q=info[a]|info[b];info[a]=info[b]=q;}
 for(int i=0;i<N;i++)if(info[i]!=full)return false;return true;
}
bool pivot(const Order& order){
 U info[N];for(int i=0;i<N;i++)info[i]=U(1)<<i;
 for(int t=0;t<M;t++){
  auto [a,b]=edge[order[t]];
  if((info[a]|info[b])==full){
   U spread=(U(1)<<a)|(U(1)<<b);
   for(int j=t+1;j<M;j++){
    auto [x,y]=edge[order[j]];
    if(spread & ((U(1)<<x)|(U(1)<<y)))spread|=(U(1)<<x)|(U(1)<<y);
   }
   if(spread==full)return true;
  }
  U q=info[a]|info[b];info[a]=info[b]=q;
 }
 return false;
}
int greedy(const Order& order,const Order& deletion){
 U mask=(U(1)<<M)-1;
 for(int j:deletion){U q=mask & ~(U(1)<<j);if(connected(order,q))mask=q;}
 return __builtin_popcountll(mask);
}
int main(int argc,char**argv){
 int iters=argc>1?stoi(argv[1]):50000;
 unsigned seed=argc>2?stoul(argv[2]):2100825;
 mt19937 rng(seed);
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)edge.emplace_back(a,b);
 vector<Order> deletions(24);
 for(auto& d:deletions){iota(d.begin(),d.end(),0);shuffle(d.begin(),d.end(),rng);}
 auto score=[&](const Order& s){
  if(pivot(s))return -10000;
  int best=M;
  for(auto &del:deletions)best=min(best,greedy(s,del));
  return best;
 };
 Order current; iota(current.begin(),current.end(),0);shuffle(current.begin(),current.end(),rng);
 int current_score=score(current);if(current_score<0){current_score=-10000;}
 int best_score=-10000;Order best=current;
 for(int i=0;i<iters;i++){
  if(i%5000==0 || current_score<0){shuffle(current.begin(),current.end(),rng);current_score=score(current);}
  Order trial=current;
  int x=rng()%M,y=rng()%M;swap(trial[x],trial[y]);
  int trial_score=score(trial);
  if(trial_score>best_score){best=trial;best_score=trial_score;cerr<<"new best "<<i<<" score="<<best_score<<"\n";}
  if(trial_score>=current_score || (trial_score>=0 && (rng()%1000)<3)){
   current=trial;current_score=trial_score;
  }
 }
 cout<<"seed "<<seed<<" iterations "<<iters<<" best_24_start_score "<<best_score<<" nonpivot "<<(!pivot(best))<<"\n";
 for(auto e:best){auto [a,b]=edge[e];cout<<a<<" "<<b<<"\n";}
}
