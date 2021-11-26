Implementing the algorithm as given in the paper: 
# Computing Square Roots Faster than the Tonelli-Shanks/Bernstein Algorithm.
 Paper [link](ia.cr/2020/1407).
 
Algorithm 1 as given in the paper is implemented in the algo1.py. This is the without table lookup variant that requires T+O(n<sup>3/2</sup>) operations.

Comparison between Table 1 from paper and python script on the number of operations(Squarings and Multiplications) besides T:

| n  | Paper             | Paper | Script            | Script | Difference   |
|----|-------------------|-------|-------------------|--------|--------------|
|    | ops               | #tot  | ops               | #tot   | Script-Paper |
| 16 | 26.0[S]+26.0[M]   | 52.0  | 25.9[S]+27.4[M]   | 53.3   | 1.3          |
| 32 | 66.5[S]+68.0[M]   | 134.5 | 66.3[S]+67.8[M]   | 134.1  | -0.4         |
| 48 | 121.5[S]+114.0[M] | 235.5 | 121.1[S]+112.5[M] | 233.6  | -1.9         |
| 64 | 181.0[S]+170.0[M] | 351.0 | 180.8[S]+166.7[M] | 347.5  | -3.5         |
| 80 | 246.5[S]+231.5[M] | 478.0 | 247.9[S]+226.8[M] | 474.7  | -3.3         |
| 96 | 313.5[S]+300.0[M] | 613.5 | 312.3[S]+289.5[M] | 601.8  | -11.7        |

Results from the script are calculated by taking a random square in Zp and averaging the count for 1000 different primes for a particular n.
Data for the above table is generated using test.py script. Primes for testing are found using Miller-Rabin primality test.
