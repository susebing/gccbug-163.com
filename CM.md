# [程序员面试金典](https://www.nowcoder.com/ta/cracking-the-coding-interview)

## CM1确定字符互异

```
题目描述
请实现一个算法，确定一个字符串的所有字符是否全都不同。这里我们要求不允许使用额外的存储结构。

给定一个string iniString，请返回一个bool值,True代表所有字符全都不同，False代表存在相同的字符。保证字符串中的字符为ASCII字符。字符串的长度小于等于3000。

测试样例：
"aeiou"
返回：True
"BarackObama"
返回：False
```

## CM2 原串翻转

```
题目描述
请实现一个算法，在不使用额外数据结构和储存空间的情况下，翻转一个给定的字符串(可以使用单个过程变量)。

给定一个string iniString，请返回一个string，为翻转后的字符串。保证字符串的长度小于等于5000。

测试样例：
"This is nowcoder"
返回："redocwon si sihT"
```

## CM3 确定两串乱序同构

```
题目描述
给定两个字符串，请编写程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。这里规定大小写为不同字符，且考虑字符串中的空格。

给定一个string stringA和一个string stringB，请返回一个bool，代表两串是否重新排列后可相同。保证两串的长度都小于等于5000。

测试样例：
"This is nowcoder","is This nowcoder"
返回：true
"Here you are","Are you here"
返回：false
```

##  CM4	空格替换

```
题目描述
请编写一个方法，将字符串中的空格全部替换为“%20”。假定该字符串有足够的空间存放新增的字符，并且知道字符串的真实长度(小于等于1000)，同时保证字符串由大小写的英文字母组成。

给定一个string iniString 为原始的串，以及串的长度 int len, 返回替换后的string。

测试样例：
"Mr John Smith”,13
返回："Mr%20John%20Smith"
”Hello  World”,12
返回：”Hello%20%20World”
```

##  CM5	基本字符串压缩

```
题目描述
利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串“aabcccccaaa”经压缩会变成“a2b1c5a3”。若压缩后的字符串没有变短，则返回原先的字符串。

给定一个string iniString为待压缩的串(长度小于等于10000)，保证串内字符均由大小写英文字母组成，返回一个string，为所求的压缩后或未变化的串。

测试样例
"aabcccccaaa"
返回："a2b1c5a3"
"welcometonowcoderrrrr"
返回："welcometonowcoderrrrr"
```

##  CM6	像素翻转

```
题目描述
有一副由NxN矩阵表示的图像，这里每个像素用一个int表示，请编写一个算法，在不占用额外内存空间的情况下(即不使用缓存矩阵)，将图像顺时针旋转90度。

给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵,保证N小于等于500，图像元素小于等于256。

测试样例：
[[1,2,3],[4,5,6],[7,8,9]],3
返回：[[7,4,1],[8,5,2],[9,6,3]]
```

## CM7	清除行列

```
题目描述
请编写一个算法，若N阶方阵中某个元素为0，则将其所在的行与列清零。

给定一个N阶方阵int[][](C++中为vector<vector><int>>)mat和矩阵的阶数n，请返回完成操作后的int[][]方阵(C++中为vector<vector><int>>)，保证n小于等于300，矩阵中的元素为int范围内。</int></vector></int></vector>

测试样例：
[[1,2,3],[0,1,2],[0,0,1]]
返回：[[0,0,3],[0,0,0],[0,0,0]]
```

##  CM8	翻转子串

```
题目描述
假定我们都知道非常高效的算法来检查一个单词是否为其他字符串的子串。请将这个算法编写成一个函数，给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成，要求只能调用一次检查子串的函数。

给定两个字符串s1,s2,请返回bool值代表s2是否由s1旋转而成。字符串中字符为英文字母和空格，区分大小写，字符串长度小于等于1000。

测试样例：
"Hello world","worldhello "
返回：false
"waterbottle","erbottlewat"
返回：true
```

##  JZ14	链表中倒数第k个结点

```
题目描述
输入一个链表，输出该链表中倒数第k个结点。
```

##  CM10	访问单个节点的删除

```
题目描述
实现一个算法，删除单向链表中间的某个结点，假定你只能访问该结点。

给定待删除的节点，请执行删除操作，若该节点为尾节点，返回false，否则返回true
```

## CM11	链表分割

