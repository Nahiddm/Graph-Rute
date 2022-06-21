'''
#MODUL5
#AHMAD NAHID MA'ALY
#1202200049
class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices_no=0

    def insertVertex(self,vertex):
        if vertex in self.graph:
            print("Vertex sudah ada di dalam graph")
        else:
            self.graph[vertex]=[] #list kosong digunakan untuk menampung tetangga dari vertex 1
            self.vertices_no+=1

    def insertEdge(self,vrt1,vrt2,jarak):
        if vrt1  in self.graph:
            self.graph[vrt1].append(vrt2)
        else:
            self.graph[vrt1]=[vrt2,jarak]
        if vrt2  in self.graph:
            self.graph[vrt2].append(vrt1)
        else:
            self.graph[vrt2]=[vrt1,jarak]

    

    def DFS(self,start):
        stack = [start]
        visited=set()
        while len(stack)>0:
            current = stack.pop()
            print(current)
            visited.add(current)
            for i in self.graph[current]:
                if i not in visited:
                    if i in stack:
                        stack.remove(i)
                    stack.append(i)


    def deleteVertex(self,vertex):
        if vertex not in self.graph:
            print("Vertex tidak ada di dalam graph")
        else:
            self.graph.pop(vertex)
            print("Vertex Berhasil Hapus", vertex)
    def getGraph(self):
        return self.graph
    def getEdges(self):
        edges = []
        for v in self.graph:
            for e  in self.graph[v]:
                if {e,v} not in edges:
                    edges.append({e,v})
        return edges
 
g = Graph()

while True:
    menu = int(input("""
    ((Menu Data Kota dan Lintasan))
    
    1. Input Kota
    2. Input Lintasan
    3. Cetak Rute Graph serta Lintasan
    0. EXIT.

    ((Terimakasih))

    Pilih :  """))
    if menu == 1:
        jumlah = int(input(" Jumlah Kota yang akan di input : "))
        for x in range(jumlah):
            kota = input("Kota: ")
        g.insertVertex(kota)      
    if menu == 2:
        Edgekota = input("lintasan/edge (kota 1, kota 2, jarak) : ")
        a = Edgekota.split(',')
        g.insertEdge(a[0],a[1],a[2])

    if menu == 3:
        print("Rute Graph",(g.getGraph()))
        print("Edges Graph",(g.getEdges()))
        
    if menu == 0:
        print("Terimakasih")
        exit()
        '''

class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices_no=0

    def tambahvertex(self,vertex):
        if vertex in self.graph:
            print("Vertex sudah ada di dalam graph")
        else:
            self.graph[vertex]=[] 
            self.vertices_no+=1

    def tambahedge(self,vrt1,vrt2,distance):
        if vrt1  in self.graph:
            self.graph[vrt1].append(vrt2)
        else:
            self.graph[vrt1]=[vrt2,distance]
        if vrt2  in self.graph:
            self.graph[vrt2].append(vrt1)
        else:
            self.graph[vrt2]=[vrt1,distance]
    

    
    def getEdges(self):
        edges = []
        for v in self.graph:
            for e  in self.graph[v]:
                if {e,v} not in edges:
                    edges.append({e,v})
        return edges

graph = Graph()

while True:
    menu = int(input("""
    ((Menu Data Kota dan Lintasan))
    
    1. Input Kota
    2. Input Lintasan
    3. Cetak Rute Graph serta Lintasan jarak
    4. cetak graph
    0. EXIT.

    ((Terimakasih))
    Pilih :  """))

    if menu == 1:
        jumlah = int(input("Jumlah kota : "))
        for x in range(jumlah):
            kota= input("kota : ")
        graph.tambahvertex(kota)

    if menu == 2:
        edgekota = input ("lintasan (kota1, kota2, jarak : ")
        a = edgekota.split(",")
        graph.tambahedge(a[0],a[1],a[2])

    if menu == 3:
        start = (input("kota awal    : "))
        end = (input("kota tujuan  : "))
        print(graph.plingdeket(start, end))
    
    if menu == 4:
        print("Edges Graph",(graph.getEdges()))