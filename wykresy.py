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

bfs_rdul = []
bfs_rdlu = []
bfs_drul = []
bfs_drlu = []
bfs_ludr = []
bfs_lurd = []
bfs_uldr = []
bfs_ulrd = []

dfs_rdul = []
dfs_rdlu = []
dfs_drul = []
dfs_drlu = []
dfs_ludr = []
dfs_lurd = []
dfs_uldr = []
dfs_ulrd = []

astr_manh =[]
astr_hamm = []



file = open("message.txt", "r")
file.close()