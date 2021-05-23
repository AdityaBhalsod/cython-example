cpdef test(int x):          # for cp is both cython and python usable.
    cdef int y = 0          # for c is only cython usable.
    cdef int i              # for c is only cython usable.
    for i in range(x):
        y += i
    return y