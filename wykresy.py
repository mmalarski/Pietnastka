import matplotlib.pyplot as plt
import numpy as np

# ORDER = "RDUL"
# ORDER = "RDLU"
# ORDER = "DRUL"
# ORDER = "DRLU"
# ORDER = "LUDR"
# ORDER = "LURD"
# ORDER = "ULDR"
# ORDER = "ULRD"

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

visited_count_rdul = [0, 0, 0, 0, 0, 0, 0]
visited_count_rdlu = [0, 0, 0, 0, 0, 0, 0]
visited_count_drul = [0, 0, 0, 0, 0, 0, 0]
visited_count_drlu = [0, 0, 0, 0, 0, 0, 0]
visited_count_ludr = [0, 0, 0, 0, 0, 0, 0]
visited_count_lurd = [0, 0, 0, 0, 0, 0, 0]
visited_count_uldr = [0, 0, 0, 0, 0, 0, 0]
visited_count_ulrd = [0, 0, 0, 0, 0, 0, 0]

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

for line in Lines:
    line.split(" ")

for line in Lines:
    index = int(line[0]) - 1
    if line[2] == "bfs":
        sol_len_bfs[index] += line[4]
        visited_count_bfs[index] += line[5]
        processed_count_bfs[index] += line[6]
        depth_avr_bfs[index] += line[7]
        time_avg_bfs[index] += line[8]
        if line[3] == "rdul":
        if line[3] == "rdlu":
        if line[3] == "drul":
        if line[3] == "drlu":
        if line[3] == "ludr":
        if line[3] == "lurd":
        if line[3] == "uldr":
        if line[3] == "ulrd":

    elif line[2] == "dfs":
        sol_len_dfs[index] += line[4]
        visited_count_dfs[index] += line[5]
        processed_count_dfs[index] += line[6]
         depth_avr_dfs[index] += line[7]
         time_avg_dfs[index] += line[8]
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


# 1
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, sol_len_bfs, 0.4, label = 'BFS')
# plt.bar(X_axis + 0.2, sol_len_dfs, 0.4, label = 'DFS')
# plt.bar(X_axis + 0.2, sol_len_astr, 0.4, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Długość znalezionego rozwiązania")
# plt.title("Ogółem")
# plt.legend()
# plt.show()

#2
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, visited_count_bfs, 0.4, label = 'BFS')
# plt.bar(X_axis + 0.2, visited_count_dfs, 0.4, label = 'DFS')
# plt.bar(X_axis + 0.2, visited_count_astr, 0.4, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów odwiedzonych")
# plt.title("Ogółem")
# plt.legend()
# plt.show()


#3
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, processed_count_bfs, 0.4, label = 'BFS')
# plt.bar(X_axis + 0.2, processed_count_dfs, 0.4, label = 'DFS')
# plt.bar(X_axis + 0.2, processed_count_astr , 0.4, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów przetworzonych")
# plt.title("Ogółem")
# plt.legend()
# plt.show()

#4
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, depth_avr_bfs, 0.4, label = 'BFS')
# plt.bar(X_axis + 0.2, depth_avr_dfs, 0.4, label = 'DFS')
# plt.bar(X_axis + 0.2, depth_avr_astr, 0.4, label = 'A*')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Maksymalna osiągnięta głębokość rekursji")
# plt.title("Ogółem")
# plt.legend()
# plt.show()

#5
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, time_avg_bfs , 0.4, label = 'BFS')
# plt.bar(X_axis + 0.2, time_avg_dfs, 0.4, label = 'DFS')
# plt.bar(X_axis + 0.2, time_avg_astr, 0.4, label = 'A*')
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

#7
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


#8
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

#9
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

#10
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
# plt.bar(X_axis - 0.2, sol_len_bfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, sol_len_bfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, sol_len_bfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, sol_len_bfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, sol_len_bfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, sol_len_bfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, sol_len_bfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, sol_len_bfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Długość znalezionego rozwiązania")
# plt.title("BFS")
# plt.legend()
# plt.show()

#12
# X = ['1', '2', '3', '4', '5', '6', '7']
# X_axis = np.arange(len(X))
# plt.bar(X_axis - 0.2, visited_count_bfs_rdul, 0.4, label = 'RDUL')
# plt.bar(X_axis + 0.2, visited_count_bfs_rdlu, 0.4, label = 'RDLU')
# plt.bar(X_axis - 0.2, visited_count_bfs_drul, 0.4, label = 'DRUL')
# plt.bar(X_axis + 0.2, visited_count_bfs_drlu, 0.4, label = 'DRLU')
# plt.bar(X_axis - 0.2, visited_count_bfs_ludr, 0.4, label = 'LUDR')
# plt.bar(X_axis + 0.2, visited_count_bfs_lurd, 0.4, label = 'LURD')
# plt.bar(X_axis - 0.2, visited_count_bfs_uldr, 0.4, label = 'ULDR')
# plt.bar(X_axis + 0.2, visited_count_bfs_ulrd, 0.4, label = 'ULRD')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Głebokość")
# plt.ylabel("Liczba stanów odwiedzonych")
# plt.title("BFS")
# plt.legend()
# plt.show()


#13
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

#14
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

#15
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

#17
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


#18
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

#19
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

#20
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