# Stable Matching 
Stable matching problem is solved by implementing Gale–Shapley algorithm.  
Input for the program can be provided by stdin or by piping file, matching is provided in stdout.  
#### Read from files
```
cat friends_in.txt | python3 sm.py
cat illiad_in.txt | python3 sm.py
```
#### Compare result with the expected output (no output from diff = no difference)
```
cat illiad_in.txt | python3 sm.py > result.txt
diff -w illiad_out.txt result.txt 
```

## Gale-Shapley algorithm
```
Initially all m∈M and w∈W are free
While there is a man m who is free and hasn’t proposed to every woman
    Choose such a man m
    Let w be the highest-ranked woman in m’s preference list 
        to whom m has not yet proposed 
    If w is free then
        (m, w) become engaged
    Else w is currently engaged to m′
        If w prefers m′ to m then
            m remains free
        Else w prefers m to m′ 
            (m, w) become engaged 
            m′ becomes free
        Endif 
     Endif
Endwhile
Return the set S of engaged pairs
```
## Sources
Gale-Shapley algorithm pseudocode from book "Algorithm Design" by Jon Kleinberg & Eva Tardos  
Input and output files from course conducted by Thore Husfeldt

## Further reading

Stable marriage Wikipedia : https://en.wikipedia.org/wiki/Stable_marriage_problem  
Gale-Shapley algorithm Wikipedia : https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
