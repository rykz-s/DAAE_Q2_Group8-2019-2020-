import random
import sys

GRAPH = {\
            'Pacitan': {'Ponorogo': 79, 'Trenggalek': 105},
            'Ponorogo': {'Pacitan': 79, 'Trenggalek': 44, 'Magetan': 36, 'Kab_Madiun': 30, 'Tulungagung': 80},
            'Trenggalek': {'Pacitan': 105, 'Ponorogo': 44, 'Tulungagung': 36},
            'Tulungagung': {'Ponorogo': 80, 'Trenggalek': 36, 'Kediri': 54, 'Blitar': 29, 'Kab_Blitar': 30},
            'Magetan': {'Ponorogo': 36, 'Madiun': 26, 'Ngawi': 36},
            'Madiun': {'Magetan': 26, 'Kab_Madiun': 1, 'Ngawi': 37},
            'Kab_Madiun': {'Madiun': 1, 'Ponorogo': 30, 'Kediri': 115, 'Nganjuk': 60},
            'Ngawi': {'Magetan': 36, 'Madiun': 37, 'Bojonegoro': 75},
            'Tuban': {'Bojonegoro': 42, 'Lamongan': 59},
            'Lamongan': {'Tuban': 59, 'Bojonegoro': 66, 'Jombang': 70, 'Gresik': 30},
            'Gresik': {'Lamongan': 30, 'Mojokerto': 57, 'Surabaya': 21},
            'Bojonegoro': {'Ngawi': 75, 'Nganjuk': 65, 'Tuban': 42, 'Lamongan': 66},
            'Nganjuk': {'Bojonegoro': 65, 'Kab_Madiun': 60, 'Kediri': 66, 'Jombang': 52},
            'Kediri': {'Tulungagung': 54, 'Kab_Madiun': 115, 'Kab_Kediri': 27, 'Nganjuk': 66},
            'Kab_Kediri': {'Kediri': 27, 'Jombang': 53, 'Batu': 68},
            'Jombang': {'Nganjuk': 52, 'Kab_Kediri': 53, 'Lamongan': 70, 'Mojokerto': 30, 'Batu': 73},
            'Mojokerto': {'Kab_Mojokerto': 1, 'Jombang': 30, 'Gresik': 57, 'Sidoarjo': 52},
            'Kab_Mojokerto': {'Mojokerto': 1, 'Batu': 46},
            'Sidoarjo': {'Malang': 71, 'Mojokerto': 52, 'Surabaya': 29, 'Pasuruan': 47},
            'Surabaya': {'Sidoarjo': 29, 'Gresik': 21, 'Bangkalan': 32},
            'Blitar': {'Kab_Blitar': 8, 'Tulungagung': 29, 'Batu': 73, 'Malang': 76},
            'Kab_Blitar': {'Tulungagung': 30, 'Blitar': 8, 'Kab_Malang': 73},
            'Malang': {'Kab_Malang': 23, 'Blitar': 76, 'Batu': 17, 'Sidoarjo': 71},
            'Kab_Malang': {'Kab_Blitar': 73, 'Malang': 23, 'Lumajang': 95},
            'Pasuruan': {'Sidoarjo': 47, 'Kab_Pasuruan': 5, 'Probolinggo': 46},
            'Kab_Pasuruan': {'Pasuruan': 5, 'Lumajang': 87},
            'Lumajang': {'Kab_Malang': 95, 'Kab_Pasuruan': 87, 'Probolinggo': 44, 'Jember': 66},
            'Probolinggo': {'Pasuruan': 46, 'Lumajang': 44, 'Kab_Probolinggo': 47},
            'Kab_Probolinggo': {'Probolinggo': 47, 'Jember': 107, 'Bondowoso': 34},
            'Jember': {'Lumajang': 66, 'Kab_Probolinggo': 107, 'Bondowoso': 34, 'Banyuwangi': 103},
            'Bondowoso': {'Jember': 34, 'Kab_Probolinggo': 34, 'Situbondo': 34},    
            'Situbondo': {'Bondowoso': 34, 'Banyuwangi': 95},
            'Banyuwangi': {'Jember': 103, 'Situbondo': 95},
            'Bangkalan': {'Surabaya': 32, 'Sampang': 64},
            'Sampang': {'Bangkalan': 64, 'Pamekasan': 34},
            'Pamekasan': {'Sampang': 34, 'Sumenep': 55},
            'Batu': {'Malang': 17, 'Blitar': 73, 'Kab_Kediri': 68, 'Jombang': 73, 'Kab_Mojokerto': 46},
            'Sumenep': {'Pamekasan': 55}
        }

def dfs_paths(source, destination, path=None):
    """All possible paths from source to destination using depth-first search
    source: Nama kota Asal
    destination: Nama kota Tujuan
    path: Jalur yang dilalui saat ini (Default value = None)
    yields: Semua jalur yang mungkin dari asal ke tujuan
    """
    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(GRAPH[source].keys()) - set(path):
        yield from dfs_paths(next_node, destination, path + [next_node])

def terdekat(source, destination):
    """Cheapest path from source to destination using uniform cost search
    :param source: Source city name
    :param destination: Destination city name
    :returns: Cost and path for cheapest traversal
    """
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
    print("List of city in East Java : ")
    p = open("listcity.txt", "r")
    print(p.read())
    print("\n")
    cities = open('randcity.txt').readlines()
    city = cities[0]
    words = city.split()
    source = random.choice(words)
    goal = random.choice(words)
    if source == goal:
        print("Salah, coba lagi!")
        sys.exit(1)
    print(source)
    print(" ")
    print(goal)
    count = 0
    paths = dfs_paths(source, goal)
    for path in paths:
        print(" ")
        print(' -> '.join(city for city in path))
        print ("\nJumlah kota yang dilewati adalah sebanyak", len(path) , "kota")
        count+=1
        #jjalur = '6'
        #paths = dfs_paths(source, goal)
        #cost, jalur_terdekat = terdekat(source, goal)
        #print('Ada Berapa cara dari arad ke Sibiu?', end=' ')
        #jwb1 = input().strip()
        #if jwb1 == jjalur:
         #   print('Selamat Anda benar', end='\n')
        #else:
         #   print('Selamat Anda salah', end='\n')
        #print('Jalur terdekat dari Arad ke Sibiu?', end=' ')
        #jwb = input().strip()
        #if jwb == fruits:
         #   print('Selamat Anda benar', end='\n')
        #else:
         #   print('Selamat Anda salah', end='\n')
    #print('\nSemua kemungkinan jalur yang bisa dilalui:')   
    paths = dfs_paths(source, goal)
    cost, jalur_terdekat = terdekat(source, goal)
    print("Ada berapa cara dari " + source + " ke " + goal + " ?", end=' ')
    ans1 = input().strip()
    if ans1 == count:
        print ('Selamat anda benar!', end='\n')
    else:
        print('Anda salah!', end='\n')
        print("Jawaban yang benar adalah", count, "cara")
    print("Jalur terdekat dari " + source + " ke " + goal + " ?", end =' ') 
    print(" ")
    print("Terdapat", count, "cara")
    print('\nJalur Terdekat:')
    cost, jalur_terdekat = terdekat(source, goal)
    print(' -> '.join(city for city in jalur_terdekat))
    print('Cost Jalur =', cost, "km\n")

if __name__ == '__main__':
    main()