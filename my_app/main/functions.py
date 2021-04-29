import pandas as pd

def ConvertNavigationVariables(mean, start, end):
    data = pd.ExcelFile('../data/Tube_and_Bus_Route_Stops.xls')
    sheet = 'Bus Regions'
    mean_map = 'bus_map'
    if 'Tube' in mean:
        sheet = 'Tube Regions'
        mean_map = 'tube_map'
    df = pd.read_excel(data, sheet_name=sheet, skiprows=1)

    if start is None:
        start = ''
    if end is None:
        end = ''

    # Create dataframe from dataset
    df = df[{'Name', 'Number'}].set_index('Name')
    start_number = df.loc[start, 'Number']
    end_number = df.loc[end, 'Number']

    return mean_map, start_number, end_number


#                Figure out how to convert map into matrix form       (X)
#                Need to find way to isolate the start, end vertices  (X)
#                link group number to station name                    ( )
#                Block paths to find alternate routes (min 3)         ( )
#                    locate
#                Record in sql table                                  ( )
#                Link with entry/exit data to produce score           ( )
#                Put in table to ROUTES page, which links to analysis ( )

class Graph:
    def __init__(self):
        self.pathlist = []

    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        if parent[j] == -1:
            print(j)
            return
        self.printPath(parent, parent[j])
        print(j)
        self.pathlist.append(j)

    def printSolution(self, dist, parent, src, end):

        print("Vertex \t\tDistance from Source\tPath")
        # for i in range(1, len(dist)):
        #     print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
        #     self.printPath(parent, i)
        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, end, dist[end])),
        self.printPath(parent, end)

    def dijkstra(self, graph, src, end):
        self.pathlist.append(src)
        row = len(graph)
        col = len(graph[0])

        dist = [float("Inf")] * row

        parent = [-1] * row

        dist[src] = 0

        queue = []
        for i in range(row):
            queue.append(i)

        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)

            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        self.printSolution(dist, parent, src, end)


data = pd.read_excel('../data/multi-year-station-entry-and-exit-figures.xls',
                     sheet_name='2017 Entry & Exit (Zone 1)', skiprows=6)

df = pd.DataFrame(data)
df1 = pd.DataFrame(index=range(23), columns=['total']).fillna(0)
df2 = df['Group Alphabet'].drop_duplicates().dropna().reset_index()

for x, poo in df1.iterrows():
    for y, lines in df.iterrows():
        if x == lines['Group Number']:
            poo['total'] += lines['million']

df3 = pd.concat([df1, df2['Group Alphabet']], axis=1, join='inner')

# entry/exit for each station

A = df3.iloc[0]['total']
B = df3.iloc[1]['total']
C = df3.iloc[2]['total']
D = df3.iloc[3]['total']
E = df3.iloc[4]['total']
F = df3.iloc[5]['total']
G = df3.iloc[6]['total']
H = df3.iloc[7]['total']
I = df3.iloc[8]['total']
J = df3.iloc[9]['total']
K = df3.iloc[10]['total']
L = df3.iloc[11]['total']
M = df3.iloc[12]['total']
N = df3.iloc[13]['total']
O = df3.iloc[14]['total']
P = df3.iloc[15]['total']
Q = df3.iloc[16]['total']
R = df3.iloc[17]['total']
S = df3.iloc[18]['total']
T = df3.iloc[19]['total']
U = df3.iloc[20]['total']
V = df3.iloc[21]['total']
W = df3.iloc[22]['total']

g = Graph()

#            0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
#            A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W
tube_map = [[0, A, A, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A 0
            [B, 0, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B 1
            [C, C, 0, C, 0, C, C, C, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, 0, 0, 0, 0],  # C 2
            [D, 0, D, 0, D, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D 3
            [0, 0, 0, E, 0, E, 0, 0, E, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, E],  # E 4
            [0, 0, F, F, F, 0, F, 0, F, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F 5
            [0, 0, G, 0, 0, G, 0, G, G, 0, G, 0, 0, 0, 0, 0, 0, 0, G, 0, 0, 0, 0],  # G 6
            [0, 0, H, 0, 0, 0, H, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, H, H, 0, 0, 0, 0],  # H 7
            [0, 0, 0, 0, I, I, I, 0, 0, I, I, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I 8
            [0, 0, 0, 0, J, 0, 0, 0, J, 0, J, J, 0, J, 0, 0, 0, 0, 0, 0, 0, 0, J],  # J 9
            [0, 0, 0, 0, 0, 0, K, K, K, K, 0, 0, 0, K, K, 0, 0, K, 0, 0, 0, 0, 0],  # K 10
            [0, 0, 0, 0, 0, 0, 0, 0, 0, L, 0, 0, L, L, 0, 0, 0, 0, 0, 0, L, L, L],  # L 11
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, M, 0, M, 0, 0, 0, 0, 0, M, M, 0, 0],  # M 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, N, N, N, N, 0, N, 0, 0, 0, 0, N, 0, 0, 0],  # N 13
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, O, 0, 0, O, 0, O, O, O, 0, O, 0, 0, 0],  # O 14
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, P, 0, P, 0, 0, P, 0, 0, 0],  # P 15
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Q, Q, 0, Q, 0, 0, 0, 0, 0],  # Q 16
            [0, 0, 0, 0, 0, 0, 0, R, 0, 0, R, 0, 0, 0, R, 0, R, 0, R, 0, 0, 0, 0],  # R 17
            [0, 0, S, 0, 0, 0, 0, S, 0, 0, 0, 0, 0, 0, 0, 0, 0, S, 0, 0, 0, 0, 0],  # S 18
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, T, T, T, T, 0, 0, 0, 0, 0, 0, 0],  # T 19
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, U, U, 0, 0, 0, 0, 0, 0, 0, 0, U, 0],  # U 20
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, V, 0, 0, 0, 0, 0, 0, 0, 0, V, 0, V],  # V 21
            [0, 0, 0, 0, W, 0, 0, 0, 0, W, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0]]  # W 22

