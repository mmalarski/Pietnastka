import matplotlib.pyplot as plt
import numpy as np

# ogółem
sol_len_bfs = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs = [0, 0, 0, 0, 0, 0, 0]
sol_len_astr = [0, 0, 0, 0, 0, 0, 0]

visited_count_bfs = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs = [0, 0, 0, 0, 0, 0, 0]
visited_count_astr = [0, 0, 0, 0, 0, 0, 0]

processed_count_bfs = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs = [0, 0, 0, 0, 0, 0, 0]
processed_count_astr = [0, 0, 0, 0, 0, 0, 0]

depth_avr_bfs = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs = [0, 0, 0, 0, 0, 0, 0]
depth_avr_astr = [0, 0, 0, 0, 0, 0, 0]

time_avg_bfs = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs = [0, 0, 0, 0, 0, 0, 0]
time_avg_astr = [0, 0, 0, 0, 0, 0, 0]

# A*
sol_len_hamm = [0, 0, 0, 0, 0, 0, 0]
sol_len_manh = [0, 0, 0, 0, 0, 0, 0]

visited_count_hamm = [0, 0, 0, 0, 0, 0, 0]
visited_count_manh = [0, 0, 0, 0, 0, 0, 0]

processed_count_hamm = [0, 0, 0, 0, 0, 0, 0]
processed_count_manh = [0, 0, 0, 0, 0, 0, 0]

depth_avr_hamm = [0, 0, 0, 0, 0, 0, 0]
depth_avr_manh = [0, 0, 0, 0, 0, 0, 0]

time_avg_hamm = [0, 0, 0, 0, 0, 0, 0]
time_avg_manh = [0, 0, 0, 0, 0, 0, 0]

# bfs
sol_len_bfs_rdul = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_drul = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_drlu = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_ludr = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_lurd = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_uldr = [0, 0, 0, 0, 0, 0, 0]
sol_len_bfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

visited_count_bfs_rdul = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_drul = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_drlu = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_ludr = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_lurd = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_uldr = [0, 0, 0, 0, 0, 0, 0]
visited_count_bfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

processed_count_bfs_rdul = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_drul = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_drlu = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_ludr = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_lurd = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_uldr = [0, 0, 0, 0, 0, 0, 0]
processed_count_bfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

depth_avr_bfs_rdul = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_drul = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_drlu = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_ludr = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_lurd = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_uldr = [0, 0, 0, 0, 0, 0, 0]
depth_avr_bfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

time_avg_bfs_rdul = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_drul = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_drlu = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_ludr = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_lurd = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_uldr = [0, 0, 0, 0, 0, 0, 0]
time_avg_bfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

# dfs
sol_len_dfs_rdul = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_drul = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_drlu = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_ludr = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_lurd = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_uldr = [0, 0, 0, 0, 0, 0, 0]
sol_len_dfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

visited_count_dfs_rdul = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_drul = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_drlu = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_ludr = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_lurd = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_uldr = [0, 0, 0, 0, 0, 0, 0]
visited_count_dfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

processed_count_dfs_rdul = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_drul = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_drlu = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_ludr = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_lurd = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_uldr = [0, 0, 0, 0, 0, 0, 0]
processed_count_dfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

depth_avr_dfs_rdul = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_drul = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_drlu = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_ludr = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_lurd = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_uldr = [0, 0, 0, 0, 0, 0, 0]
depth_avr_dfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

time_avg_dfs_rdul = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_rdlu = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_drul = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_drlu = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_ludr = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_lurd = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_uldr = [0, 0, 0, 0, 0, 0, 0]
time_avg_dfs_ulrd = [0, 0, 0, 0, 0, 0, 0]

file = open("message.txt", "r")
Lines = file.readlines()
file.close()

# for line in Lines:
#     line.split(" ")

