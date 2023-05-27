Parallel Computation of Number-Theoretic and Graph Properties
This Python script performs a variety of number-theoretic and graph computations on a range of integers, using multiple cores to speed up the computation.

Description
The script computes the following properties for each integer m in a given range:

Various number-theoretic properties, such as the number and multiplicity of prime factors, the sum of divisors, the totient, and the Möbius function.
Properties of a certain graph associated with m, such as its density, the number of triangles, the transitivity, and the size of the largest clique.
Some properties that combine number theory and graph theory, such as the "saturation" and the "R" and "Mr" values.
The script uses Python's built-in concurrent.futures module to parallelize the computations and thereby speed up the total processing time.

Usage
To run the script, you just need to specify the range of integers you're interested in and the number of worker processes you want to use. This can be done at the bottom of the script, in the if __name__ == '__main__': section.

The script will then compute all of the above properties for each integer in the given range, using the specified number of workers.

For each m, the results are initially written to a separate CSV file. After all computations are complete, these individual CSV files are combined into one large CSV file, and the individual files are deleted.

Requirements
The script requires the following Python libraries:

os
pandas
sympy
networkx
numpy
time
concurrent.futures
Performance
The script can be run on any machine with a Python interpreter and the required libraries. However, the performance benefits of parallelization will be more noticeable on machines with multiple cores.

In our tests, using 4 cores was about twice as fast as using 2 cores, and using 8 cores was still faster, though the speedup was less pronounced. For machines with hyper-threading, using a number of workers up to the total number of logical cores can still provide a performance improvement, though again the improvement is less pronounced compared to the number of physical cores.

Note that the optimal number of workers can depend on various factors, such as the specific characteristics of your workload and your computer's hardware and operating system.

Future Work
In future, we plan to extend the range of number-theoretic and graph properties computed by the script. Suggestions for additional properties to include are welcome.
