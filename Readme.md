Main.py Data Generation Project

Overview
The main.py script is a powerful tool used for data generation. The script calculates and systematically appends data to a CSV file, which can be analyzed or used for further processing. Each row in the output file corresponds to a unique integer value, identified by the 'mod m' feature.

Features
The output CSV file includes the following columns, each representing a specific mathematical or statistical property:

'mod m': The modulus of the number being processed.
'parity': The parity (odd or even) of the number.
'prime factors': The total number of prime factors.
'unique prime factors': The total number of unique prime factors.
'max prime powers': The maximum power of any prime factor.
'range prime factors': The range of the prime factors.
'max gap': The maximum gap between consecutive prime factors.
'totient': The totient of the number.
'divisors': The total number of divisors.
'sum of divisors': The sum of all divisors.
'mobius': The value of the Möbius function at the number.
'saturation': The saturation of the number.
'R': A calculated ratio associated with the number.
'Mr': Another calculated ratio associated with the number.
'graph density': The density of a graph associated with the number.
'triangles': The number of triangles in the graph.
'transitivity': The transitivity of the graph.
'cliques': The maximum clique size in the graph.

Resuming the Script
The script is designed to be robust against interruptions. It initiates the data generation starting with a user-defined 'm' value. In the event of a crash or intentional halt, the program can be restarted at the last 'm' value, preventing data loss and ensuring the CSV file's continuity. This feature makes main.py highly flexible and adaptable to varying computational environments and execution durations.
