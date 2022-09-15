import sys,random
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    double *compute_distances(int numpts, struct point *points);
""")

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == '__main__':

    seed = int(sys.argv[1])
    num = int(sys.argv[2])

    random.seed(seed)

    points = [Point(random.random(),random.random(),random.random())
                for _ in range(num)]

    lib = ffi.dlopen("./libp5.so")

    x = ffi.new("Point *")
    dists = lib.compute_distances(num,points)

    mindist = 2.0
    for dist in dists:
        if dist < mindist:
            mindist = dist
    
    print(f"MINDIST {mindist:.12f}")