for whatever in Lines:
    listline = whatever.split(" ")
    line = [0, 0, "", "", 0, 0, 0, 0, 0.0]
    line[0] = int(listline[0])
    line[1] = int(listline[1])
    line[2] = listline[2]
    line[3] = listline[3]
    line[4] = int(listline[4])
    line[5] = int(listline[5])
    line[6] = int(listline[6])
    line[7] = int(listline[7])
    line[8] = float(listline[8])
    index = int(line[0]) - 1
    if line[2] == "bfs":
        sol_len_bfs[index] += line[4]
        visited_count_bfs[index] += line[5]
        processed_count_bfs[index] += line[6]
        depth_avr_bfs[index] += line[7]
        time_avg_bfs[index] += line[8]
        if line[3] == "rdul":
            sol_len_bfs_rdul[index] += line[4]
            visited_count_bfs_rdul[index] += line[5]
            processed_count_bfs_rdul[index] += line[6]
            depth_avr_bfs_rdul[index] += line[7]
            time_avg_bfs_rdul[index] += line[8]
        if line[3] == "rdlu":
            sol_len_bfs_rdlu[index] += line[4]
            visited_count_bfs_rdlu[index] += line[5]
            processed_count_bfs_rdlu[index] += line[6]
            depth_avr_bfs_rdlu[index] += line[7]
            time_avg_bfs_rdlu[index] += line[8]
        if line[3] == "drul":
            sol_len_bfs_drul[index] += line[4]
            visited_count_bfs_drul[index] += line[5]
            processed_count_bfs_drul[index] += line[6]
            depth_avr_bfs_drul[index] += line[7]
            time_avg_bfs_drul[index] += line[8]
        if line[3] == "drlu":
            sol_len_bfs_drlu[index] += line[4]
            visited_count_bfs_drlu[index] += line[5]
            processed_count_bfs_drlu[index] += line[6]
            depth_avr_bfs_drlu[index] += line[7]
            time_avg_bfs_drlu[index] += line[8]
        if line[3] == "ludr":
            sol_len_bfs_ludr[index] += line[4]
            visited_count_bfs_ludr[index] += line[5]
            processed_count_bfs_ludr[index] += line[6]
            depth_avr_bfs_ludr[index] += line[7]
            time_avg_bfs_ludr[index] += line[8]
        if line[3] == "lurd":
            sol_len_bfs_lurd[index] += line[4]
            visited_count_bfs_lurd[index] += line[5]
            processed_count_bfs_lurd[index] += line[6]
            depth_avr_bfs_lurd[index] += line[7]
            time_avg_bfs_lurd[index] += line[8]
        if line[3] == "uldr":
            sol_len_bfs_uldr[index] += line[4]
            visited_count_bfs_uldr[index] += line[5]
            processed_count_bfs_uldr[index] += line[6]
            depth_avr_bfs_uldr[index] += line[7]
            time_avg_bfs_uldr[index] += line[8]
        if line[3] == "ulrd":
            sol_len_bfs_ulrd[index] += line[4]
            visited_count_bfs_ulrd[index] += line[5]
            processed_count_bfs_ulrd[index] += line[6]
            depth_avr_bfs_ulrd[index] += line[7]
            time_avg_bfs_ulrd[index] += line[8]
    elif line[2] == "dfs":
        sol_len_dfs[index] += line[4]
        visited_count_dfs[index] += line[5]
        processed_count_dfs[index] += line[6]
        depth_avr_dfs[index] += line[7]
        time_avg_dfs[index] += line[8]
        if line[3] == "rdul":
            sol_len_dfs_rdul[index] += line[4]
            visited_count_dfs_rdul[index] += line[5]
            processed_count_dfs_rdul[index] += line[6]
            depth_avr_dfs_rdul[index] += line[7]
            time_avg_dfs_rdul[index] += line[8]
        if line[3] == "rdlu":
            sol_len_dfs_rdlu[index] += line[4]
            visited_count_dfs_rdlu[index] += line[5]
            processed_count_dfs_rdlu[index] += line[6]
            depth_avr_dfs_rdlu[index] += line[7]
            time_avg_dfs_rdlu[index] += line[8]
        if line[3] == "drul":
            sol_len_dfs_drul[index] += line[4]
            visited_count_dfs_drul[index] += line[5]
            processed_count_dfs_drul[index] += line[6]
            depth_avr_dfs_drul[index] += line[7]
            time_avg_dfs_drul[index] += line[8]
        if line[3] == "drlu":
            sol_len_dfs_drlu[index] += line[4]
            visited_count_dfs_drlu[index] += line[5]
            processed_count_dfs_drlu[index] += line[6]
            depth_avr_dfs_drlu[index] += line[7]
            time_avg_dfs_drlu[index] += line[8]
        if line[3] == "ludr":
            sol_len_dfs_ludr[index] += line[4]
            visited_count_dfs_ludr[index] += line[5]
            processed_count_dfs_ludr[index] += line[6]
            depth_avr_dfs_ludr[index] += line[7]
            time_avg_dfs_ludr[index] += line[8]
        if line[3] == "lurd":
            sol_len_dfs_lurd[index] += line[4]
            visited_count_dfs_lurd[index] += line[5]
            processed_count_dfs_lurd[index] += line[6]
            depth_avr_dfs_lurd[index] += line[7]
            time_avg_dfs_lurd[index] += line[8]
        if line[3] == "uldr":
            sol_len_dfs_uldr[index] += line[4]
            visited_count_dfs_uldr[index] += line[5]
            processed_count_dfs_uldr[index] += line[6]
            depth_avr_dfs_uldr[index] += line[7]
            time_avg_dfs_uldr[index] += line[8]
        if line[3] == "ulrd":
            sol_len_dfs_ulrd[index] += line[4]
            visited_count_dfs_ulrd[index] += line[5]
            processed_count_dfs_ulrd[index] += line[6]
            depth_avr_dfs_ulrd[index] += line[7]
            time_avg_dfs_ulrd[index] += line[8]
    elif line[2] == "astr":
        sol_len_astr[index] += line[4]
        visited_count_astr[index] += line[5]
        processed_count_astr[index] += line[6]
        depth_avr_astr[index] += line[7]
        time_avg_astr[index] += line[8]
        if line[3] == "hamm":
            sol_len_hamm[index] += line[4]
            visited_count_hamm[index] += line[5]
            processed_count_hamm[index] += line[6]
            depth_avr_hamm[index] += line[7]
            time_avg_hamm[index] += line[8]
        elif line[3] == "manh":
            sol_len_manh[index] += line[4]
            visited_count_manh[index] += line[5]
            processed_count_manh[index] += line[6]
            depth_avr_manh[index] += line[7]
            time_avg_manh[index] += line[8]

