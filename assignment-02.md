# CMPS 2200 Assignment 2

**Name:**___Quin Moore______________________

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py`.. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$ k = 1
  * $W(n/3)=2W(n/9)+1$
  * $W(n)=2*2W(n/9)+1+1$ k = 2 
  * $W(n/9)=2W(n/27)+1$
  * $W(n)=2*2*2W(n/27)+1+1+1$ k = 3
  * $W(n)=2^k*W(n/3^k)+k
  * n = 3^k
  * log3(n) = k
  * W(n)=2^log3(n)*W(1)+log3(n)
  * Asymptotic upper bound is 2^log3(n)
.  Big O(n)
   * height is  log3𝑛 
  
* num nodes at level  𝑖  is  2𝑖 

* num nodes at level  log3𝑛  is  2log3𝑛∈𝑂(𝑛𝑙𝑜𝑔32)
.  
.  
.  
.  
  * $W(n)=5W(n/4)+n$
  * W(n/4)=5W(n/16)+n
  * W(n)=5*5W(n/16)+n+n
  * W(n/16)=5W(n/64)+n
  * W(n)=5*5*5W(n/64)+n+n+n
  * W(n)=5^k*W(n/4^k)+k*n
  * n=4^k
  * log4(n)=k
  * W(n)=5^log4(n)*W(1)+log4(n)*n
  * Aymptotic upper bound is log4(n)*n
  * Big O(nlog(n))
  * num levels is  log4𝑛
  * num nodes at level  𝑖  is  5𝑖
  * ⇒5log4𝑛∈𝑂(𝑛log45)
.  
.  
.  
.  
.  
  * $W(n)=7W(n/7)+n$
  * W(n/7)=7W(n/49)+n
  * W(n)=7*7W(n/49)+n+n
  * W(n)=7^k*W(n/7^k)+k*n
  * n=7^k
  * log7(n)=k
  * W(n)=7^log7(n)*W(1)+log7(n)*n
  * W(n)=n+log7(n)*n
  * Aymptotic upepr bound is log7(n)*n
.   Big O(nlog(n))
    * max cost per level is
    * 𝑛 num levels =  log7𝑛
    * ⇒𝑂(𝑛log7𝑛)
    
.  
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
  * W(n/3) = 9W(n/9)+n^2
  * W(n)=9*9W(n/9)+n^2+n^2
  * W(n)=9^kW(n/3^k)+kn^2
  * n = 3^k
  * log3(n)=k
  * W(n)=9^log3(n)*W(1)+log(n)*n^2
  * Aymptotic upper bound is log(n)*n^2
  * max cost per level is  𝑛2
  * num levels =  log3𝑛
  * ⇒𝑂(𝑛2log3𝑛)
.  
.  
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
  * W(n/2)=8W(n/4)+n^3
  * W(n) = 8*8W(n/4)+n^3+n^3
  * W(n) = 8^k*W(n/2^k)+kn^3
  * log2(n)=k
  * W(n) = 8^log2(n)*W(1)+log2(n)*n^3
  * W(n)=4n+log(n)*n^3
  * Aysmptotic upper bound is log(n)*n^3
  * 𝑂(𝑛3log2𝑛)  .
.  
.  
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
  * W(n/25)=49W(n/625) + n^3/2 * log(n)
  * W(n)=49*49W(n/625) + 2(n^3/2 * log(n))
  * W(n)=49^k*W(n/25^k)+k(n^3/2*log(n))
  * log25(n)=k
  * W(n)=49^log25(n)*W(1)+log25(n)*(n^3/2*log(n))
  * Asympototic upper bound is log25(n)*(n^3/2*log(n)
  * 𝑂(𝑛3/2log𝑛)
.  
.  
.  
.  
.  
  * $W(n)=W(n-1)+2$
  * W(n-1)=W(n-2)+2
  * W(n)=W(n-2)+2+2
  * W(n-2)=W(n-3)+2
  * W(n)=W(n-3)+2+2+2
  * W(n)=W(n-k)+2k
  * n=k
  * W(n)=W(1)+2n
  * Asymptotic upper bound is 2n
  * 𝑂(𝑛)
.  
.  
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
  * W(n-1)=W(n-2)+n^c
  * W(n)=W(n-2)+2(n^c)
  * W(n)=W(n-k)+k(n^c)
  * n=k
  * W(n)=W(1)+n*n^c
  * n*n^c=n^c+1=n^c
  * Asymptotic upper bound is n^c
  * 𝑂(𝑛𝑐+1)
.  
.  
.  
.  
.  
  * $W(n)=W(\sqrt{n})+1$
  * W(sqrt(n))=W(n^1/4)+1
  * W(n)=W(n^1/4)+1+1
  * W(n)=W(n^1/2^k)+k
  * n^1/2^k=1
  * n=1^2^k
  * log(n)=2^k
  * log(log(n))=k
  * W(n)=W(1)+  log(log(n))
  * Asymptotic upper bound is log(log(n))
  * 𝑂(lglg𝑛)


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
W(n) = 5W(n/2) + n
W(n/2)= 5W(n/4) + n
W(n)=5*5W(n/4) +2n
W(n)=5^k*W(n/2^k)+kn
log2(n)=k
W(n)=5^log2(n)*W(1)+log2(n)*n
Asymptotic run time is nlog(n)
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
W(n) = 2W(n-1) + c
W(n-1)=2W(n-2)+c
W(n)=2*2W(n-2)+c+c
W(n)=2^kW(n-k)+ kc
n=k
W(n)=2^n*W(1)+nc
Asymptotic run time is 2^n
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.
W(n)= 9W(n/3) + n^2
W(n/3)=9W(n/3)+n^2
W(n)=9*9W(n/9)+2(n^2)
W(n)=9^k*W(n/3^k)+kn^2
log3(n)=k
W(n)=9^log3(n)*W(1)+log3(n)*n^2
W(n)=3n+log3(n)*n^2
Asymptotic run time is log3(n)*n^2
    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?
I would choose the first algorithim with run time nlog(n). nlog(n) is less than log3(n)*n^2 is less than 2^n

3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


