# Implementasi algoritma Brute Force dengan metode Depth First Search

def DFSBruteForce(pola, awal, tujuan):
    # Inisialisasi stack untuk DFS
    stack = [(awal, [awal])]
    
    # Loop hingga stack kosong
    while stack:
        (node, path) = stack.pop()   # ambil node dan path terakhir
        for next_node in pola[node]:
            if next_node == tujuan:
                # jika node tujuan ditemukan, tambahkan ke path dan kembalikan
                return path + [next_node]
            else:
                # tambahkan node yang belum dikunjungi ke stack
                if next_node not in path:
                    stack.append((next_node, path + [next_node]))
    
    # jika tidak ditemukan path, return None
    return None


# Contoh penggunaan
pola = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

awal = 'A'
tujuan = 'F'

path = DFSBruteForce(pola, awal, tujuan)

if path:
    print(f"Pola tersingkat dari {awal} ke {tujuan} adalah {path}")
else:
    print(f"Tidak ditemukan path dari {awal} ke {tujuan}")
