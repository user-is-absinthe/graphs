import time

open('')
start = time.time()
for i in range(2 ** 32):
    # print('{} : {}\t---\t{}'.format(i, 2**32, bin(i)[2:].zfill(32)))
    pass
print('Elapsed time {}.'.format(time.time() - start))

# Elapsed time 181.92647790908813 without print().
