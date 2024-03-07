Once upon a time, in the kingdom of *, there was a mysterious square grid with n rows and n columns. Each cell in this grid was enchanted with either a magical symbol representing "truth" (1
) or "illusion" (0
).

The residents of * believed that by performing a special operation, they could unveil the true nature of the grid. This operation involved selecting a cell in the grid and flipping its magical symbol, turning "illusion" into "truth" and vice versa.

However, the residents sought a deeper understanding of the grid's true nature. They were intrigued by the idea of finding the minimum number of operations needed to transform the grid into a state that would remain unchanged when rotated at angles of 0∘
, 90∘
, 180∘
 and 270∘
.

The picture below shows an example of all rotations of a grid.


To aid in their quest, the residents studied the mystical properties of the grid and experimented with various operations. They were determined to unlock the secrets hidden within the grid and uncover its true form.

Through perseverance and ingenuity, the residents of * eventually discovered the minimum number of operations required to achieve their goal. The grid revealed its true nature, and the residents celebrated their newfound knowledge, forever changed by their journey of discovery.

Can you achieve what the residents of * and find the minimum number of operations required to transform the grid into a state that would remain unchanged when rotated at angles of 0∘
, 90∘
, 180∘
 and 270∘
?

Input
The first line contains a single integer t
 (1≤t≤100
) — the number of test cases.

The first line of each test case contains a single integer n
 (1≤n≤100
) — the size of the grid.

Then n
 lines follow, each with n
 characters ai,j
 (0≤ai,j≤1
) — the number written in each cell.

Output
For each test case output a single integer  — the minimum number of operations needed to make the square look the same rotated 0∘
, 90∘
, 180∘
 and 270∘
.

Example
inputCopy
5
3
010
110
010
1
0
5
11100
11011
01011
10011
11000
5
01000
10101
01010
00010
01001
5
11001
00000
11111
10110
01111
outputCopy
1
0
9
7
6
Note
In the first test case, we can perform one operations to make the grid 010111010
. Now, all rotations of the square are the same.