for i in range(7):
    sol_len_bfs[i] = sol_len_bfs[i] / 3304
    sol_len_dfs[i] = sol_len_dfs[i] / 3304
    sol_len_astr[i] = sol_len_astr[i] / 826
    visited_count_bfs[i] = visited_count_bfs[i] / 3304
    visited_count_dfs[i] = visited_count_dfs[i] / 3304
    visited_count_astr[i] = visited_count_astr[i] / 826
    processed_count_bfs[i] = processed_count_bfs[i] / 3304
    processed_count_dfs[i] = processed_count_dfs[i] / 3304
    processed_count_astr[i] = processed_count_astr[i] / 826
    depth_avr_bfs[i] = depth_avr_bfs[i] / 3304
    depth_avr_dfs[i] = depth_avr_dfs[i] / 3304
    depth_avr_astr[i] = depth_avr_astr[i] / 826
    time_avg_bfs[i] = time_avg_bfs[i] / 3304
    time_avg_dfs[i] = time_avg_dfs[i] / 3304
    time_avg_astr[i] = time_avg_astr[i] / 826
    sol_len_hamm[i] = sol_len_hamm[i] / 413
    sol_len_manh[i] = sol_len_manh[i] / 413
    visited_count_hamm[i] = visited_count_hamm[i] / 413
    visited_count_manh[i] = visited_count_manh[i] / 413
    processed_count_hamm[i] = processed_count_hamm[i] / 413
    processed_count_manh[i] = processed_count_manh[i] / 413
    depth_avr_hamm[i] = depth_avr_hamm[i] / 413
    depth_avr_manh[i] = depth_avr_manh[i] / 413
    time_avg_hamm[i] = time_avg_hamm[i] / 413
    time_avg_manh[i] = time_avg_manh[i] / 413
    sol_len_bfs_rdul[i] = sol_len_bfs_rdul[i] / 413
    sol_len_bfs_rdlu[i] = sol_len_bfs_rdlu[i] / 413
    sol_len_bfs_drul[i] = sol_len_bfs_drul[i] / 413
    sol_len_bfs_drlu[i] = sol_len_bfs_drlu[i] / 413
    sol_len_bfs_ludr[i] = sol_len_bfs_ludr[i] / 413
    sol_len_bfs_lurd[i] = sol_len_bfs_lurd[i] / 413
    sol_len_bfs_uldr[i] = sol_len_bfs_uldr[i] / 413
    sol_len_bfs_ulrd[i] = sol_len_bfs_ulrd[i] / 413
    visited_count_bfs_rdul[i] = visited_count_bfs_rdul[i] / 413
    visited_count_bfs_rdlu[i] = visited_count_bfs_rdlu[i] / 413
    visited_count_bfs_drul[i] = visited_count_bfs_drul[i] / 413
    visited_count_bfs_drlu[i] = visited_count_bfs_drlu[i] / 413
    visited_count_bfs_ludr[i] = visited_count_bfs_ludr[i] / 413
    visited_count_bfs_lurd[i] = visited_count_bfs_lurd[i] / 413
    visited_count_bfs_uldr[i] = visited_count_bfs_uldr[i] / 413
    visited_count_bfs_ulrd[i] = visited_count_bfs_ulrd[i] / 413
    processed_count_bfs_rdul[i] = processed_count_bfs_rdul[i] / 413
    processed_count_bfs_rdlu[i] = processed_count_bfs_rdlu[i] / 413
    processed_count_bfs_drul[i] = processed_count_bfs_drul[i] / 413
    processed_count_bfs_drlu[i] = processed_count_bfs_drlu[i] / 413
    processed_count_bfs_ludr[i] = processed_count_bfs_ludr[i] / 413
    processed_count_bfs_lurd[i] = processed_count_bfs_lurd[i] / 413
    processed_count_bfs_uldr[i] = processed_count_bfs_uldr[i] / 413
    processed_count_bfs_ulrd[i] = processed_count_bfs_ulrd[i] / 413
    depth_avr_bfs_rdul[i] = depth_avr_bfs_rdul[i] / 413
    depth_avr_bfs_rdlu[i] = depth_avr_bfs_rdlu[i] / 413
    depth_avr_bfs_drul[i] = depth_avr_bfs_drul[i] / 413
    depth_avr_bfs_drlu[i] = depth_avr_bfs_drlu[i] / 413
    depth_avr_bfs_ludr[i] = depth_avr_bfs_ludr[i] / 413
    depth_avr_bfs_lurd[i] = depth_avr_bfs_lurd[i] / 413
    depth_avr_bfs_uldr[i] = depth_avr_bfs_uldr[i] / 413
    depth_avr_bfs_ulrd[i] = depth_avr_bfs_ulrd[i] / 413
    time_avg_bfs_rdul[i] = time_avg_bfs_rdul[i] / 413
    time_avg_bfs_rdlu[i] = time_avg_bfs_rdlu[i] / 413
    time_avg_bfs_drul[i] = time_avg_bfs_drul[i] / 413
    time_avg_bfs_drlu[i] = time_avg_bfs_drlu[i] / 413
    time_avg_bfs_ludr[i] = time_avg_bfs_ludr[i] / 413
    time_avg_bfs_lurd[i] = time_avg_bfs_lurd[i] / 413
    time_avg_bfs_uldr[i] = time_avg_bfs_uldr[i] / 413
    time_avg_bfs_ulrd[i] = time_avg_bfs_ulrd[i] / 413
    sol_len_dfs_rdul[i] = sol_len_dfs_rdul[i] / 413
    sol_len_dfs_rdlu[i] = sol_len_dfs_rdlu[i] / 413
    sol_len_dfs_drul[i] = sol_len_dfs_drul[i] / 413
    sol_len_dfs_drlu[i] = sol_len_dfs_drlu[i] / 413
    sol_len_dfs_ludr[i] = sol_len_dfs_ludr[i] / 413
    sol_len_dfs_lurd[i] = sol_len_dfs_lurd[i] / 413
    sol_len_dfs_uldr[i] = sol_len_dfs_uldr[i] / 413
    sol_len_dfs_ulrd[i] = sol_len_dfs_ulrd[i] / 413
    visited_count_dfs_rdul[i] = visited_count_dfs_rdul[i] / 413
    visited_count_dfs_rdlu[i] = visited_count_dfs_rdlu[i] / 413
    visited_count_dfs_drul[i] = visited_count_dfs_drul[i] / 413
    visited_count_dfs_drlu[i] = visited_count_dfs_drlu[i] / 413
    visited_count_dfs_ludr[i] = visited_count_dfs_ludr[i] / 413
    visited_count_dfs_lurd[i] = visited_count_dfs_lurd[i] / 413
    visited_count_dfs_uldr[i] = visited_count_dfs_uldr[i] / 413
    visited_count_dfs_ulrd[i] = visited_count_dfs_ulrd[i] / 413
    processed_count_dfs_rdul[i] = processed_count_dfs_rdul[i] / 413
    processed_count_dfs_rdlu[i] = processed_count_dfs_rdlu[i] / 413
    processed_count_dfs_drul[i] = processed_count_dfs_drul[i] / 413
    processed_count_dfs_drlu[i] = processed_count_dfs_drlu[i] / 413
    processed_count_dfs_ludr[i] = processed_count_dfs_ludr[i] / 413
    processed_count_dfs_lurd[i] = processed_count_dfs_lurd[i] / 413
    processed_count_dfs_uldr[i] = processed_count_dfs_uldr[i] / 413
    processed_count_dfs_ulrd[i] = processed_count_dfs_ulrd[i] / 413
    depth_avr_dfs_rdul[i] = depth_avr_dfs_rdul[i] / 413
    depth_avr_dfs_rdlu[i] = depth_avr_dfs_rdlu[i] / 413
    depth_avr_dfs_drul[i] = depth_avr_dfs_drul[i] / 413
    depth_avr_dfs_drlu[i] = depth_avr_dfs_drlu[i] / 413
    depth_avr_dfs_ludr[i] = depth_avr_dfs_ludr[i] / 413
    depth_avr_dfs_lurd[i] = depth_avr_dfs_lurd[i] / 413
    depth_avr_dfs_uldr[i] = depth_avr_dfs_uldr[i] / 413
    depth_avr_dfs_ulrd[i] = depth_avr_dfs_ulrd[i] / 413
    time_avg_dfs_rdul[i] = time_avg_dfs_rdul[i] / 413
    time_avg_dfs_rdlu[i] = time_avg_dfs_rdlu[i] / 413
    time_avg_dfs_drul[i] = time_avg_dfs_drul[i] / 413
    time_avg_dfs_drlu[i] = time_avg_dfs_drlu[i] / 413
    time_avg_dfs_ludr[i] = time_avg_dfs_ludr[i] / 413
    time_avg_dfs_lurd[i] = time_avg_dfs_lurd[i] / 413
    time_avg_dfs_uldr[i] = time_avg_dfs_uldr[i] / 413
    time_avg_dfs_ulrd[i] = time_avg_dfs_ulrd[i] / 413

