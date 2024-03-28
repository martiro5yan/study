import time

for i in [0.7, 0.5, 1.0, 2.5, 3.3]:
    print(f'Waiting for {i} seconds')
    time.sleep(i)
print('The end')