#           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
#           A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
bus_map = [[0, A, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A 0
           [B, 0, 0, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B 1
           [C, 0, 0, C, 0, 0, C, 0, C, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C 2
           [0, D, D, 0, D, 0, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D 3
           [0, 0, 0, E, 0, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E 4
           [0, 0, 0, 0, F, 0, F, F, 0, 0, 0, 0, 0, 0, 0, 0, 0, F],  # F 5
           [0, 0, G, G, 0, G, 0, G, G, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G 6
           [0, 0, 0, 0, 0, H, H, 0, H, H, H, 0, 0, H, 0, 0, H, 0],  # H 7
           [0, 0, I, 0, 0, 0, I, I, 0, I, 0, 0, 0, 0, 0, 0, 0, 0],  # I 8
           [0, 0, 0, 0, 0, 0, 0, J, J, 0, J, J, 0, 0, 0, 0, 0, 0],  # J 9
           [0, 0, 0, 0, 0, 0, 0, K, 0, K, 0, K, 0, K, 0, 0, 0, 0],  # K 10
           [0, 0, 0, 0, 0, 0, 0, 0, 0, L, L, 0, L, L, 0, 0, 0, 0],  # L 11
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, M, 0, M, M, 0, 0, 0],  # M 12
           [0, 0, 0, 0, 0, 0, 0, N, 0, 0, N, N, N, 0, N, N, N, 0],  # N 13
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, O, O, 0, O, 0, 0],  # O 14
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, P, P, 0, P, P],  # P 15
           [0, 0, 0, 0, 0, 0, 0, Q, 0, 0, 0, 0, 0, Q, 0, Q, 0, Q],  # Q 16
           [0, 0, 0, 0, 0, R, 0, 0, 0, 0, 0, 0, 0, 0, 0, R, R, 0]]  # R 17

# g.dijkstra(tube_map, 10, 3)
# print(g.pathlist)

def FindPath(mean, start, end):
    mean_map, start_number, end_number = ConvertNavigationVariables(mean, start, end)

    data = pd.read_excel('../data/multi-year-station-entry-and-exit-figures.xls',
                         sheet_name='2017 Entry & Exit (Zone 1)', skiprows=6)

    df = pd.DataFrame(data)
    df1 = pd.DataFrame(index=range(23), columns=['total']).fillna(0)
    df2 = df['Group Alphabet'].drop_duplicates().dropna().reset_index()

    for x, poo in df1.iterrows():
        for y, lines in df.iterrows():
            if x == lines['Group Number']:
                poo['total'] += lines['million']

    df3 = pd.concat([df1, df2['Group Alphabet']], axis=1, join='inner')

    # entry/exit for each station

    A = df3.iloc[0]['total']
    B = df3.iloc[1]['total']
    C = df3.iloc[2]['total']
    D = df3.iloc[3]['total']
    E = df3.iloc[4]['total']
    F = df3.iloc[5]['total']
    G = df3.iloc[6]['total']
    H = df3.iloc[7]['total']
    I = df3.iloc[8]['total']
    J = df3.iloc[9]['total']
    K = df3.iloc[10]['total']
    L = df3.iloc[11]['total']
    M = df3.iloc[12]['total']
    N = df3.iloc[13]['total']
    O = df3.iloc[14]['total']
    P = df3.iloc[15]['total']
    Q = df3.iloc[16]['total']
    R = df3.iloc[17]['total']
    S = df3.iloc[18]['total']
    T = df3.iloc[19]['total']
    U = df3.iloc[20]['total']
    V = df3.iloc[21]['total']
    W = df3.iloc[22]['total']

    g = Graph()

    #            0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
    #            A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W
    tube_map = [[0, A, A, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A 0
                [B, 0, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B 1
                [C, C, 0, C, 0, C, C, C, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, 0, 0, 0, 0],  # C 2
                [D, 0, D, 0, D, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D 3
                [0, 0, 0, E, 0, E, 0, 0, E, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, E],  # E 4
                [0, 0, F, F, F, 0, F, 0, F, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F 5
                [0, 0, G, 0, 0, G, 0, G, G, 0, G, 0, 0, 0, 0, 0, 0, 0, G, 0, 0, 0, 0],  # G 6
                [0, 0, H, 0, 0, 0, H, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, H, H, 0, 0, 0, 0],  # H 7
                [0, 0, 0, 0, I, I, I, 0, 0, I, I, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I 8
                [0, 0, 0, 0, J, 0, 0, 0, J, 0, J, J, 0, J, 0, 0, 0, 0, 0, 0, 0, 0, J],  # J 9
                [0, 0, 0, 0, 0, 0, K, K, K, K, 0, 0, 0, K, K, 0, 0, K, 0, 0, 0, 0, 0],  # K 10
                [0, 0, 0, 0, 0, 0, 0, 0, 0, L, 0, 0, L, L, 0, 0, 0, 0, 0, 0, L, L, L],  # L 11
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, M, 0, M, 0, 0, 0, 0, 0, M, M, 0, 0],  # M 12
                [0, 0, 0, 0, 0, 0, 0, 0, 0, N, N, N, N, 0, N, 0, 0, 0, 0, N, 0, 0, 0],  # N 13
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, O, 0, 0, O, 0, O, O, O, 0, O, 0, 0, 0],  # O 14
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, P, 0, P, 0, 0, P, 0, 0, 0],  # P 15
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Q, Q, 0, Q, 0, 0, 0, 0, 0],  # Q 16
                [0, 0, 0, 0, 0, 0, 0, R, 0, 0, R, 0, 0, 0, R, 0, R, 0, R, 0, 0, 0, 0],  # R 17
                [0, 0, S, 0, 0, 0, 0, S, 0, 0, 0, 0, 0, 0, 0, 0, 0, S, 0, 0, 0, 0, 0],  # S 18
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, T, T, T, T, 0, 0, 0, 0, 0, 0, 0],  # T 19
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, U, U, 0, 0, 0, 0, 0, 0, 0, 0, U, 0],  # U 20
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, V, 0, 0, 0, 0, 0, 0, 0, 0, V, 0, V],  # V 21
                [0, 0, 0, 0, W, 0, 0, 0, 0, W, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0]]  # W 22

    #           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
    #           A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
    bus_map = [[0, A, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A 0
               [B, 0, 0, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B 1
               [C, 0, 0, C, 0, 0, C, 0, C, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C 2
               [0, D, D, 0, D, 0, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D 3
               [0, 0, 0, E, 0, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E 4
               [0, 0, 0, 0, F, 0, F, F, 0, 0, 0, 0, 0, 0, 0, 0, 0, F],  # F 5
               [0, 0, G, G, 0, G, 0, G, G, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G 6
               [0, 0, 0, 0, 0, H, H, 0, H, H, H, 0, 0, H, 0, 0, H, 0],  # H 7
               [0, 0, I, 0, 0, 0, I, I, 0, I, 0, 0, 0, 0, 0, 0, 0, 0],  # I 8
               [0, 0, 0, 0, 0, 0, 0, J, J, 0, J, J, 0, 0, 0, 0, 0, 0],  # J 9
               [0, 0, 0, 0, 0, 0, 0, K, 0, K, 0, K, 0, K, 0, 0, 0, 0],  # K 10
               [0, 0, 0, 0, 0, 0, 0, 0, 0, L, L, 0, L, L, 0, 0, 0, 0],  # L 11
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, M, 0, M, M, 0, 0, 0],  # M 12
               [0, 0, 0, 0, 0, 0, 0, N, 0, 0, N, N, N, 0, N, N, N, 0],  # N 13
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, O, O, 0, O, 0, 0],  # O 14
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, P, P, 0, P, P],  # P 15
               [0, 0, 0, 0, 0, 0, 0, Q, 0, 0, 0, 0, 0, Q, 0, Q, 0, Q],  # Q 16
               [0, 0, 0, 0, 0, R, 0, 0, 0, 0, 0, 0, 0, 0, 0, R, R, 0]]  # R 17

    mean_map = bus_map
    if 'Tube' in mean:
        mean_map = tube_map

    print(mean_map, start_number, end_number)
    g.dijkstra(mean_map, start_number, end_number)
    path = g.pathlist
    return path



