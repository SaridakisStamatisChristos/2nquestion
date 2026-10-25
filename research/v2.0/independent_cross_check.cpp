// Independent C++ check of final n14 row-tree vs column-unicyclic obstruction.
#include <bits/stdc++.h>
using namespace std;using Edge=pair<int,int>;
vector<Edge> cells;vector<int> P,Q;
vector<vector<Edge>> domain(bool left){
  const auto& G=left?P:Q;int target=left?4:5;vector<Edge> edges;
  for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)edges.emplace_back(G[i],G[j]);
  vector<vector<Edge>> answer;vector<Edge> seq;int need[3];
  if(left){need[0]=1;need[1]=1;need[2]=0;}
  else{need[0]=2;need[1]=1;need[2]=1;}
  function<void(int)> dfs=[&](int used){
    if((int)seq.size()==target){
      int p[14];iota(p,p+14,0);
      auto rt=[&](int x){while(p[x]!=x)x=p[x];return x;};
      for(auto [a,b]:seq)p[rt(a)]=rt(b);
      for(int v:G)if(rt(v)!=rt(G[0]))return;
      int known[14]={};for(int i=0;i<5;i++)known[G[i]]=1<<i;
      for(int t=0;t<target;t++){
        auto [a,b]=seq[left?t:target-1-t];
        known[a]=known[b]=known[a]|known[b];
      }
      for(int k=0;k<3;k++){
        int u=0,coll=0;
        for(int v:G)if((left?cells[v].second:cells[v].first)==k){
          u|=known[v];coll+=(known[v]==31);
        }
        if(u!=31||coll<need[k])return;
      }
      answer.push_back(seq);return;
    }
    for(int k=0;k<10;k++)if(!(used>>k&1)){
      seq.push_back(edges[k]);dfs(used|(1<<k));seq.pop_back();
    }
  };dfs(0);return answer;
}
int main(){
  int m[3][3]={{1,1,2},{1,2,2},{2,2,1}};
  for(int r=0;r<3;r++)for(int c=0;c<3;c++)for(int j=0;j<m[r][c];j++)cells.emplace_back(r,c);
  assert(cells.size()==14);
  for(int i=0;i<14;i++){if(cells[i].first==1)P.push_back(i);if(cells[i].second==2)Q.push_back(i);}
  auto A=domain(true),B=domain(false);assert(A.size()==48&&B.size()==288);
  long long dup=0,miss=0,found=0;
  for(auto& x:A){
    int state[14]={};for(int j=0;j<5;j++)state[P[j]]=1<<j;
    for(auto [a,b]:x)state[a]=state[b]=state[a]|state[b];
    for(auto& y:B){
      bool clash=false;
      for(auto [a,b]:x)for(auto [u,v]:y)
        if(min(a,b)==min(u,v)&&max(a,b)==max(u,v))clash=true;
      if(clash){dup++;continue;}
      int z[14];copy(state,state+14,z);
      for(auto [a,b]:y)z[a]=z[b]=z[a]|z[b];
      bool okay=true;for(int v:Q)if(z[v]!=31)okay=false;
      if(okay)found++;else miss++;
    }
  }
  assert(dup==0&&miss==13824&&found==0);
  cout<<"PASS independent C++: 48 x 288 = 13824 incompatible local order pairs\n";
}