```
题目描述
编写代码，以给定值x为基准将链表分割成两部分，所有小于x的结点排在大于或等于x的结点之前

给定一个链表的头指针 ListNode* pHead，请返回重新排列后的链表的头指针。注意：分割以后保持原来的数据顺序不变。
```

##  CM12	链式A+B

```
题目描述
有两个用链表表示的整数，每个结点包含一个数位。这些数位是反向存放的，也就是个位排在链表的首部。编写函数对这两个整数求和，并用链表形式返回结果。

给定两个链表ListNode* A，ListNode* B，请返回A+B的结果(ListNode*)。

测试样例：
{1,2,3},{3,2,1}
返回：{4,4,4}
```

## CM13	回文链表

```
题目描述
请编写一个函数，检查链表是否为回文。

给定一个链表ListNode* pHead，请返回一个bool，代表链表是否为回文。

测试样例：
{1,2,3,2,1}
返回：true
{1,2,3,2,3}
返回：false
```

##  CM14	集合栈

```
题目描述
请实现一种数据结构SetOfStacks，由多个栈组成，其中每个栈的大小为size，当前一个栈填满时，新建一个栈。该数据结构应支持与普通栈相同的push和pop操作。

给定一个操作序列int[][2] ope(C++为vector&ltvector&ltint>>)，每个操作的第一个数代表操作类型，若为1，则为push操作，后一个数为应push的数字；若为2，则为pop操作，后一个数无意义。请返回一个int[][](C++为vector&ltvector&ltint>>)，为完成所有操作后的SetOfStacks，顺序应为从下到上，默认初始的SetOfStacks为空。保证数据合法。
```

##  JZ5	用两个栈实现队列

```
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
```

## CM16	双栈排序

```
题目描述
请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。

给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到最后一个元素。

测试样例：
[1,2,3,4,5]
返回：[5,4,3,2,1]
```

##  CM17	猫狗收容所

```
题目描述
        有家动物收容所只收留猫和狗，但有特殊的收养规则，收养人有两种收养方式，第一种为直接收养所有动物中最早进入收容所的，第二种为选择收养的动物类型（猫或狗），并收养该种动物中最早进入收容所的。

       给定一个操作序列int[][2] ope(C++中为vector<vector<int>>)代表所有事件。若第一个元素为1，则代表有动物进入收容所，第二个元素为动物的编号，正数代表狗，负数代表猫；若第一个元素为2，则代表有人收养动物，第二个元素若为0，则采取第一种收养方式，若为1，则指定收养狗，若为-1则指定收养猫。请按顺序返回收养的序列。若出现不合法的操作，即没有可以符合领养要求的动物，则将这次领养操作忽略。

测试样例：
[[1,1],[1,-1],[2,0],[2,-1]]
返回：[1,-1]
```

## CM18	二叉树平衡检查

```
题目描述
实现一个函数，检查二叉树是否平衡，平衡的定义如下，对于树中的任意一个结点，其两颗子树的高度差不超过1。

给定指向树根结点的指针TreeNode* root，请返回一个bool，代表这棵树是否平衡。
```

##  CM19	有向路径检查

```
题目描述
对于一个有向图，请实现一个算法，找出两点之间是否存在一条路径。

给定图中的两个结点的指针DirectedGraphNode* a, DirectedGraphNode* b(请不要在意数据类型，图是有向图),请返回一个bool，代表两点之间是否存在一条路径(a到b或b到a)。
```

##  CM20	高度最小的BST

```
题目描述
对于一个元素各不相同且按升序排列的有序序列，请编写一个算法，创建一棵高度最小的二叉查找树。

给定一个有序序列int[] vals,请返回创建的二叉查找树的高度。
```

##  CM21	输出单层结点

```
题目描述
对于一棵二叉树，请设计一个算法，创建含有某一深度上所有结点的链表。

给定二叉树的根结点指针TreeNode* root，以及链表上结点的深度，请返回一个链表ListNode，代表该深度上所有结点的值，请按树上从左往右的顺序链接，保证深度不超过树的高度，树上结点的值为非负整数且不超过100000。

题解 讨论 通过的代码笔记 纠错 收藏
```

## CM22	检查是否为BST

```
题目描述
请实现一个函数，检查一棵二叉树是否为二叉查找树。

给定树的根结点指针TreeNode* root，请返回一个bool，代表该树是否为二叉查找树。
```

