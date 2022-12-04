-: ADVENT OF CODE (Day 04) :-

Problem Link: https://adventofcode.com/2022/day/4

-: Part 1 :-

We had to find if one section falls under the other section. 

```
 S1_start                              S1_end             
    +------------------------------------+                
    |                                    |                
    +------------------------------------+                
           +-----------------------+                      
           |                       |                      
           +-----------------------+                      
         S2_start               S2_end      
```
So, we can simply make the check if S1_start <= S2_start and S1_end >= S2_end. This an be other way around as well i.e S2_start <= S1_start and S2_end >= S1_end.    

-: Part 2 :-

We had to find if there is even partial overlap between the two sections.

```
                                      
 S1_start             S1_end                                
    +--------------------+                                  
    |                    |                                  
    +--------------------+                                  
            +-----------------------+                       
            |                       |                       
            +-----------------------+                       
          S2_start               S2_end                     
                                                   
```

In this case a simple way to check would be find the range of the overlap.

start = max(S1_start, S2_start) and end = min(S1_end, S2_end)

Now, if start <= end, then there is an overlap.

Link to my solution: https://github.com/arnabsen1729/aoc-2022/blob/main/day04/solution.py