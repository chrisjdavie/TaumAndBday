'''
Solving the hackerrank Taum and B'day puzzle.

https://www.hackerrank.com/challenges/taum-and-bday

-------------------------

Problem Statement

Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy B number of black gifts and W number of white gifts.

The cost of each black gift is X units.
The cost of every white gift is Y units.
The cost of converting each black gift into white gift or vice versa is Z units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

Input Format

The first line will contain an integer T which will be the number of test cases.
There will be T pairs of lines. The first line of each test case will contain the values of integers B and W. Another line of each test case will contain the values of integers X, Y, and Z.

Constraints 
1=<T=<10 
0=<X,Y,Z,B,W=<109
Output Format

T lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.

-------------------------

Created on 31 Dec 2015

@author: chris
'''

for _ in range(input()):
    numBlack, numWhite = map(int, raw_input().strip().split())
    costBlack, costWhite, costConvert = map(int, raw_input().strip().split())
    
    costBlackProc = costBlack
    costWhiteProc = costWhite
    
    if costBlack > costWhite + costConvert:
        costBlackProc = costWhite + costConvert
    if costWhite > costBlack + costConvert:
        costWhiteProc = costBlack + costConvert
    
    print numBlack*costBlackProc + numWhite*costWhiteProc