# 1
X = ['1', '2', '3', '4', '5', '6', '7']
X_axis = np.arange(len(X))
plt.bar(X_axis - 0.2, sol_len_bfs, 0.2, label='BFS')
plt.bar(X_axis, sol_len_dfs, 0.2, label='DFS')
plt.bar(X_axis + 0.2, sol_len_astr, 0.2, label='A*')

plt.xticks(X_axis, X)
plt.xlabel("Głebokość")
plt.ylabel("Długość znalezionego rozwiązania")
plt.title("Ogółem")
plt.yscale('log')
plt.legend()
plt.show()

# 2
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, visited_count_bfs, 0.2, label = 'BFS')
# plt.bar(X_axis, visited_count_dfs, 0.2, label = 'DFS')
# plt.bar(X_axis + 0.2, visited_count_astr, 0.2, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów odwiedzonych")
# plt.yscale('log')
# plt.title("Ogółem")
# plt.legend()
# plt.show()


# 3
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, processed_count_bfs, 0.2, label = 'BFS')
# plt.bar(X_axis, processed_count_dfs, 0.2, label = 'DFS')
# plt.bar(X_axis + 0.2, processed_count_astr , 0.2, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów przetworzonych")
# plt.title("Ogółem")
# plt.legend()
# plt.show()