##  CM23	寻找下一个结点

```
题目描述
请设计一个算法，寻找二叉树中指定结点的下一个结点（即中序遍历的后继）。

给定树的根结点指针TreeNode* root和结点的值int p，请返回值为p的结点的后继结点的值。保证结点的值大于等于零小于等于100000且没有重复值，若不存在后继返回-1。
```

##  CM24	最近公共祖先

```
题目描述
有一棵无穷大的满二叉树，其结点按根结点一层一层地从左往右依次编号，根结点编号为1。现在有两个结点a，b。请设计一个算法，求出a和b点的最近公共祖先的编号。

给定两个int a,b。为给定结点的编号。请返回a和b的最近公共祖先的编号。注意这里结点本身也可认为是其祖先。

测试样例：
2，3
返回：1
```

##  JZ24	二叉树中和为某一值的路径

```
题目描述
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
```

##  CM26	二进制插入

```
题目描述
有两个32位整数n和m，请编写算法将m的二进制数位插入到n的二进制的第j到第i位,其中二进制的位数从低位数到高位且以0开始。

给定两个数int n和int m，同时给定int j和int i，意义如题所述，请返回操作后的数，保证n的第j到第i位均为零，且m的二进制位数小于等于i-j+1。

测试样例：
1024，19，2，6
返回：1100
```

## CM27	二进制小数

```
题目描述
有一个介于0和1之间的实数，类型为double，返回它的二进制表示。如果该数字无法精确地用32位以内的二进制表示，返回“Error”。

给定一个double num，表示0到1的实数，请返回一个string，代表该数的二进制表示或者“Error”。

测试样例：
0.625
返回：0.101
```

##  CM28	最接近的数

```
题目描述
有一个正整数，请找出其二进制表示中1的个数相同、且大小最接近的那两个数。(一个略大，一个略小)

给定正整数int x，请返回一个vector，代表所求的两个数（小的在前）。保证答案存在。

测试样例：
2
返回：[1,4]
```

##  CM29	整数转化

```
题目描述
编写一个函数，确定需要改变几个位，才能将整数A转变成整数B。

给定两个整数int A，int B。请返回需要改变的数位个数。

测试样例：
10,5
返回：4
```

##  CM30	奇偶位交换

```
题目描述
请编写程序交换一个数的二进制的奇数位和偶数位。（使用越少的指令越好）

给定一个int x，请返回交换后的数int。

测试样例：
10
返回：5
```

##  CM31	找出缺失的整数

```
题目描述
数组A包含了0到n的所有整数，但其中缺失了一个。对于这个问题，我们设定限制，使得一次操作无法取得数组number里某个整数的完整内容。唯一的可用操作是询问数组中第i个元素的二进制的第j位(最低位为第0位)，该操作的时间复杂度为常数，请设计算法，在O(n)的时间内找到这个数。

给定一个数组number，即所有剩下的数按从小到大排列的二进制各位的值，如A[0][1]表示剩下的第二个数二进制从低到高的第二位。同时给定一个int n，意义如题。请返回缺失的数。

测试样例：
[[0],[0,1]]
返回：1
```

## CM32	像素设定

```
题目描述
有一个单色屏幕储存在一维数组中，其中数组的每个元素代表连续的8位的像素的值，请实现一个函数，将第x到第y个像素涂上颜色(像素标号从零开始)，并尝试尽量使用最快的办法。

给定表示屏幕的数组screen(数组中的每个元素代表连续的8个像素，且从左至右的像素分别对应元素的二进制的从低到高位)，以及int x,int y，意义如题意所述，保证输入数据合法。请返回涂色后的新的屏幕数组。

测试样例：
[0,0,0,0,0,0],0,47
返回：[255,255,255,255,255,255]
```

##  CM33	碰撞的蚂蚁

```
题目描述
在n个顶点的多边形上有n只蚂蚁，这些蚂蚁同时开始沿着多边形的边爬行，请求出这些蚂蚁相撞的概率。(这里的相撞是指存在任意两只蚂蚁会相撞)

给定一个int n(3<=n<=10000)，代表n边形和n只蚂蚁，请返回一个double，为相撞的概率。

测试样例：
3
返回：0.75
```

