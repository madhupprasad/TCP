import math
dict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"C1":6,"C2":7,"C3":8,"C4":9}
visited = [False]*10
class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    def addEdge(self, v1, v2, val):
        self.adjMatrix[v1][v2] = val
        self.adjMatrix[v2][v1] = val

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    def __len__(self):
        return self.size
    def toString(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val),end = " "),
            print('\n')
    def find_path(self,src,dstn):
        visited[src] = True
        if src == dstn:
            return
def main():
    g = Graph(10)
    g.addEdge(dict["A"],dict["C1"],1);
    g.addEdge(dict["B"],dict["C2"],1);
    g.addEdge(dict["E"],dict["C3"],1);
    g.addEdge(dict["F"],dict["C4"],1);
    g.addEdge(dict["A"],dict["C"],150);
    g.addEdge(dict["A"],dict["D"],100);
    g.addEdge(dict["B"],dict["C"],150);
    g.addEdge(dict["D"],dict["C"],60);
    g.addEdge(dict["F"],dict["C"],70);
    g.addEdge(dict["D"],dict["E"],80);
    g.addEdge(dict["F"],dict["E"],80);

    routTable = [
            [['B','C',150],['C','C',150],['D','D',100],['E','C',150],['F','C',150]],
            [['A','C',150],['C','C',150],['D','C',150],['E','C',150],['F','C',150]],
            [['A','A',150],['B','B',150],['D','D',60],['E','F',70],['F','F',70]],
            [['A','A',100],['B','C',60],['C','C',60],['E','E',75],['F','E',75]],
            [['A','D',75],['B','F',80],['C','F',80],['D','D',75],['F','F',80]],
            [['A','C',70],['B','C',70],['C','C',70],['D','E',80],['E','E',80]]
            ]

    src = input("Enter source:")
    dstn = input("Enter destination:")
    size = int(input("Enter packet size:"))
    route_fragments = []
    i = 0
    for i in range(0,len(g.adjMatrix[dict[src]])):
        if g.adjMatrix[dict[src]][i] == 1:
            src_i = i
        if g.adjMatrix[dict[dstn]][i] == 1:
            dstn_i = i
    i = src_i
    while i != dstn_i:
        route_fragments.append(routTable[i][ dstn_i if dstn_i < i else dstn_i-1 ][2])
        print(routTable[i][ dstn_i if dstn_i < i else dstn_i-1 ][1])
        i = dict[routTable[i][ dstn_i if dstn_i < i else dstn_i-1 ][1]]
    min_frag = min(route_fragments) - 20
    min_frag = min_frag - (min_frag % 8)
    n = math.ceil(size/min_frag)
    print('minimum fragmentation  = ',min_frag)
    print('number of fragments = ',n)
    x = min_frag/8
    packets = [0] * n
    for i in range(n):
        packets[i] = [0] * 3

    for i in range(0,n):
        print('For Packet: ',i+1)
        packets[i][0] = min_frag + 20 if min_frag <= size else size + 20
        print('packet size = ',packets[i][0])
        packets[i][1] = 1 if i != n-1 else 0
        print('m bit = ',packets[i][1])
        packets[i][2] = 0 if i == 0 else packets[i-1][2] + x
        print('fragmentation offset = ',packets[i][2])
        size = size - min_frag
        print('remaining size = ',size)
        
    print("TotalSize\tmBit\tFragOff")
    for i in range(0,len(packets)):
        print('\n')
        for j in range(0,len(packets[i])):
            print(packets[i][j],end = '\t')
    
if __name__ == "__main__":
    main()
