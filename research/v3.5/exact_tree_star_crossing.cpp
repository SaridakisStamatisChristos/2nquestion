// Stage 18. Independent exact 7-person original chronological tree crossing
// obstruction for the five-member shared cell (y,z1,z2,z3,z4).
// The reverse-suffix target supports are exactly {y,zi}, four pairs.
// We must NOT count a relaxed local scheme as a global gossip witness.
#include <algorithm>
#include <iostream>
#include <numeric>
using namespace std;
int main(){
 const int n=7;
 long long trees=0,orders=0,rooted_covers=0,star_compatible=0;
 for(int code=0;code<16807;code++){
  int degree[7],seq[5],edges[6][2];
  fill(degree,degree+7,1);
  int value=code;
  for(int i=0;i<5;i++){
   seq[i]=value%7;
   value/=7;
   degree[seq[i]]++;
  }
  for(int i=0;i<5;i++){
   int leaf=0;
   while(degree[leaf]!=1)leaf++;
   edges[i][0]=leaf;edges[i][1]=seq[i];
   degree[leaf]--;degree[seq[i]]--;
  }
  int x=-1,y=-1;
  for(int i=0;i<7;i++)if(degree[i]==1){
   if(x<0)x=i;else y=i;
  }
  edges[5][0]=x;edges[5][1]=y;
  int last=-1;
  for(int i=0;i<6;i++)if(
     (edges[i][0]==0&&edges[i][1]==1)||
     (edges[i][1]==0&&edges[i][0]==1))last=i;
  if(last<0)continue;
  trees++;
  int order[5],j=0;
  for(int i=0;i<6;i++)if(i!=last)order[j++]=i;
  do{
   orders++;
   int know[7];
   for(int i=0;i<7;i++)know[i]=1<<i;
   for(int i=0;i<5;i++){
    int e=order[i],a=edges[e][0],b=edges[e][1];
    know[a]=know[b]=know[a]|know[b];
   }
   const int a=edges[last][0],b=edges[last][1];
   know[a]=know[b]=know[a]|know[b];
   const int full=(1<<n)-1;
   // Exact singleton-corner tree and collective five-receiver cover.
   if(know[0]!=full||know[1]!=full||
      (know[2]|know[3]|know[4]|know[5]|know[6])!=full)continue;
   rooted_covers++;
   // Center root y=2; the four corresponding reversed-Q3 target support
   // pairs are {2,3}, {2,4}, {2,5}, {2,6}. Check every original secret.
   bool compatible=true;
   for(int secret=0;secret<n;secret++){
    for(int z=3;z<=6;z++){
     if(!((know[2]&(1<<secret))||(know[z]&(1<<secret)))){
      compatible=false;break;
     }
    }
    if(!compatible)break;
   }
   if(compatible)star_compatible++;
  }while(next_permutation(order,order+5));
 }
 cout<<"n=7 rooted tree-with-last-corner-call graph count "<<trees<<"\n";
 cout<<"all original chronological tree histories "<<orders<<"\n";
 cout<<"complete singleton-corner + five-cell covers "<<rooted_covers<<"\n";
 cout<<"star-compatible full information crossings "<<star_compatible<<"\n";
 if(trees!=4802||orders!=576240||
    rooted_covers!=57600||star_compatible!=0){
  cerr<<"FAIL Stage 18 exact tree-star obstruction\n";
  return 2;
 }
 cout<<"PASS no rooted original-chronology tree crosses four target pairs\n";
 cout<<"LIMIT: the all-n result uses the separately written side-splitting proof\n";
 return 0;
}