## CM34	判断直线相交

```
题目描述
给定直角坐标系上的两条直线，确定这两条直线会不会相交。

线段以斜率和截距的形式给出，即double s1，double s2，double y1，double y2，分别代表直线1和2的斜率(即s1,s2)和截距(即y1,y2)，请返回一个bool，代表给定的两条直线是否相交。这里两直线重合也认为相交。

测试样例：
3.14,3.14,1,2
返回：false
```

##  CM35	加法运算替代

```
题目描述
请编写一个方法，实现整数的乘法、减法和除法运算(这里的除指整除)。只允许使用加号。

给定两个正整数int a,int b,同时给定一个int type代表运算的类型，1为求a ＊ b，0为求a ／ b，-1为求a － b。请返回计算的结果，保证数据合法且结果一定在int范围内。

测试样例：
1,2,1
返回：2
```

## CM36	平分的直线

```
题目描述
在二维平面上，有两个正方形，请找出一条直线，能够将这两个正方形对半分。假定正方形的上下两条边与x轴平行。

给定两个vecotrA和B，分别为两个正方形的四个顶点。请返回一个vector，代表所求的平分直线的斜率和截距，保证斜率存在。

测试样例：
[(0,0),(0,1),(1,1),(1,0)],[(1,0),(1,1),(2,0),(2,1)]
返回：[0.0，0.5]
```

## CM37	穿点最多的直线

```
题目描述
在二维平面上，有一些点，请找出经过点数最多的那条线。

给定一个点集vector<point>p和点集的大小n,没有两个点的横坐标相等的情况,请返回一个vector<double>，代表经过点数最多的那条直线的斜率和截距。</double></point>
```

## CM38	第k个数

```
题目描述
有一些数的素因子只有3、5、7，请设计一个算法，找出其中的第k个数。

给定一个数int k，请返回第k个数。保证k小于等于100。

测试样例：
3
返回：7
```

##  CM39	上楼梯

```
题目描述
有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶、3阶。请实现一个方法，计算小孩有多少种上楼的方式。为了防止溢出，请将结果Mod 1000000007

给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100000。

测试样例1：
1
返回：1
测试样例2：
3
返回：4
测试样例3：
4
返回：7
```

## CM40	机器人走方格I

```
题目描述
有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，计算机器人有多少种走法。

给定两个正整数int x,int y，请返回机器人的走法数目。保证x＋y小于等于12。

测试样例：
2,2
返回：2
```

##  CM41	机器人走方格II

```
题目描述
有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，计算机器人有多少种走法。注意这次的网格中有些障碍点是不能走的。

给定一个int[][] map(C++ 中为vector >),表示网格图，若map[i][j]为1则说明该点不是障碍点，否则则为障碍。另外给定int x,int y，表示网格的大小。请返回机器人从(0,0)走到(x - 1,y - 1)的走法数，为了防止溢出，请将结果Mod 1000000007。保证x和y均小于等于50
```

## CM42	魔术索引I

```
题目描述
在数组A[0..n-1]中，有所谓的魔术索引，满足条件A[i]=i。给定一个升序数组，元素值各不相同，编写一个方法，判断在数组A中是否存在魔术索引。请思考一种复杂度优于o(n)的方法。

给定一个int数组A和int n代表数组大小，请返回一个bool，代表是否存在魔术索引。

测试样例：
[1,2,3,4,5]
返回：false
```

## CM43	魔术索引II

```
题目描述
在数组A[0..n-1]中，有所谓的魔术索引，满足条件A[i]=i。给定一个不下降序列，元素值可能相同，编写一个方法，判断在数组A中是否存在魔术索引。请思考一种复杂度优于o(n)的方法。

给定一个int数组A和int n代表数组大小，请返回一个bool，代表是否存在魔术索引。

测试样例：
[1,1,3,4,5]
返回：true
```

## CM44	集合的子集

```
题目描述
请编写一个方法，返回某集合的所有非空子集。

给定一个int数组A和数组的大小int n，请返回A的所有非空子集。保证A的元素个数小于等于20，且元素互异。各子集内部从大到小排序,子集之间字典逆序排序，见样例。

测试样例：
[123,456,789]
返回：{[789,456,123],[789,456],[789,123],[789],[456 123],[456],[123]}
```

## CM45	字符串排列

