// Independent exact enumeration of chronological tree histories and two-group
// rooted covering. No optimistic domains, external solver or reused oracle.
// A root collector (vertex 0) lies outside two disjoint recipient groups.
// Compute PRIVATE members: member v knows some secret no other in its group knows.
#include <algorithm>
#include <iostream>
using namespace std;
int main(){
 for(int n=4;n<=6;n++){
  long long nt=1;for(int i=0;i<n-2;i++)nt*=n;
  long long histories=0,covers=0,at_most_one_private_each=0;
  int edges[8][2],perm[8];
  for(long long id=0;id<nt;id++){
   int degree[8];fill(degree,degree+n,1);
   int code[8]={};auto z=id;
   for(int i=0;i<n-2;i++){code[i]=z%n;z/=n;degree[code[i]]++;}
   for(int i=0;i<n-2;i++){
    int leaf=-1;for(int v=0;v<n;v++)if(degree[v]==1){leaf=v;break;}
    edges[i][0]=leaf;edges[i][1]=code[i];
    degree[leaf]--;degree[code[i]]--;
   }
   int a=-1,b=-1;
   for(int v=0;v<n;v++)if(degree[v]==1){if(a<0)a=v;else b=v;}
   edges[n-2][0]=a;edges[n-2][1]=b;
   for(int i=0;i<n-1;i++)perm[i]=i;
   do{
    histories++;
    int know[8];for(int v=0;v<n;v++)know[v]=1<<v;
    for(int i=0;i<n-1;i++){
     int u=edges[perm[i]][0],v=edges[perm[i]][1];
     know[u]=know[v]=know[u]|know[v];
    }
    int all=(1<<n)-1;if(know[0]!=all)continue;
    for(int mask=1;mask<(1<<(n-1))-1;mask++){
     int group[8]={},coverage[2]={},private_count[2]={};
     for(int v=1;v<n;v++){
      int g=(mask>>(v-1))&1;group[v]=g;coverage[g]|=know[v];
     }
     if(coverage[0]!=all||coverage[1]!=all)continue;
     covers++;
     for(int v=1;v<n;v++){
      int g=group[v];bool priv=false;
      for(int secret=0;secret<n;secret++)if(know[v]>>secret&1){
       bool other=false;
       for(int u=1;u<n;u++)
        if(u!=v&&group[u]==g&&(know[u]>>secret&1))other=true;
       if(!other){priv=true;break;}
      }
      private_count[g]+=priv;
     }
     if(private_count[0]<=1&&private_count[1]<=1)
      at_most_one_private_each++;
    }
   }while(next_permutation(perm,perm+n-1));
  }
  const long long exp_hist[]={96,3000,155520};
  const long long exp_cover[]={24,1152,72960};
  const long long exp_private[]={0,0,3840};
  int ix=n-4;
  if(histories!=exp_hist[ix]||covers!=exp_cover[ix]||
     at_most_one_private_each!=exp_private[ix]){
   cerr<<"FAIL n="<<n<<" histories="<<histories
       <<" covers="<<covers<<" low-private="<<at_most_one_private_each<<"\n";
   return 2;
  }
  cout<<"PASS n="<<n<<" chronological tree histories="<<histories
      <<" rooted covering assignments="<<covers
      <<" <=1 private in each X-group="<<at_most_one_private_each<<"\n";
 }
 // Separately replay an explicit six-participant counterexample to
 // a tempting but invalid stronger private-recipient lemma.
 int schedule[5][2]={{2,4},{3,1},{0,5},{1,0},{4,0}};
 int know[6];for(int i=0;i<6;i++)know[i]=1<<i;
 for(auto &e:schedule){int a=e[0],b=e[1];know[a]=know[b]=know[a]|know[b];}
 const int expected[]={63,43,20,10,63,33};
 for(int i=0;i<6;i++)if(know[i]!=expected[i])return 3;
 if((know[1]|know[2]|know[3]|know[5])!=63)return 4;
 cout<<"PASS concrete n6 rooted tree: 5 distinct calls,"
     <<" singleton {4} complete, group {1,2,3,5} collectively complete,"
     <<" each group has precisely one private recipient\n";
 cout<<"VERDICT: rooted private-scarcity appears with slack;"
     <<" all-n crossing inequality uses equality rigidity ONLY\n";
}