# 4
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, depth_avr_bfs, 0.2, label = 'BFS')
# plt.bar(X_axis, depth_avr_dfs, 0.2, label = 'DFS')
# plt.bar(X_axis + 0.2, depth_avr_astr, 0.2, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Maksymalna osiągnięta głębokość rekursji")
# plt.title("Ogółem")
# plt.legend()
# plt.show()

# 5
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, time_avg_bfs , 0.2, label = 'BFS')
# plt.bar(X_axis, time_avg_dfs, 0.2, label = 'DFS')
# plt.bar(X_axis + 0.2, time_avg_astr, 0.2, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Czas trwania procesu obliczeniowego")
# plt.title("Ogółem")
# plt.legend()
# plt.show()


# 6
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, sol_len_manh, 0.4, label = 'Manhattan')
# plt.bar(X_axis + 0.2, sol_len_hamm, 0.4, label = 'Hamming')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Długość znalezionego rozwiązania")
# plt.title("A*")
# plt.legend()
# plt.show()

# 7
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, visited_count_manh, 0.4, label = 'Manhattan')
# plt.bar(X_axis + 0.2, visited_count_hamm, 0.4, label = 'Hamming')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów odwiedzonych")
# plt.title("A*")
# plt.legend()
# plt.show()


# 8
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, processed_count_manh, 0.4, label = 'Manhattan')
# plt.bar(X_axis + 0.2, processed_count_hamm, 0.4, label = 'Hamming')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów przetworzonych")
# plt.title("A*")
# plt.legend()
# plt.show()

