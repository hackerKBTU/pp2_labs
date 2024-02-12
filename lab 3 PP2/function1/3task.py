def solve(numheads, numlegs):
    for i in range(1, numheads + 1):
        num_chicks = i
        num_rabbits = numheads - i
        if num_chicks * 2 + num_rabbits * 4 == numlegs:
            print(f"Number of rabbits = {num_rabbits} and Number of chicks = {num_chicks}")
            break

solve(35, 94)