```
题目描述
编写一个方法，确定某字符串的所有排列组合。

给定一个string A和一个int n,代表字符串和其长度，请返回所有该字符串字符的排列，保证字符串长度小于等于11且字符串中字符均为大写英文字符，排列中的字符串按字典序从大到小排序。(不合并重复字符串)

测试样例：
"ABC"
返回：["CBA","CAB","BCA","BAC","ACB","ABC"]
```

##  CM46	合法括号序列判断

```
题目描述
对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。

给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。

测试样例：
"(()())",6
返回：true
测试样例：
"()a()()",7
返回：false
测试样例：
"()(()()",7
返回：false
```

## CM47	洪水

```
题目描述
在一个nxm矩阵形状的城市里爆发了洪水，洪水从(0,0)的格子流到这个城市，在这个矩阵中有的格子有一些建筑，洪水只能在没有建筑的格子流动。请返回洪水流到(n - 1,m - 1)的最早时间(洪水只能从一个格子流到其相邻的格子且洪水单位时间能从一个格子流到相邻格子)。

给定一个矩阵map表示城市，其中map[i][j]表示坐标为(i,j)的格子，值为1代表该格子有建筑，0代表没有建筑。同时给定矩阵的大小n和m(n和m均小于等于100)，请返回流到(n - 1,m - 1)的最早时间。保证洪水一定能流到终点。
```

##  CM48	硬币表示

```
题目描述
有数量不限的硬币，币值为25分、10分、5分和1分，请编写代码计算n分有几种表示法。

给定一个int n，请返回n分有几种表示法。保证n小于等于100000，为了防止溢出，请将答案Mod 1000000007。

测试样例：
6
返回：2
```

##  CM49	n皇后问题

```
题目描述
请设计一种算法，解决著名的n皇后问题。这里的n皇后问题指在一个nxn的棋盘上放置n个棋子，使得每行每列和每条对角线上都只有一个棋子，求其摆放的方法数。

给定一个int n，请返回方法数，保证n小于等于15

测试样例：
1
返回：1
```

##  CM50	堆箱子

```
题目描述
有一堆箱子，每个箱子宽为wi，长为di，高为hi，现在需要将箱子都堆起来，而且为了使堆起来的箱子不倒，上面的箱子的宽度和长度必须小于下面的箱子。请实现一个方法，求出能堆出的最高的高度，这里的高度即堆起来的所有箱子的高度之和。

给定三个int数组w,l,h，分别表示每个箱子宽、长和高，同时给定箱子的数目n。请返回能堆成的最高的高度。保证n小于等于500。

测试样例：
[1,1,1],[1,1,1],[1,1,1]
返回：1
```

##  CM51	约瑟夫问题I

```
题目描述
约瑟夫问题是一个非常著名的趣题，即由n个人坐成一圈，按顺时针由1开始给他们编号。然后由第一个人开始报数，数到m的人出局。现在需要求的是最后一个出局的人的编号。

给定两个int n和m，代表游戏的人数。请返回最后一个出局的人的编号。保证n和m小于等于1000。

测试样例：
5 3
返回：4
```

##  CM52	约瑟夫问题II

```
题目描述
约瑟夫问题是一个著名的趣题。这里我们稍稍修改一下规则。有n个人站成一列。并从头到尾给他们编号，第一个人编号为1。然后从头开始报数，第一轮依次报1，2，1，2...然后报到2的人出局。接着第二轮再从上一轮最后一个报数的人开始依次报1，2，3，1，2，3...报到2，3的人出局。以此类推直到剩下以后一个人。现在需要求的即是这个人的编号。

给定一个int n，代表游戏的人数。请返回最后一个人的编号

测试样例：
5
返回：5
```

##  CM53	变位词排序

```
题目描述
请编写一个方法，对一个字符串数组进行排序，将所有变位词合并，保留其字典序最小的一个串。这里的变位词指变换其字母顺序所构成的新的词或短语。例如"triangle"和"integral"就是变位词。

给定一个string的数组str和数组大小int n，请返回排序合并后的数组。保证字符串串长小于等于20，数组大小小于等于300。

测试样例：
["ab","ba","abc","cba"]
返回：["ab","abc"]
```

##  CM54	元素查找

