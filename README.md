# Find if point is in ring Codility challnge solved in Python
A ring is an area limited by two circles that have the same center but different radius. In this task we consider only rings whose center is at (0,0). 

For example, a ring with inner radius 1 and outer radius 3 appears as follows: 

![Image 1](/1.png)

There are N distinct points on the plane (numbered from 0 to N-1) The K-th point lies at coordinate (points_x[K], points_y[K]) 

Your task is to count how many of these points lie strictly inside the ring (the border of the ring is not included). 

Write a function: 
  
  `def solution(inner, outer, points x, points_ y) `
  
that, given integers inner and outer (which denote, respectively, the inner and outer radius of the ring) and two arrays of N integers each: points_x and points_y, returns the number of points which lie strictly inside the ring. 

## Examples 

1. Given inner = 1, outer = 3, points_x = [0, 1, 2, -2, 3] and points_y = [0, 1, 4, 1, 0], the function should return 2, because only points (-2, 1) and (1, 1) lie inside the ring. 

![Image 2](/2.png)

2. Given inner = 2, outer = 4, points_x = [4, 0, 1, -2] and points_y = [-4, 4, 3, 0], the function should return 1, because only point (1, 3) lies inside the ring. 

![Image 3](/3.png)

Assume that:
* N is an integer within the range [1..1,000]; 
* inner is an integer within the range [0..9,999]; 
* outer is an integer within the range [1 ..1 0,000]; • inner < outer; 
* arrays points_x and points_y have the same length N; 
* each element of arrays points_y, points_y is an integer within the range [-10,000..10,000]; 
* given points are pairwise distinct. 

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment. 
