// Stage 17: exact n=8 original-order LOCAL unicyclic 2/2/1 cover check.
// Exhaust every labelled spanning tree not containing final edge (0,a)
// using all 8^6 Prufer codes; quotient only STATIC TREE topology by vertex
// permutations within the groups that FIX endpoints 0 and a.
// Then replay ALL 7! chronological edge orders on each canonical tree.
// This reduction is exact because the support predicate is label invariant.
// This is not a global two-half gossip solver.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;
using Edge=pair<int,int>;
int edge_index(int x,int y){
 if(x>y)swap(x,y);
 return x*(15-x)/2+(y-x-1);
}
void perms_range(int start,int finish,vector<vector<int>>&out){
 vector<int> v;
 for(int i=start;i<finish;i++)v.push_back(i);
 do{out.push_back(v);}while(next_permutation(v.begin(),v.end()));
}
struct Counts{long long trees=0,orbits=0,orders=0,passing=0;};
Counts check(int a,int b){
 const int n=8;
 const int c=n-a-b;
 if(a<2||b<2||c<1){cerr<<"bad group sizes\n";exit(8);}
 vector<vector<int>> P,Q,R;
 perms_range(1,a,P);
 perms_range(a+1,a+b,Q);
 perms_range(a+b,n,R);
 vector<array<int,8>> maps;
 for(auto&p:P)for(auto&q:Q)for(auto&r:R){
  array<int,8> m;
  iota(m.begin(),m.end(),0);
  for(int i=1;i<a;i++)m[i]=p[i-1];
  for(int i=a+1;i<a+b;i++)m[i]=q[i-a-1];
  for(int i=a+b;i<n;i++)m[i]=r[i-a-b];
  maps.push_back(m);
 }
 Counts C;
 for(int code=0;code<262144;code++){
  int pr[6],degree[8],edges[7][2];
  fill(degree,degree+8,1);
  int z=code;
  for(int i=0;i<6;i++){pr[i]=z%8;z/=8;degree[pr[i]]++;}
  for(int i=0;i<6;i++){
   int leaf=0;while(degree[leaf]!=1)leaf++;
   edges[i][0]=leaf;edges[i][1]=pr[i];
   degree[leaf]--;degree[pr[i]]--;
  }
  int x=-1,y=-1;
  for(int i=0;i<n;i++)if(degree[i]==1){if(x<0)x=i;else y=i;}
  edges[6][0]=x;edges[6][1]=y;
  uint32_t mask=0;
  bool contains_final=false;
  for(auto&e:edges){
   int u=e[0],v=e[1];
   if((u==0&&v==a)||(u==a&&v==0))contains_final=true;
   mask|=uint32_t(1)<<edge_index(u,v);
  }
  if(contains_final)continue;
  C.trees++;
  bool canonical=true;
  for(auto&m:maps){
   uint32_t translated=0;
   for(auto&e:edges)
    translated|=uint32_t(1)<<edge_index(m[e[0]],m[e[1]]);
   if(translated<mask){canonical=false;break;}
  }
  if(!canonical)continue;
  C.orbits++;
  int order[7];iota(order,order+7,0);
  do{
   C.orders++;
   int know[8]={1,2,4,8,16,32,64,128};
   for(int i=0;i<7;i++){
    int t=order[i],u=edges[t][0],v=edges[t][1];
    know[u]=know[v]=know[u]|know[v];
   }
   // Both members of any 2-person group must ultimately know every secret.
   // Only endpoints 0 and a change in the LAST call, hence the other
   // member must already be fully informed in the seven-call tree.
   if(a==2&&know[1]!=255)continue;
   if(b==2&&know[a+1]!=255)continue;
   know[0]=know[a]=know[0]|know[a];
   bool ok=true;
   for(int secret=0;secret<n;secret++){
    int carriers[3]={};
    for(int i=0;i<n;i++)if(know[i]&(1<<secret))
     carriers[i<a?0:i<a+b?1:2]++;
    if(carriers[0]<2||carriers[1]<2||carriers[2]<1)
    {ok=false;break;}
   }
   if(ok){
    C.passing++;
    if(a==2&&b==5){
     // Additional Stage 18 independent certificate: EXACTLY one of the
     // five group-B receivers is full, and for each of the four others
     // a reversed target has support {full_B, that receiver} inside B.
     int full_count=0,full_B=-1;
     for(int i=0;i<n;i++)if(know[i]==255){
      full_count++;
      if(i>=a&&i<a+b)full_B=i;
     }
     if(full_count!=4||full_B<0){
      cerr<<"FAIL center-singleton cycle four-root assertion\n";exit(9);
     }
     for(int z=a;z<a+b;z++)if(z!=full_B){
      bool pair_secret=false;
      for(int secret=0;secret<n;secret++){
       int holders=0;
       for(int i=a;i<a+b;i++)
        if(know[i]&(1<<secret))holders|=(1<<i);
       if(holders==((1<<full_B)|(1<<z)))pair_secret=true;
      }
      if(!pair_secret){
       cerr<<"FAIL missing target support pair at receiver "<<z<<"\n";
       exit(10);
      }
     }
    }
   }
  }while(next_permutation(order,order+7));
 }
 return C;
}
int main(){
 struct Fixture{int a,b;long long orbits,passing;};
 const Fixture fixtures[]={{2,3,18240,0},{2,4,18240,0},
                           {3,3,26616,0},{2,5,9653,160},
                           {3,4,18240,0},{2,2,9653,160}};
 long long total=0;
 for(auto f:fixtures){
  Counts q=check(f.a,f.b);
  if(q.trees!=196608||q.orbits!=f.orbits||
     q.orders!=q.orbits*5040||q.passing!=f.passing){
   cerr<<"FAIL n=8 "<<f.a<<","<<f.b<<" trees="<<q.trees
       <<" orbits="<<q.orbits<<" orders="<<q.orders
       <<" compatible="<<q.passing<<"\n";return 2;
  }
  total+=q.orders;
  cout<<"PASS n=8 local group sizes "<<f.a<<","<<f.b<<","<<8-f.a-f.b
      <<" trees="<<q.trees<<" topology_orbits="<<q.orbits
      <<" exact chronological orders="<<q.orders
      <<" compatible="<<q.passing<<"\n";
 }
 if(total!=507235680){cerr<<"FAIL total enumerated\n";return 3;}
 cout<<"PASS local size-8 patterns (2,2,4) OR (2,5,1); 507235680 exact reduced orders\n";
 cout<<"LIMIT: original full two-half gossip conjecture not solved by this local enumeration alone\n";
}
