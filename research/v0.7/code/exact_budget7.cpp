#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int N,M; vector<pair<int,int>> ed; int idx[10][10];
U initclique(const vector<int>& S) {U mask=0;for(int a:S) for(int b:S)if(a<b)mask |= U(1)<<idx[a][b];return mask;}
struct S{U mask;int used;};
void rec(U mask,int used,unordered_set<U>& out,int k){
 if(__builtin_popcount((unsigned)used)==N){out.insert(mask);return;}
 vector<int> verts;for(int v=0;v<N;v++)if(used>>v&1)verts.push_back(v);
 for(int v=0;v<N;v++)if(!(used>>v&1)){
  for(int aa=0;aa<(int)verts.size();aa++)for(int bb=aa+1;bb<(int)verts.size();bb++)for(int cc=bb+1;cc<(int)verts.size();cc++){
   int a=verts[aa],b=verts[bb],c=verts[cc];
   if((mask>>idx[a][b]&1)&&(mask>>idx[a][c]&1)&&(mask>>idx[b][c]&1)){
      U x=mask|(U(1)<<idx[min(v,a)][max(v,a)])|(U(1)<<idx[min(v,b)][max(v,b)])|(U(1)<<idx[min(v,c)][max(v,c)]);
      rec(x,used|(1<<v),out,k);
   }
  }
 }
}
bool connected(U mask,const vector<int> &order){
 U info[10];for(int v=0;v<N;v++)info[v]=U(1)<<v;
 for(int i:order) if(mask>>i&1){auto [a,b]=ed[i];U k=info[a]|info[b];info[a]=info[b]=k;}
 U full=(U(1)<<N)-1;for(int v=0;v<N;v++)if(info[v]!=full)return false;
 return true;
}
int main(int argc,char**argv){N=argc>1?atoi(argv[1]):7;int trials=argc>2?atoi(argv[2]):100;int seed=argc>3?atoi(argv[3]):271828;for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){idx[a][b]=idx[b][a]=ed.size();ed.push_back({a,b});}M=ed.size();
 unordered_set<U> out;int k=3;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){
  vector<int>S={a,b,c,d};rec(initclique(S),(1<<a)|(1<<b)|(1<<c)|(1<<d),out,k);
 }
 vector<U> trees(out.begin(),out.end());sort(trees.begin(),trees.end());cerr<<"n="<<N<<" candidates="<<trees.size()<<"\n";

 vector<pair<int,int>> timeline={{3,6},{1,6},{0,6},{5,6},{0,3},{2,6},{4,6},{0,1},{3,5},{0,5},{1,2},{1,5},{0,2},{0,4},{1,3},{2,3},{1,4},{2,5},{4,5},{2,4},{3,4}};
 vector<int> order;for(auto [a,b]:timeline)order.push_back(idx[a][b]);
 cerr<<"schedule=";for(auto [a,b]:timeline)cerr<<"("<<a<<","<<b<<") ";cerr<<"\n";
 auto is_tw3=[&](U m){for(U t:trees)if((m&t)==m)return true;return false;};
 for(int k=9;k<=13;k++){
 unsigned long long checks=0,tc=0,tw3=0;U witness=0;auto beg=chrono::steady_clock::now();
 vector<int> comb(k);iota(comb.begin(),comb.end(),0);
 while(true){U mask=0;for(int i:comb)mask|=U(1)<<i; checks++;
 if(connected(mask,order)){tc++;if(is_tw3(mask)){tw3++;if(!witness)witness=mask;}}
 int j=k-1;while(j>=0 && comb[j]==M-k+j)--j;
 if(j<0)break;
 comb[j]++;for(int l=j+1;l<k;l++)comb[l]=comb[l-1]+1;
 }
 auto end=chrono::steady_clock::now();
 cerr<<"k="<<k<<" checked="<<checks<<" tc="<<tc<<" tw3="<<tw3<<" witness="<<witness<<" elapsed="<<chrono::duration_cast<chrono::milliseconds>(end-beg).count()<<"ms\n";
 if(witness){cerr<<"witness_edges=";for(int i:order)if(witness>>i&1){auto [a,b]=ed[i];cerr<<"("<<a<<","<<b<<") ";}cerr<<"\n";break;}
 }
}