```
题目描述
有一个排过序的数组，包含n个整数，但是这个数组向左进行了一定长度的移位，例如，原数组为[1,2,3,4,5,6]，向左移位5个位置即变成了[6,1,2,3,4,5],现在对于移位后的数组，需要查找某个元素的位置。请设计一个复杂度为log级别的算法完成这个任务。

给定一个int数组A，为移位后的数组，同时给定数组大小n和需要查找的元素的值x，请返回x的位置(位置从零开始)。保证数组中元素互异。

测试样例：
[6,1,2,3,4,5],6,6
返回：0
```

## CM55	找出字符串

```
题目描述
有一个排过序的字符串数组，但是其中有插入了一些空字符串，请设计一个算法，找出给定字符串的位置。算法的查找部分的复杂度应该为log级别。

给定一个string数组str,同时给定数组大小n和需要查找的string x，请返回该串的位置(位置从零开始)。

测试样例：
["a","b","","c","","d"],6,"c"
返回：3
```

## CM56	矩阵元素查找

```
题目描述
有一个NxM的整数矩阵，矩阵的行和列都是从小到大有序的。请设计一个高效的查找算法，查找矩阵中元素x的位置。

给定一个int有序矩阵mat，同时给定矩阵的大小n和m以及需要查找的元素x，请返回一个二元数组，代表该元素的行号和列号(均从零开始)。保证元素互异。

测试样例：
[[1,2,3],[4,5,6]],2,3,6
返回：[1,2]
```

##  CM57	叠罗汉I

```
题目描述
叠罗汉是一个著名的游戏，游戏中一个人要站在另一个人的肩膀上。同时我们应该让下面的人比上面的人更高一点。已知参加游戏的每个人的身高，请编写代码计算通过选择参与游戏的人，我们最多能叠多少个人。注意这里的人都是先后到的，意味着参加游戏的人的先后顺序与原序列中的顺序应该一致。

给定一个int数组men，代表依次来的每个人的身高。同时给定总人数n，请返回最多能叠的人数。保证n小于等于500。

测试样例：
[1,6,2,5,3,4],6
返回：4
```

##  CM58	叠罗汉II

```
题目描述
叠罗汉是一个著名的游戏，游戏中一个人要站在另一个人的肩膀上。为了使叠成的罗汉更稳固，我们应该让上面的人比下面的人更轻一点。现在一个马戏团要表演这个节目，为了视觉效果，我们还要求下面的人的身高比上面的人高。请编写一个算法，计算最多能叠多少人，注意这里所有演员都同时出现。

给定一个二维int的数组actors，每个元素有两个值，分别代表一个演员的身高和体重。同时给定演员总数n，请返回最多能叠的人数。保证总人数小于等于500。

测试样例：
[[1,2],[3,4],[5,6],[7,8]],4
返回：4
```

## CM59	维护x的秩

```
题目描述
现在我们要读入一串数，同时要求在读入每个数的时候算出它的秩，即在当前数组中小于等于它的数的个数(不包括它自身)，请设计一个高效的数据结构和算法来实现这个功能。

给定一个int数组A，同时给定它的大小n，请返回一个int数组，元素为每次加入的数的秩。保证数组大小小于等于5000。

测试样例：
[1,2,3,4,5,6,7],7
返回：[0,1,2,3,4,5,6]
```

## CM60	数组中的逆序对

```
题目描述
有一组数，对于其中任意两个数组，若前面一个大于后面一个数字，则这两个数字组成一个逆序对。请设计一个高效的算法，计算给定数组中的逆序对个数。

给定一个int数组A和它的大小n，请返回A中的逆序对个数。保证n小于等于5000。

测试样例：
[1,2,3,4,5,6,7,0],8
返回：7
```

##  CM61	无缓存交换

```
题目描述
请编写一个函数，函数内不使用任何临时变量，直接交换两个数的值。

给定一个int数组AB，其第零个元素和第一个元素为待交换的值，请返回交换后的数组。

测试样例：
[1,2]
返回：[2,1]
```

## CM62	井字棋

```
题目描述
对于一个给定的井字棋棋盘，请设计一个高效算法判断当前玩家是否获胜。

给定一个二维数组board，代表当前棋盘，其中元素为1的代表是当前玩家的棋子，为0表示没有棋子，为-1代表是对方玩家的棋子。

测试样例：
[[1,0,1],[1,-1,-1],[1,-1,0]]
返回：true
```

