// Independent original-order adversarial oracle for 3- and 4-leaf
// exact midpoint star supports opposed to a chronological tree whose
// FINAL edge is outside the shared B-cell.
//
// n=6: B vertices 2..5, pairs {2,3},{2,4},{2,5}
// n=7: B vertices 2..6, pairs {2,3},{2,4},{2,5},{2,6}
//
// It checks complete temporal compatibility, and never assumes the
// input is a successful global gossip schedule. No imported project oracle.
#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int main(){
 for(int n=6;n<=7;n++){
  long long words=1;for(int i=0;i<n-2;i++)words*=n;
  long long trees=0,histories=0,collective=0,crossing=0;
  for(long long id=0;id<words;id++){
   long long work=id;
   array<int,8> deg{};for(int i=0;i<n;i++)deg[i]=1;
   array<int,8> code{};
   for(int i=0;i<n-2;i++){code[i]=work%n;work/=n;deg[code[i]]++;}
   vector<pair<int,int>> edges;
   for(int i=0;i<n-2;i++){
    int leaf=0;while(deg[leaf]!=1)leaf++;
    edges.push_back(minmax(leaf,code[i]));
    deg[leaf]--;deg[code[i]]--;
   }
   int first=-1,second=-1;
   for(int j=0;j<n;j++)if(deg[j]==1){if(first<0)first=j;else second=j;}
   edges.push_back(minmax(first,second));
   auto finaledge=find(edges.begin(),edges.end(),pair<int,int>{0,1});
   if(finaledge==edges.end())continue;
   trees++;
   edges.erase(finaledge);
   vector<int> order(n-2);iota(order.begin(),order.end(),0);
   do{
    histories++;
    array<int,8> know{};
    for(int i=0;i<n;i++)know[i]=1<<i;
    for(int t:order){
      auto [a,b]=edges[t];
      know[a]=know[b]=know[a]|know[b];
    }
    know[0]=know[1]=know[0]|know[1];
    int total=0;
    for(int j=2;j<n;j++)total|=know[j];
    collective+=(total==(1<<n)-1);
    // Four (respectively three) star supports are source-side
    // carrier sets {2,z}. Each target-side original secret must
    // cross every source support at the fixed midpoint.
    bool compatible=true;
    for(int secret=0;secret<n;secret++){
      int bit=1<<secret;
      if(know[2]&bit)continue;
      for(int z=3;z<n;z++)if(!(know[z]&bit))compatible=false;
    }
    crossing+=compatible;
   }while(next_permutation(order.begin(),order.end()));
  }
  long long expected_trees=2*words/n;
  long long expected_histories=expected_trees;
  for(int i=2;i<n-1;i++)expected_histories*=i;
  if(trees!=expected_trees||histories!=expected_histories||crossing!=0){
   cerr<<"FAIL n="<<n<<" treeCount="<<trees<<" orders="<<histories
       <<" starCross="<<crossing<<"\n";return 2;
  }
  cout<<"PASS n="<<n<<" labelled trees with last (0,1)="<<trees
      <<" original-order tree histories="<<histories
      <<" B collective covers="<<collective
      <<"  "<<(n-3)<<"-leaf compatible histories="<<crossing<<"\n";
 }
 cout<<"VERDICT: exact chronological tree-versus-star crossing impossible; "
     <<"not a full 36-contact gossip enumeration\n";
}
