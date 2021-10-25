Bus Company
Time limit: 12000 ms
Memory limit: 256 MB

Lima is known by its tree-shaped road networks. Thus, there are NN cities numbered from 11 to NN and there are exactly N - 1N−1 bidirectional roads that connect them and there exists a path between any pair of cities. There are two bus companies, A and B, that are being frequently compared by the Ministry of Transportation. Each city has exactly one bus stop, which is owned by one of the two companies.

The Ministry of Transportation may try to compare the two companies, and identify a winner company following these steps:

Choose two cities uu and vv and consider the simple path (u, v)(u,v) between them. A simple path is a path that doesn't visit the same city twice.
For each company, compute the average length of all the simple paths that start in a city aa and end in a city bb such that both bus stops at aa and bb are owned by this company and the path (a, b)(a,b) contains path (u, v)(u,v). That is, all cities in the path from uu to vv are contained in the path from aa to bb. If there are no such paths, the value is considered \infty∞.
Declare that the company that has a smaller average length is the winner company.
Additionally, a company can buy the bus stop at some city uu, in which case the ownership of the bus stop at city uu changes.

You will receive QQ events that happen in order, which can be one of the two types:

Transaction Event: The bus stop in city uu was bought by the other company (if it was owned by company A, now belongs to company B, and vice versa).
Comparison Event: Two cities uu and vv are chosen to compare the two companies. Check which company wins or if there is a tie.

Standard input

The first line contains a single integer NN, indicating the total number of cities.

The second line contains NN integers 00 or 11, indicating whether city ii initially belongs to company A or B, respectively.

The next N-1N−1 lines each contain 22 integers aa and bb, indicating there is a bidirectional road between city aa and city bb.

Line N+2N+2 contains an integer QQ, the number of events. The following QQ lines contain the events. Each event is either 1 ~u1 u (transaction event), or 2 ~u ~v2 u v (comparison event).


Standard Output
For each comparison event print A if company A wins, B if company B wins, or TIE if there is a tie between both companies.


Constraints and notes
N \geq 2N≥2
N, Q \leq 2 \cdot 10^5N,Q≤2⋅10 
5
 
In all events, 1 \leq u, v \leq N, u \neq v1≤u,v≤N,u

=v.
The road network forms a tree.
There is at least one comparison event.

For 5\%5% of the test files, N, Q \leq 10^3N,Q≤10 
3
 .
For 10\%10% of the test files, N, Q \leq 10^4N,Q≤10 
4
 .
For 30\%30% of the test files, N, Q \leq 10^5N,Q≤10 
5
 .




Input	                        Output	
8                               B
1 0 0 0 0 1 0 0                 A
1 3                             TIE
                                  A
5 8
6 2
1 5
5 4
2 7
5 2
6
2 2 6
2 8 7
1 8
1 1
2 8 7
2 2 5