// Exhaustively enumerate commutation classes of temporal cliques K4 and K5,
// and determine whether each class contains a temporally connected 2-tree.
#include <bits/stdc++.h>
using namespace std;
int n,m;vector<pair<int,int>> edges;
bool is_tc(vector<int> const& ord,uint32_t mask){
 uint32_t info[6];for(int i=0;i<n;i++)info[i]=1<<i;
 for(int t:ord)if(mask>>t&1){auto[u,v]=edges[t];uint32_t x=info[u]|info[v];info[u]=info[v]=x;}
 for(int i=0;i<n;i++)if(info[i]!=(1U<<n)-1)return false;return true;
}
bool is_two_tree(uint32_t mask){
 auto f=[&](auto&&self,int active)->bool{
  if(__builtin_popcount((unsigned)active)==3){
   for(int i=0;i<m;i++){auto[u,v]=edges[i];if((active>>u&1)&&(active>>v&1)&&!(mask>>i&1))return false;}return true;
  }
  for(int v=0;v<n;v++)if(active>>v&1){
   int nei=0;for(int i=0;i<m;i++)if(mask>>i&1){auto[u,w]=edges[i];
     if(u==v&&(active>>w&1))nei|=1<<w;
     if(w==v&&(active>>u&1))nei|=1<<u;
   }
   if(__builtin_popcount((unsigned)nei)!=2)continue;
   int a=__builtin_ctz((unsigned)nei),b=31-__builtin_clz((unsigned)nei);
   for(int i=0;i<m;i++)if(mask>>i&1){auto[u,w]=edges[i];
     if((u==a&&w==b)||(u==b&&w==a))if(self(self,active&~(1<<v)))return true;
   }
  }return false;
 };return f(f,(1<<n)-1);
}
int main(int argc,char**argv){n=argc>1?atoi(argv[1]):5; if(n<4||n>5)return 1;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});m=edges.size();
 vector<pair<int,int>> dep;for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
  auto[a,b]=edges[i];auto[c,d]=edges[j];if(a==c||a==d||b==c||b==d)dep.push_back({i,j});
 }
 vector<uint32_t> two;for(uint32_t b=0;b<(1U<<m);b++)if(__builtin_popcount(b)==2*n-3&&is_two_tree(b))two.push_back(b);
 vector<int> ord(m);iota(ord.begin(),ord.end(),0);unordered_set<uint32_t> seen;
 long long total=0, classes=0,bad=0;vector<int> badexample;
 do{
  total++;int pos[10];for(int i=0;i<m;i++)pos[ord[i]]=i;
  uint32_t sig=0;for(int j=0;j<(int)dep.size();j++)if(pos[dep[j].first]<pos[dep[j].second])sig|=uint32_t(1)<<j;
  if(!seen.insert(sig).second)continue;
  classes++;bool works=false;
  for(uint32_t b:two)if(is_tc(ord,b)){works=true;break;}
  if(!works){bad++;if(badexample.empty())badexample=ord;}
 }while(next_permutation(ord.begin(),ord.end()));
 cout<<"K"<<n<<" permutations="<<total<<" traces="<<classes<<" two_tree_masks="<<two.size()<<" traces_with_no_temporal_2_tree="<<bad<<"\n";
 if(!badexample.empty()){
  cout<<"first_bad_order=";for(int j:badexample){auto[u,v]=edges[j];cout<<"("<<u<<","<<v<<") ";}cout<<"\n";
 }
}
