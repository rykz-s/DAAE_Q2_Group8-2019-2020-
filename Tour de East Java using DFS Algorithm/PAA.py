import random
import sys

GRAPH = {\
            'Pacitan': {'Blitar': 174, 'Madiun': 108},
            'Magetan': {'Madiun': 28},
            'Madiun': {'Magetan': 28, 'Pacitan': 108, 'Bojonegoro': 112},
            'Bojonegoro': {'Madiun': 112, 'Lamongan': 66},
            'Lamongan': {'Bojonegoro': 66, 'Surabaya': 46},
            'Surabaya': {'Lamongan': 46, 'Sidoarjo': 26, 'Bangkalan': 43},
            'Sidoarjo': {'Surabaya': 26, 'Jombang': 90, 'Malang': 71, 'Pasuruan': 47},
            'Jombang': {'Sidoarjo': 90, 'Kediri': 35},
            'Kediri': {'Jombang': 35, 'Blitar': 98},
            'Blitar': {'Pacitan': 174, 'Kediri': 98, 'Malang': 78},
            'Malang': {'Blitar': 78, 'Sidoarjo': 71},
            'Pasuruan': {'Sidoarjo': 47, 'Probolinggo': 47},
            'Probolinggo': {'Pasuruan': 47, 'Bondowoso': 97},
            'Bondowoso': {'Probolinggo': 97, 'Jember': 35, 'Banyuwangi': 97},
            'Jember': {'Bondowoso': 35},
            'Banyuwangi': {'Bondowoso': 97},
            'Sumenep': {'Bangkalan': 139},
            'Bangkalan': {'Sumenep': 139, 'Surabaya': 43}
        }

def dfs_paths(source, destination, path=None):
    
    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(GRAPH[source].keys()) - set(path):
        yield from dfs_paths(next_node, destination, path + [next_node])

def terdekat(source, destination):
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))
                

def main():
    print("Daftar Kota di Jawa Timur : ")
    p = open("listcity.txt", "r")
    print(p.read())
    print("\n")
    cities = open('randcity.txt').readlines()
    city = cities[0]
    words = city.split()
    source = random.choice(words)
    goal = random.choice(words)
    if source == goal:
        print("Generate random mengambil asal kota dan tujuan kota yang sama!")
        sys.exit(1)
    count = 0
    paths = dfs_paths(source, goal)
    cost, jalur_terdekat = terdekat(source, goal)
    for path in paths:
        count+=1
    print("Ada berapa cara dari " + source + " ke " + goal + " ?", end=' ')
    ans1 = int(input("\nJumlah cara = "))
    benar = 0
    if ans1 == count:
        print ('Selamat jawaban Anda benar!', end='\n')
        benar+=1
    else:
        print('Jawaban Anda salah!', end='\n')
        print("Jawaban yang benar adalah", count, "cara")
    print("\nJalur terdekat dari " + source + " ke " + goal + " ?", end ='\n') 
    d = " -> ".join(jalur_terdekat)
    ans2 = input('Jalur terdekat adalah = ')
    if ans2 == d:
        print ('Selamat jawaban Anda benar!', end='\n')
        benar+=1
    else:
        print('Jawaban Anda salah!', end='\n')
        print('Jawaban yang benar adalah ')
        print(' -> '.join(city for city in jalur_terdekat))
    print('\nBerapa jaraknya ?')
    ans3 = int(input("Jarak = "))
    if ans3 == cost:
        print ('\nSelamat Jawaban Anda benar!', end='\n')
        benar+=1
    else:
        print('\nJawaban Anda salah!', end='\n')
        print("\nJawaban yang benar adalah", cost, "km\n")
    if benar == 1 :    
        print("\nNilai anda adalah 50 ")
    elif benar == 2:
        print("\nNilai anda adalah 75 ")
    elif benar == 3:
        print("\nNilai anda adalah 100, Selamat anda benar semua!")
    elif benar == 0:
        print("\nDibaca mapnya lagi yaaa")
    print("\nJadi, dari quiz game di atas dapat disimpulkan bahwa kemungkinan jalur yang dapat dilalui adalah :")
    paths = dfs_paths(source, goal)
    hitung = 0
    for path in paths:
        print("\n")
        hitung+=1
        print(hitung, ".")
        print(' -> '.join(city for city in path))
    print("\n")
    print("Jumlah jalur yang bisa ditempuh adalah:", count, "jalur")
    print("Jalur yang terdekat adalah:",( ' -> '.join(city for city in jalur_terdekat)))
    print("Dengan jarak",cost, "km\n")
    
if __name__ == '__main__':
    main()
