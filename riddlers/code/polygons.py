import itertools

##This code tells you how many polygons can be drawn for
##a given set of points.  This code is actually entirely
##combinatorial: instead of checking to see if line
##segments intersect or anything like that, it just
##assumes that you have labeled the verticies of your
##graph and know which line segments intersect already.
##For the purposes of this code, a vertex is just a number,
##and an edge is just an implicitly unordered pair of numbers.

##These are some nice functions.  EdgeList takes in a list
##of verticies and produces the list of edges connecting
##each vertex to the next one on the list.  Contains takes
##two edges and a list of edges, and checks to see if the
##list of edges contains both of those edges.
##GeneratePolygons takes in an integer n and produces all
##n-gons on Kn.  Notice that GeneratePolygons will actually
##double count each polygon as it produces one polygon per
##orientation you can go around it.  It, however, always does
##start and end at vertex 1.  Purge takes two edges and a list
##of polygons,  and returns a list of all the polygons in the
##list that don't contain the two edges specified.

def EdgeList(verticies):
    output = []
    for i in range(len(verticies)-1):
        output.append([verticies[i], verticies[i+1]])
    return(output)

def Contains(edge1, edge2, edges):
    true1 = False
    true2 = False
    for edge in edges:
        if (edge[0] == edge1[0]) and (edge[1] == edge1[1]):
            true1 = True
        if (edge[1] == edge1[0]) and (edge[0] == edge1[1]):
            true1 = True
        if (edge[0] == edge2[0]) and (edge[1] == edge2[1]):
            true2 = True
        if (edge[1] == edge2[0]) and (edge[0] == edge2[1]):
            true2 = True
    return(true1 and true2)

def GeneratePolygons(n):
    output = []
    for l in list(itertools.permutations(range(2, n+1))):
        verticies = [1] + list(l) + [1]
        output.append(EdgeList(verticies))
    return(output)

def Purge(edge1, edge2, polygons):
    output = polygons.copy()
    for i in range(len(polygons)-1, -1, -1):
        if Contains(edge1, edge2, output[i]):
            del output[i]
    return(output)

##This is the main loop.  The three lists of edges
##correspond to the three embeddings of K7 constructed
##in the previous code.  In order to get the number of
##heptagons that you can draw on a specific K7, uncomment
##out the corresponding list of edges.

output = GeneratePolygons(8)

##l = [[[1, 3], [2, 5]],
##     [[1, 3], [2, 6]],
##     [[1, 4], [2, 5]],
##     [[1, 4], [2, 6]],
##     [[1, 4], [3, 5]],
##     [[1, 4], [3, 6]],
##     [[1, 6], [5, 7]],
##     [[1, 6], [5, 8]],
##     [[1, 7], [5, 8]],
##     [[1, 7], [6, 8]],
##     [[2, 4], [3, 7]],
##     [[2, 4], [3, 8]],
##     [[2, 6], [3, 5]],
##     [[2, 7], [3, 8]],
##     [[2, 6], [4, 5]],
##     [[2, 7], [4, 8]],
##     [[3, 6], [4, 5]],
##     [[3, 7], [4, 8]],
##     [[5, 7], [6, 8]]]

##l = [[[1, 3], [2, 4]],
##     [[1, 3], [2, 5]],
##     [[1, 3], [2, 6]],
##     [[1, 4], [2, 5]],
##     [[1, 4], [2, 6]],
##     [[1, 4], [3, 5]],
##     [[1, 6], [5, 7]],
##     [[1, 6], [5, 8]],
##     [[1, 7], [5, 8]],
##     [[1, 7], [6, 8]],
##     [[2, 4], [3, 5]],
##     [[2, 6], [3, 5]],
##     [[2, 7], [3, 8]],
##     [[2, 6], [4, 5]],
##     [[2, 7], [4, 8]],
##     [[3, 6], [4, 7]],
##     [[3, 6], [4, 8]],
##     [[3, 7], [4, 8]],
##     [[5, 7], [6, 8]]]

##l = [[[1, 3], [2, 4]],
##     [[1, 3], [2, 5]],
##     [[1, 4], [2, 5]],
##     [[1, 4], [3, 5]],
##     [[1, 6], [4, 7]],
##     [[1, 6], [5, 7]],
##     [[2, 4], [3, 5]],
##     [[2, 6], [3, 7]],
##     [[4, 7], [5, 6]]]

##l = [[[1, 3], [2, 4]],
##     [[1, 3], [2, 5]],
##     [[1, 4], [2, 5]],
##     [[1, 6], [4, 7]],
##     [[1, 6], [5, 7]],
##     [[2, 6], [3, 7]],
##     [[3, 5], [4, 6]],
##     [[3, 5], [4, 7]],
##     [[4, 7], [5, 6]]]

##l = [[[1, 3], [2, 4]],
##     [[1, 3], [2, 5]],
##     [[1, 5], [4, 6]],
##     [[1, 5], [4, 7]],
##     [[1, 6], [4, 7]],
##     [[2, 5], [3, 4]],
##     [[2, 6], [3, 7]],
##     [[2, 6], [5, 7]],
##     [[3, 6], [5, 7]]]

for i in range(len(l)):
    output = Purge(l[i][0], l[i][1], output)

print(len(output)//2)
