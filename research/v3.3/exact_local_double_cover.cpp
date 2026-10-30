// Stage 16. Standalone finite enumeration: ORIGINAL chronological unicyclic
// local components with last cycle edge crossing groups 0 and 1.
// Each original secret must have >=2 terminal carriers in BOTH groups 0,1,
// and >=1 in central group 2. This is a necessary local consequence of a
// hypothetically successful both-cyclic ORIGINAL midpoint, NOT a full solver.
//
// Completeness: relabel any given group partition to canonical contiguous
// intervals. Relabel last edge endpoints to vertices 0 and a. Enumerate every
// labelled spanning tree via all n^(n-2) Prufer strings, every (n-1)! tree
// contact chronology, and append the specified new edge. No duplicate calls.
// For n=5,6,7 this checks all possible sizes (a,b,c), a,b>=2,c>=1.
// Passing this does not exclude an arbitrary global schedule for n>=8.
#include <algorithm>
#include <iostream>
#include <numeric>
using namespace std;
struct Result {long long trees=0,histories=0,witnesses=0;};
Result search(int n,int a,int b) {
 const int c=n-a-b;
 if(a<2||b<2||c<1) return {};
 const int endpoint=a; // final edge (0,a), lying in the first TWO groups
 long long possibilities=1;
 for(int t=0;t<n-2;t++)possibilities*=n;
 Result r;
 for(long long id=0;id<possibilities;id++){
  int degree[8],prufer[6],edges[7][2];
  fill(degree,degree+n,1);
  long long num=id;
  for(int i=0;i<n-2;i++){prufer[i]=num%n;num/=n;degree[prufer[i]]++;}
  for(int i=0;i<n-2;i++){
   int leaf=0;while(degree[leaf]!=1)leaf++;
   edges[i][0]=leaf;edges[i][1]=prufer[i];
   degree[leaf]--;degree[prufer[i]]--;
  }
  int x=-1,y=-1;
  for(int i=0;i<n;i++)if(degree[i]==1){if(x<0)x=i;else y=i;}
  edges[n-2][0]=x;edges[n-2][1]=y;
  bool repeated=false;
  for(int i=0;i<n-1;i++){
   int u=edges[i][0],v=edges[i][1];
   if((u==0&&v==endpoint)||(v==0&&u==endpoint)){repeated=true;break;}
  }
  if(repeated)continue;
  r.trees++;
  int permutation[7];
  iota(permutation,permutation+n-1,0);
  do {
   r.histories++;
   int knowledge[8];
   for(int i=0;i<n;i++)knowledge[i]=1<<i;
   for(int j=0;j<n-1;j++){
    const int edge=permutation[j];
    const int u=edges[edge][0],v=edges[edge][1];
    knowledge[u]=knowledge[v]=knowledge[u]|knowledge[v];
   }
   knowledge[0]=knowledge[endpoint]=knowledge[0]|knowledge[endpoint];
   bool good=true;
   for(int secret=0;secret<n;secret++){
    int count[3]={};
    for(int i=0;i<n;i++)if(knowledge[i]&(1<<secret)){
     count[i<a?0:i<a+b?1:2]++;
    }
    if(count[0]<2||count[1]<2||count[2]<1){good=false;break;}
   }
   if(good){
    ++r.witnesses;
    cerr<<"WITNESS n="<<n<<" groups "<<a<<","<<b<<","<<c<<"\n";
   }
  }while(next_permutation(permutation,permutation+n-1));
 }
 return r;
}
void check_sharp_eight(){
 // Four chronological four-person tree pieces within two size-four sides.
 // The penultimate (0,2) joins the two sides; final (1,3) closes a cycle.
 const int n=8;
 const int calls[8][2]={
  {0,4},{1,5},{0,1},
  {2,6},{3,7},{2,3},
  {0,2},{1,3}
 };
 int knowledge[8];for(int i=0;i<n;i++)knowledge[i]=1<<i;
 bool seen[8][8]={};
 for(auto &e:calls){
  const int u=e[0],v=e[1];
  if(u==v||seen[u][v]){cerr<<"FAIL duplicate edge in n8\n";exit(3);}
  seen[u][v]=seen[v][u]=true;
  knowledge[u]=knowledge[v]=knowledge[u]|knowledge[v];
 }
 const int groups[8]={0,0,1,1,2,2,2,2};
 for(int secret=0;secret<n;secret++){
  int count[3]={};
  for(int i=0;i<n;i++)if(knowledge[i]&(1<<secret))count[groups[i]]++;
  if(count[0]<2||count[1]<2||count[2]<1){
   cerr<<"FAIL local n8 boundary secret "<<secret<<"\n";exit(4);
  }
 }
 for(int i=0;i<4;i++)if(knowledge[i]!=255){cerr<<"FAIL n8 full root\n";exit(5);}
 cout<<"PASS sharp local n8 distinct-call unicyclic chronology (2,2,4), final across groups\n";
}
int main(){
 long long all=0;
 for(int n=5;n<=7;n++){
  const long long exp_tree=(n==5?75:n==6?864:12005);
  const long long exp_hist=(n==5?1800:n==6?103680:8643600);
  for(int a=2;a<=n-3;a++)for(int b=2;b<=n-a-1;b++){
   Result r=search(n,a,b);
   if(r.trees!=exp_tree||r.histories!=exp_hist||r.witnesses!=0){
    cerr<<"FAIL local n="<<n<<" sizes "<<a<<","<<b<<","<<n-a-b
        <<" trees="<<r.trees<<" histories="<<r.histories
        <<" witnesses="<<r.witnesses<<"\n";return 2;
   }
   all+=r.histories;
   cout<<"PASS n="<<n<<" groups="<<a<<","<<b<<","<<n-a-b
       <<" spanning trees="<<r.trees
       <<" complete chronological tree histories="<<r.histories
       <<" valid local unicyclic configurations=0\n";
  }
 }
 if(all!=1800+3*103680+6*8643600) return 6;
 check_sharp_eight();
 cout<<"PASS exact local exclusion for <=7 vertices; all-n midpoint conjecture remains OPEN\n";
 return 0;
}