##  CM63	无判断max

```
题目描述
请编写一个方法，找出两个数字中最大的那个。条件是不得使用if-else等比较和判断运算符。

给定两个int a和b，请返回较大的一个数。若两数相同则返回任意一个。

测试样例：
1，2
返回：2
```

##  CM64	珠玑妙算

```
题目描述
我们现在有四个槽，每个槽放一个球，颜色可能是红色(R)、黄色(Y)、绿色(G)或蓝色(B)。例如，可能的情况为RGGB(槽1为红色，槽2、3为绿色，槽4为蓝色)，作为玩家，你需要试图猜出颜色的组合。比如，你可能猜YRGB。要是你猜对了某个槽的颜色，则算一次“猜中”。要是只是猜对了颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。

给定两个string A和guess。分别表示颜色组合，和一个猜测。请返回一个int数组，第一个元素为猜中的次数，第二个元素为伪猜中的次数。

测试样例：
"RGBY","GGRR"
返回：[1,1]
```

##  CM65	阶乘尾零

```
题目描述
请设计一个算法，计算n的阶乘有多少个尾随零。

给定一个int n，请返回n的阶乘的尾零个数。保证n为正整数。

测试样例：
5
返回：1
```

## CM66	最小调整有序

```
题目描述
有一个整数数组，请编写一个函数，找出索引m和n，只要将m和n之间的元素排好序，整个数组就是有序的。注意：n-m应该越小越好，也就是说，找出符合条件的最短序列。

给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的起点和终点。(原序列位置从0开始标号,若原序列有序，返回[0,0])。保证A中元素均为正整数。

测试样例：
[1,4,6,5,9,10],6
返回：[2,3]
```

##  CM67	数字发音

```
题目描述
有一个非负整数，请编写一个算法，打印该整数的英文描述。

给定一个int x，请返回一个string，为该整数的英文描述。

测试样例：
1234
返回："One Thousand,Two Hundred Thirty Four"
```

## CM68	最大连续数列和

```
题目描述
对于一个有正有负的整数数组，请找出总和最大的连续数列。

给定一个int数组A和数组大小n，请返回最大的连续数列的和。保证n的大小小于等于3000。

测试样例：
[1,2,3,-6,1]
返回：6
```

##  CM69	词频统计

```
题目描述
请设计一个高效的方法，找出任意指定单词在一篇文章中的出现频数。

给定一个string数组article和数组大小n及一个待统计单词word，请返回该单词在文章中的出现频数。保证文章的词数小于等于1000。
```

## CM70	整数对查找

```
题目描述
请设计一个高效算法，找出数组中两数之和为指定值的所有整数对。

给定一个int数组A和数组大小n以及需查找的和sum，请返回和为sum的整数对的个数。保证数组大小小于等于3000。

测试样例：
[1,2,3,4,5],5,6
返回：2
```

## CM71	树转链表

```
题目描述
有一个类似结点的数据结构TreeNode，包含了val属性和指向其它结点的指针。其可以用来表示二叉查找树(其中left指针表示左儿子，right指针表示右儿子)。请编写一个方法，将二叉查找树转换为一个链表，其中二叉查找树的数据结构用TreeNode实现，链表的数据结构用ListNode实现。

给定二叉查找树的根结点指针root，请返回转换成的链表的头指针。
```

##  CM72	另类加法

```
题目描述
请编写一个函数，将两个数字相加。不得使用+或其他算数运算符。

给定两个int A和B。请返回A＋B的值

测试样例：
1,2
返回：3
```

##  CM73	2的个数

```
题目描述
请编写一个方法，输出0到n(包括n)中数字2出现了几次。

给定一个正整数n，请返回0到n的数字中2出现了几次。

测试样例：
10
返回：1
```

##  CM74	下一个较大元素

```
题目描述
现在我们有一个int数组，请你找出数组中每个元素的下一个比它大的元素。

给定一个int数组A及数组的大小n，请返回一个int数组，代表每个元素比他大的下一个元素,若不存在则为-1。保证数组中元素均为正整数。

测试样例：
[11,13,10,5,12,21,3],7
返回：[13,21,12,12,21,-1,-1]
```

##  CM75	下一个较大元素II