# 9
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, depth_avr_manh, 0.4, label = 'Manhattan')
# plt.bar(X_axis + 0.2, depth_avr_hamm, 0.4, label = 'Hamming')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Maksymalna osiągnięta głębokość rekursji")
# plt.title("A*")
# plt.legend()
# plt.show()

# 10
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, time_avg_manh, 0.4, label = 'Manhattan')
# plt.bar(X_axis + 0.2, time_avg_hamm, 0.4, label = 'Hamming')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Czas trwania procesu obliczeniowego")
# plt.title("A*")
# plt.legend()
# plt.show()


# 11
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.4, sol_len_bfs_rdul, 0.1, label = 'RDUL')
# plt.bar(X_axis - 0.3, sol_len_bfs_rdlu, 0.1, label = 'RDLU')
# plt.bar(X_axis - 0.2, sol_len_bfs_drul, 0.1, label = 'DRUL')
# plt.bar(X_axis - 0.1, sol_len_bfs_drlu, 0.1, label = 'DRLU')
# plt.bar(X_axis      , sol_len_bfs_ludr, 0.1, label = 'LUDR')
# plt.bar(X_axis + 0.1, sol_len_bfs_lurd, 0.1, label = 'LURD')
# plt.bar(X_axis + 0.2, sol_len_bfs_uldr, 0.1, label = 'ULDR')
# plt.bar(X_axis + 0.3, sol_len_bfs_ulrd, 0.1, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Długość znalezionego rozwiązania")
# plt.title("BFS")
# plt.legend()
# plt.show()

