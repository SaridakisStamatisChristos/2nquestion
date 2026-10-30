// Stage 9 adversarial targeted n18 test; all 3x3 intersection cells size2.
// Exhaustively simulate every ordered distinct 5-contact (tree) and 6-contact
// (unicyclic) history on six vertices, retain CONNECTED contact components
// whose three labelled pairs each collectively know all six local secrets.
// Compute exact B/D bitset domains independently of older v2.3 machinery.
// Unsatisfiability of the relaxed 3x3 row/column CSP excludes this specific
// incidence matrix, NOT all n18 configurations or the universal conjecture.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
struct Domain{vector<uint32_t>B,D;uint64_t terminal=0,valid=0;};
uint32_t pack(const array<unsigned,3>&z){return z[0]|(z[1]<<8)|(z[2]<<16);}
int coord(uint32_t p,int c){return (p>>(8*c))&255;}
Domain get(bool cyclic){
 constexpr int n=6,all=63;
 const int target=5+int(cyclic);
 pair<int,int> edges[15];int ec=0;
 for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)edges[ec++]={u,v};
 unordered_set<uint32_t>BS,DS;Domain out;
 auto dfs=[&](auto&&self,int depth,uint16_t used,array<uint8_t,6>k)->void{
  if(depth==target){
   out.terminal++;
   int par[6];for(int i=0;i<n;i++)par[i]=i;
   auto root=[&](int x){while(par[x]!=x)x=par[x];return x;};
   for(int j=0;j<15;j++)if(used>>j&1){
    auto[a,b]=edges[j];par[root(a)]=root(b);
   }
   for(int i=1;i<n;i++)if(root(i)!=root(0))return;
   for(int g=0;g<3;g++)if((k[2*g]|k[2*g+1])!=all)return;
   out.valid++;
   array<unsigned,3>b{},d{};
   for(int g=0;g<3;g++){
    b[g]=8;
    if(k[2*g]==all)b[g]|=2;
    if(k[2*g+1]==all)b[g]|=4;
    for(int secret=0;secret<n;secret++){
     int subset=((k[2*g]>>secret)&1)|
                (((k[2*g+1]>>secret)&1)<<1);
     d[g]|=1<<subset;
    }
   }
   BS.insert(pack(b));DS.insert(pack(d));return;
  }
  for(int j=0;j<15;j++)if(!(used>>j&1)){
   auto[a,b]=edges[j];auto next=k;
   next[a]=next[b]=k[a]|k[b];
   self(self,depth+1,used|(1<<j),next);
  }
 };
 array<uint8_t,6>k{};for(int i=0;i<n;i++)k[i]=1<<i;
 dfs(dfs,0,0,k);
 out.B.assign(BS.begin(),BS.end());out.D.assign(DS.begin(),DS.end());
 sort(out.B.begin(),out.B.end());sort(out.D.begin(),out.D.end());
 return out;
}
int main(){
 const Domain tree=get(false),cyc=get(true);
 if(tree.terminal!=360360||tree.valid!=4992||tree.B.size()!=13||
    tree.D.size()!=15||cyc.terminal!=3603600||cyc.valid!=369312||
    cyc.B.size()!=48||cyc.D.size()!=69){
  cerr<<"FAIL local exhaustive-domain regression\n";return 2;
 }
 cout<<"PASS exact 6-person tree chronology: "<<tree.terminal
     <<" histories, "<<tree.valid<<" covering, B="<<tree.B.size()
     <<" D="<<tree.D.size()<<"\n";
 cout<<"PASS exact 6-person cyclic chronology: "<<cyc.terminal
     <<" histories, "<<cyc.valid<<" covering, B="<<cyc.B.size()
     <<" D="<<cyc.D.size()<<"\n";
 uint64_t tried=0,feasible=0;
 // By simultaneous row/column relabeling all cyclic-row/column marked
 // choices in the all-2 matrix reduce to (row=0,column=0).
 for(uint32_t br0:cyc.B)for(uint32_t br1:tree.B)
  for(uint32_t br2:tree.B){
   ++tried;const uint32_t rows[]={br0,br1,br2};
   bool possible=true;
   for(int c=0;c<3;c++){
    bool one=false;
    const auto& domain=(c==0)?cyc.D:tree.D;
    for(uint32_t q:domain){
     bool cellok=true;
     for(int r=0;r<3;r++)if((coord(rows[r],c)&coord(q,r))!=coord(q,r)){
      cellok=false;break;
     }
     if(cellok){one=true;break;}
    }
    if(!one){possible=false;break;}
   }
   if(possible)feasible++;
  }
 if(tried!=8112||feasible!=0){
  cerr<<"FAIL all-two-cells n18 compatibility: "<<tried
      <<" trials, "<<feasible<<" feasible\n";return 3;
 }
 cout<<"PASS targeted n18 3x3 all-cell-sizes-two: 8112 exact row B profile"
        " combinations, zero sound relaxed cross-half compatibility matches\n";
 cout<<"LIMIT: one n18 incidence family excluded, not all n18, NOT all-n\n";
}
