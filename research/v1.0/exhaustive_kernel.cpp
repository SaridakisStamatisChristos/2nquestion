// Exhaust all shortest distinct-edge all-to-all gossip protocols, up to relabelling
// their first contact to (0,1). Checks existence of 4-call butterfly.
#include <bits/stdc++.h>
using namespace std;
int n,m,k, calls[14],calls_count;vector<pair<int,int>> es;vector<array<int,4>> cyc;
long long total=0,valid=0,nobutter=0;
int idx(int a,int b){if(a>b)swap(a,b);return a*(2*n-a-1)/2+b-a-1;}
int score(){
 int pos[21];fill(pos,pos+m,999);for(int i=0;i<k;i++)pos[calls[i]]=i;
 for(auto const&C:cyc){int a=pos[C[0]],b=pos[C[1]],c=pos[C[2]],d=pos[C[3]];
  if(a<k&&b<k&&c<k&&d<k&&(max(a,c)<min(b,d)||max(b,d)<min(a,c)))return 1;
 }
 return 0;
}
void dfs(int depth,uint32_t mask,const array<uint32_t,7>&K){
 if(depth==k){total++;
   if(all_of(K.begin(),K.begin()+n,[&](uint32_t x){return x==((1u<<n)-1u);})){valid++;
    if(!score()){nobutter++;if(nobutter<=2){cerr<<"FAILURE ";for(int i=0;i<k;i++)cerr<<calls[i]+1<<' ';cerr<<'\n';}}
   }
   return;
 }
 for(int e=0;e<m;e++){
  if(mask&(1u<<e))continue;
  auto next=K;auto[a,b]=es[e];uint32_t u=next[a]|next[b];next[a]=u;next[b]=u;
  calls[depth]=e;dfs(depth+1,mask|(1u<<e),next);
 }
}
int main(int argc,char**argv){n=argc>1?atoi(argv[1]):6;assert(n>=4&&n<=6);m=n*(n-1)/2;k=2*n-4;
 for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)es.push_back({a,b});
 for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)for(int d=c+1;d<n;d++){
 cyc.push_back({idx(a,b),idx(b,c),idx(c,d),idx(a,d)});
 cyc.push_back({idx(a,b),idx(b,d),idx(c,d),idx(a,c)});
 cyc.push_back({idx(a,c),idx(b,c),idx(b,d),idx(a,d)});
 }
 array<uint32_t,7> K{};for(int i=0;i<n;i++)K[i]=1u<<i;
 int initial=idx(0,1);calls[0]=initial;
 auto temp=K;temp[0]|=temp[1];temp[1]=temp[0];
 auto start=chrono::steady_clock::now();dfs(1,1u<<initial,temp);
 auto duration=chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count();
 cout<<"n "<<n<<" schedules_with_first_contact_01 "<<total<<" optimal_gossip_sequences "<<valid<<" without_butterfly "<<nobutter<<" elapsed_ms "<<duration<<"\n";
}