# 12
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.4, visited_count_bfs_rdul, 0.1, label = 'RDUL')
# plt.bar(X_axis - 0.3, visited_count_bfs_rdlu, 0.1, label = 'RDLU')
# plt.bar(X_axis - 0.2, visited_count_bfs_drul, 0.1, label = 'DRUL')
# plt.bar(X_axis - 0.1, visited_count_bfs_drlu, 0.1, label = 'DRLU')
# plt.bar(X_axis      , visited_count_bfs_ludr, 0.1, label = 'LUDR')
# plt.bar(X_axis + 0.1, visited_count_bfs_lurd, 0.1, label = 'LURD')
# plt.bar(X_axis + 0.2, visited_count_bfs_uldr, 0.1, label = 'ULDR')
# plt.bar(X_axis + 0.3, visited_count_bfs_ulrd, 0.1, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów odwiedzonych")
# plt.yscale('log')
# plt.title("BFS")
# plt.legend()
# plt.show()


# 13
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, processed_count_bfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, processed_count_bfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, processed_count_bfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, processed_count_bfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, processed_count_bfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, processed_count_bfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, processed_count_bfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, processed_count_bfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów przetworzonych")
# plt.title("BFS")
# plt.legend()
# plt.show()

# 14
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, depth_avr_bfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, depth_avr_bfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, depth_avr_bfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, depth_avr_bfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, depth_avr_bfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, depth_avr_bfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, depth_avr_bfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, depth_avr_bfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Maksymalna osiągnięta głębokość rekursji")
# plt.title("BFS")
# plt.legend()
# plt.show()

# 15
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, time_avg_bfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, time_avg_bfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, time_avg_bfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, time_avg_bfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, time_avg_bfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, time_avg_bfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, time_avg_bfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, time_avg_bfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Czas trwania procesu obliczeniowego")
# plt.title("BFS")
# plt.legend()
# plt.show()


# 16
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, sol_len_dfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, sol_len_dfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, sol_len_dfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, sol_len_dfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, sol_len_dfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, sol_len_dfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, sol_len_dfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, sol_len_dfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Długość znalezionego rozwiązania")
# plt.title("DFS")
# plt.legend()
# plt.show()

# 17
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, visited_count_dfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, visited_count_dfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, visited_count_dfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, visited_count_dfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, visited_count_dfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, visited_count_dfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, visited_count_dfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, visited_count_dfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów odwiedzonych")
# plt.title("DFS")
# plt.legend()
# plt.show()


# 18
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, processed_count_dfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, processed_count_dfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, processed_count_dfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, processed_count_dfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, processed_count_dfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, processed_count_dfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, processed_count_dfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, processed_count_dfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów przetworzonych")
# plt.title("DFS")
# plt.legend()
# plt.show()

# 19
# X = ['1', '2', '3', '4', '5', '6', '7']d
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, depth_avr_dfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, depth_avr_dfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, depth_avr_dfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, depth_avr_dfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, depth_avr_dfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, depth_avr_dfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, depth_avr_dfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, depth_avr_dfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Maksymalna osiągnięta głębokość rekursji")
# plt.title("DFS")
# plt.legend()
# plt.show()

# 20
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, time_avg_dfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, time_avg_dfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, time_avg_dfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, time_avg_dfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, time_avg_dfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, time_avg_dfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, time_avg_dfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, time_avg_dfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Czas trwania procesu obliczeniowego")
# plt.title("DFS")
# plt.legend()
# plt.show()
