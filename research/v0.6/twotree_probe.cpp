// Search edge-order schedules K6 for which no spanning 2-tree footprint is a temporal spanner.
#include <bits/stdc++.h>
using namespace std;
int n=6,m=15; vector<pair<int,int>> edges;
bool is_tc(const vector<int>& ord,uint32_t mask){
  uint32_t x[6];for(int i=0;i<6;i++)x[i]=1<<i;
  for(auto t:ord)if(mask>>t&1){auto [u,v]=edges[t];uint32_t z=x[u]|x[v];x[u]=x[v]=z;}
  for(int i=0;i<6;i++)if(x[i]!=63)return false;return true;
}
bool is_two_tree(uint32_t mask){
  // can repeatedly remove vertex with degree exactly 2 whose neighbours are adjacent,
  // finally triangle. Need some ordering (recursive branching) because choices can differ.
  auto recursive=[&](auto&&self, int active)->bool{
    if(__builtin_popcount((unsigned)active)==3){
       for(int k=0;k<m;k++){
         auto [u,v]=edges[k];if((active>>u&1)&&(active>>v&1)&&!(mask>>k&1))return false;
       }return true;
    }
    for(int v=0;v<n;v++)if(active>>v&1){
      int nei=0;
      for(int k=0;k<m;k++)if(mask>>k&1){auto [a,b]=edges[k];
        if(a==v&&(active>>b&1))nei|=1<<b;
        if(b==v&&(active>>a&1))nei|=1<<a;
      }
      if(__builtin_popcount((unsigned)nei)!=2)continue;
      int a=__builtin_ctz((unsigned)nei),b=31-__builtin_clz((unsigned)nei);
      bool adjacent=false;
      for(int k=0;k<m;k++)if(mask>>k&1){auto [x,y]=edges[k];if((x==a&&y==b)||(x==b&&y==a))adjacent=true;}
      if(adjacent&&self(self,active&~(1<<v)))return true;
    }
    return false;
  };
  return recursive(recursive,(1<<n)-1);
}
int main(int argc,char**argv){int samples=argc>1?atoi(argv[1]):10000;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
 vector<uint32_t> two;for(uint32_t mask=0;mask<(1U<<m);mask++)if(__builtin_popcount(mask)==9&&is_two_tree(mask))two.push_back(mask);
 fprintf(stderr,"2-trees=%zu\n",two.size());
 mt19937_64 rng(20261025);vector<int> ord(m);iota(ord.begin(),ord.end(),0);
 for(int s=0;s<samples;s++){
   shuffle(ord.begin(),ord.end(),rng);
   bool found=false;for(auto mask:two)if(is_tc(ord,mask)){found=true;break;}
   if(!found){
     int best=m;uint32_t bestMask=0;
     for(uint32_t mask=0;mask<(1U<<m);mask++){
       int bits=__builtin_popcount(mask);if(bits>=best)continue;
       if(is_tc(ord,mask)){best=bits;bestMask=mask;}
     }
     cout<<"NON_2_TREE_WITNESS n=6 sample="<<s<<" optimum="<<best<<" chronology=";
     for(int a:ord){auto [u,v]=edges[a];cout<<"("<<u<<","<<v<<") ";}
     cout<<"spanner_mask="<<bestMask<<"\n";return 0;
   }
 }
 cout<<"ALL "<<samples<<" K6 sampled orders have spanning 2-tree temporal spanner\n";
}
