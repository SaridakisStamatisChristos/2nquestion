// Stage 21: independently enumerate every labelled chronological tree for all
// additional 6- and 7-person group triples needed by the n20 incidence search.
// Complete Prufer enumeration, ALL original edge orders with the final edge
// crossing the first two designated corner groups; bitset union-call replay.
// Every group must collectively know every original secret. Count individual
// recipients with an original secret private inside the third group.
// This is a local finite theorem, not a global successful gossip solver.
#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

struct Fixture {
 int a,b,c;
 map<int,long long> expected;
 long long expected_covered;
};

map<int,long long> count_private(int a,int b,int c,long long &ordered,long long &covered){
 const int n=a+b+c, full=(1<<n)-1;
 long long words=1;
 for(int k=0;k<n-2;k++)words*=n;
 map<int,long long> histogram;
 ordered=covered=0;
 for(long long word=0;word<words;word++){
  int degree[8],code[8],edges[8][2];
  fill(degree,degree+n,1);
  auto z=word;
  for(int i=0;i<n-2;i++){
   code[i]=int(z%n);z/=n;degree[code[i]]++;
  }
  for(int i=0;i<n-2;i++){
   int leaf=0;while(degree[leaf]!=1)leaf++;
   edges[i][0]=leaf;edges[i][1]=code[i];
   degree[leaf]--;degree[code[i]]--;
  }
  int u=-1,v=-1;
  for(int i=0;i<n;i++)if(degree[i]==1){
   if(u<0)u=i;else v=i;
  }
  edges[n-2][0]=u;edges[n-2][1]=v;
  for(int last=0;last<n-1;last++){
   const int x=edges[last][0],y=edges[last][1];
   if(!((x<a && y>=a && y<a+b)||(y<a && x>=a && x<a+b)))
    continue;
   int order[8],index=0;
   for(int i=0;i<n-1;i++)if(i!=last)order[index++]=i;
   do{
    ordered++;
    int know[8];
    for(int i=0;i<n;i++)know[i]=1<<i;
    for(int j=0;j<n-2;j++){
     const int t=order[j],p=edges[t][0],q=edges[t][1];
     know[p]=know[q]=know[p]|know[q];
    }
    know[x]=know[y]=know[x]|know[y];
    int group[3]={};
    for(int i=0;i<n;i++)
     group[(i<a)?0:(i<a+b)?1:2]|=know[i];
    if(group[0]!=full||group[1]!=full||group[2]!=full)
     continue;
    covered++;
    int private_count=0;
    for(int recipient=a+b;recipient<n;recipient++){
     bool is_private=false;
     for(int secret=0;secret<n;secret++){
      if(!(know[recipient]&(1<<secret)))continue;
      bool other=false;
      for(int q=a+b;q<n;q++)
       if(q!=recipient && (know[q]&(1<<secret)))other=true;
      if(!other){is_private=true;break;}
     }
     private_count+=is_private;
    }
    histogram[private_count]++;
   }while(next_permutation(order,order+n-2));
  }
 }
 return histogram;
}

int main(){
 const vector<Fixture> cases={
   {1,1,5,{{1,24000},{2,33600}},57600},
   {1,2,4,{{1,9600},{2,59520},{3,9600}},78720},
   {2,1,4,{{1,9600},{2,59520},{3,9600}},78720},
   {1,3,3,{{2,51840},{3,7200}},59040},
   {3,1,3,{{2,51840},{3,7200}},59040},
   {2,2,3,{{2,88320},{3,26880}},115200},
   {1,3,2,{{2,864}},864},
   {3,1,2,{{2,864}},864},
   {2,2,2,{{2,1664}},1664}
 };
 for(const auto &f:cases){
  long long tested=0,covered=0;
  auto histogram=count_private(f.a,f.b,f.c,tested,covered);
  if(histogram!=f.expected||covered!=f.expected_covered){
   cerr<<"FAIL tree privacy triple "<<f.a<<","<<f.b<<","<<f.c
       <<" covered="<<covered<<"\n";
   return 2;
  }
  cout<<"PASS tree "<<f.a<<","<<f.b<<","<<f.c
      <<" original chronological histories="<<tested
      <<" qualifying group covers="<<covered<<" private={";
  for(auto [count,multiplicity]:histogram)
   cout<<count<<":"<<multiplicity<<" ";
  cout<<"}\n";
 }
 cout<<"PASS exact tree privacy counts for ALL n20 additional group triples\n";
 cout<<"Boundary: n7 cases (1,1,5) and (1,2,4) attain just ONE private member\n";
 cout<<"LIMIT: finite local truths only; no n20 global gossip chronology certified\n";
 return 0;
}