```
题目描述
现在有一个数组，请找出数组中每个元素的后面比它大的最小的元素，若不存在则为-1。

给定一个int数组A及数组的大小n，请返回每个元素所求的值组成的数组。保证A中元素为正整数，且n小于等于1000。

测试样例：
[11,13,10,5,12,21,3],7
[12,21,12,12,21,-1,-1]
```

##  CM76	单词最近距离

```
题目描述
有一篇文章内含多个单词，现给定两个单词，请设计一个高效算法，找出文中这两个单词的最短距离(即最少相隔的单词数,也就是两个单词在文章中位置的差的绝对值)。

给定一个string数组article，代表所给文章，同时给定文章的单词数n和待查找的两个单词x和y。请返回两个单词的最短距离。保证两个单词均在文中出现且不相同，同时保证文章单词数小于等于1000。
```

##  CM77	最长合成字符串

```
题目描述
有一组单词，请编写一个程序，在数组中找出由数组中字符串组成的最长的串A，即A是由其它单词组成的(可重复)最长的单词。

给定一个string数组str，同时给定数组的大小n。请返回最长单词的长度，保证题意所述的最长单词存在。

测试样例：
["a","b","c","ab","bc","abc"],6
返回：3
```

##  CM78	子串判断

```
题目描述
现有一个小写英文字母组成的字符串s和一个包含较短小写英文字符串的数组p，请设计一个高效算法，对于p中的每一个较短字符串，判断其是否为s的子串。

给定一个string数组p和它的大小n，同时给定string s，为母串，请返回一个bool数组，每个元素代表p中的对应字符串是否为s的子串。保证p中的串长度小于等于8，且p中的串的个数小于等于500，同时保证s的长度小于等于1000。

测试样例：
["a","b","c","d"],4,"abc"
返回：[true,true,true,false]
```

## CM79	实时中位数

```
题目描述
现有一些随机生成的数字要将其依次传入，请设计一个高效算法，对于每次传入一个数字后，算出当前所有传入数字的中位数。(若传入了偶数个数字则令中位数为第n/2小的数字，n为已传入数字个数)。

给定一个int数组A，为传入的数字序列，同时给定序列大小n，请返回一个int数组，代表每次传入后的中位数。保证n小于等于1000。

测试样例：
[1,2,3,4,5,6],6
返回：[1,1,2,2,3,3]
```

##  CM80	字符串变换

```
题目描述
现有一个字典，同时给定字典中的两个字符串s和t，给定一个变换，每次可以改变字符串中的任意一个字符，请设计一个算法，计算由s变换到t所需的最少步数，同时需要满足在变换过程中的每个串都是字典中的串。

给定一个string数组dic，同时给定数组大小n，串s和串t，请返回由s到t变换所需的最少步数。若无法变换到t则返回-1。保证字符串长度均小于等于10，且字典中字符串数量小于等于500。

测试样例：
["abc","adc","bdc","aaa”],4,”abc","bdc"
返回：2
```

##  CM81	最大子方阵

```
题目描述
有一个方阵，其中每个单元(像素)非黑即白(非0即1)，请设计一个高效算法，找到四条边颜色相同的最大子方阵。

给定一个01方阵mat，同时给定方阵的边长n，请返回最大子方阵的边长。保证方阵边长小于等于100。

测试样例：
[[1,1,1],[1,0,1],[1,1,1]],3
返回：3
```

## CM82	最大和子矩阵

```
题目描述
有一个正整数和负整数组成的NxN矩阵，请编写代码找出元素总和最大的子矩阵。请尝试使用一个高效算法。

给定一个int矩阵mat和矩阵的阶数n，请返回元素总和最大的子矩阵的元素之和。保证元素绝对值小于等于100000，且矩阵阶数小于等于200。

测试样例：
[[1,2,-3],[3,4,-5],[-5,-6,-7]],3
返回：10
```

##  CM83	最大字母矩阵

```
题目描述
有一个单词清单，请设计一个高效算法，计算由清单中单词组成的最大子矩阵，要求矩阵中的行和列都是清单中的单词。

给定一个string数组dic，代表单词清单，同时给定清单的大小n，请返回最大子矩阵的面积。保证单词清单的大小小于等于50，且某一长度的串的数量小于等于12。

测试样例：
["aaa","aaa","aaa","bb","bb"]
返回：9
```
