# Python If-Else

**Task**

Given an integer, **$\eta$**, perform the following conditional actions:

- If **$\eta$** is odd, print *Weird*
- If **$\eta$** is even and in the inclusive range of **2** to **5**, print *Not Weird*
- If **$\eta$** is even and in the inclusive range of **6** to **20**, print *Weird*
- If **$\eta$** is even and greater than **20**, print *Not Weird*

**Input Format**

A single line containing a positive integer, **$\eta$**.

**Constraints**
- $1 \leq \eta \leq 100$


**Output Format**

Print *Weird* if the number is weird. Otherwise, print *Not Weird*.

**Sample Input 0**
```shell
3
```

**Sample Output 0**
```shell
Weird
```

**Explanation 0**

$\eta = 3$
$\eta$ is odd and odd numbers are weird, so print *Weird*.

**Sample Input 1**
```shell
24
```

**Sample Output 1**
```shell
Not Weird
```

**Explanation 1**

$\eta = 24$

$\eta > 20$ and $\eta$ is even, so it is not weird.
