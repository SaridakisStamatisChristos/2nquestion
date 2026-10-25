#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <utility>
#include <vector>
using namespace std;
using E=pair<int,int>;
static const int N=9;
using Seq=vector<E>;
static bool feasible(const Seq& a,uint64_t mask){unsigned int know[9]={1,2,4,8,16,32,64,128,256};for(int i=0;i<(int)a.size();i++)if(mask>>i&1){auto [u,v]=a[i];know[u]|=know[v];know[v]=know[u];}for(int i=0;i<9;i++)if(know[i]!=511)return false;return true;}
static bool pivot(const Seq& a){unsigned int pre[9],future[9],suf[36];for(int i=0;i<9;i++)pre[i]=future[i]=1<<i;for(int i=35;i>=0;i--){auto [u,v]=a[i];suf[i]=future[u]|future[v];future[u]=future[v]=suf[i];}for(int i=0;i<36;i++){auto [u,v]=a[i];if((pre[u]|pre[v])==511&&suf[i]==511)return true;pre[u]|=pre[v];pre[v]=pre[u];}return false;}
static int greed(const Seq &a,mt19937 &rng){array<int,36> perm; iota(perm.begin(),perm.end(),0);shuffle(perm.begin(),perm.end(),rng);uint64_t mask=(1ULL<<36)-1;int count=36;for(int j:perm){if(count==14)break;uint64_t cand=mask&~(1ULL<<j);if(feasible(a,cand)){mask=cand;count--;}}return count;}
int main(int argc,char **argv){const int samples=argc>1?atoi(argv[1]):20000;mt19937 rng(20261024);int s;cin>>s;vector<Seq> old(s,Seq(28));for(auto &a:old)for(auto &e:a)cin>>e.first>>e.second;int nonpivot=0,hard12=0,hard512=0,maxscore=0;Seq hardest;
for(int t=0;t<samples;t++){
 Seq a=old[rng()%old.size()];for(int v=0;v<8;v++)a.emplace_back(v,8);
 // Interleave the n8 edges with the eight new edges, preserving n8 chronology
 for(int j=35;j>0;j--){int k=rng()%(j+1); // random shuffle only new edge insert positions via stable-tagged permutation
 (void)k;
 }
 Seq b; b.reserve(36); int source=0; array<int,36> picks; iota(picks.begin(),picks.end(),0);shuffle(picks.begin(),picks.end(),rng);
 bool mark[36]={};for(int j=0;j<8;j++)mark[picks[j]]=true;int oldidx=0,newidx=28;
 for(int j=0;j<36;j++)b.push_back(mark[j]?a[newidx++]:a[oldidx++]);
 if(pivot(b))continue;nonpivot++;
 int score=0,best=36;for(int j=0;j<12;j++){int k=greed(b,rng);best=min(best,k);score+=k;if(best==14)break;}
 if(best>14){hard12++;int succ=0;for(int j=0;j<512;j++)if(greed(b,rng)==14){succ=1;break;}
 if(!succ){hard512++;if(score>maxscore){maxscore=score;hardest=b;}}
 }
 }
 cerr<<"samples="<<samples<<" nonpivot="<<nonpivot<<" hard12="<<hard12<<" hard512="<<hard512<<"\n";
 if(!hardest.empty()){cout<<"Candidate n9 hard under 524 greedy trials; NOT A CERTIFIED COUNTEREXAMPLE\n";for(auto [u,v]:hardest)cout<<u<<" "<<v<<"\n";}
}
