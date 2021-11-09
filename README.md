Implementing the algorithm as given in the paper: 
# Computing Square Roots Faster than the Tonelli-Shanks/Bernstein Algorithm.
 Paper [link](ia.cr/2020/1407).
 
 Algorithm 1 as given in the paper is implemented in the algo1.py. This is the without table lookup variant that requires T+O(n<sup>3/2</sup>) operations.
 
In the case n = 16, for example: prime = 65537, for various squares in Zp, the script requires around 52 total operations(Squarings and Multiplications) besides T, which is consistent with the results in Table 1 in the paper.
 
