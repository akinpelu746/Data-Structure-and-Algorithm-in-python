Xtreme Teams
Time limit: 2000 ms
Memory limit: 256 MB

In IEEEXtreme, each team consists of three students. The contest may challenge the students with problems on MM topics. There are NN students at a school who are known to specialize in some of those MM topics (possibly none, possibly all). In order to achieve best performance, for each of the MM topics, a team should have at least one student who specializes in that topic. In how many ways can a single team be formed by choosing 33 students from the NN students, so that at least one student specializes in each of the MM topics?


Standard input
The input begins with a single integer TT on the first line, the number of test cases.

The first line of each test case has two integers NN and MM. The next NN lines each have a string of length MM that represents the topic specialties of one student. For each student, the iith letter is y if he/she specializes in topic ii, or n otherwise.


Standard output
For each test case, output the number of different ways to choose 33 students to form a team on a single line.


Constraints and notes
1 \leq T \leq 151≤T≤15
3 \leq N \leq 5\,0003≤N≤5000
1 \leq M \leq 181≤M≤18
For 33\%33% of the test files, N \leq 100N≤100, M \leq 12M≤12.
For 66\%66% of the test files, M \leq 12M≤12.






Input	
4
4 3
ynn
nyn
yyn
yny
4 5
yyyyy
yyynn
nyyyn
nnnny
5 4
ynnn
nynn
nnyn
nnny
nnnn
6 6
yynnyy
yynnyy
nnyyyy
nnyyyy
yyyynn
yyyynn
Output	Explanation
3
4
0
20