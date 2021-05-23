import timeit
import multiprocessing

cy = timeit.timeit('''example_cython.test(5000)''',setup='import example_cython',number=1000)
py = timeit.timeit('''example_original.test(5000)''',setup='import example_original', number=1000)

print(f"Total CPU: {multiprocessing.cpu_count()}")

print(f"cython--> {cy}")
print(f"python--> {py}")
print('Cython is {}x faster'.format(py/cy))