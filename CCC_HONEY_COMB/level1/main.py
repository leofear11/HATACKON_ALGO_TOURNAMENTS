with open("level1_5.in", "r") as f_in, open("solution_level1_5.out", "w") as f_out:
    f_in = f_in.read().strip().split()
    cellCount = "".join(f_in).count("O")
    f_out.write(str(cellCount) + "\n")