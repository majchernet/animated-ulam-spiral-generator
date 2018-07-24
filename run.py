import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# side of numbers square
N = 201

# all numbers
PN = N ** 2

# numbers shift for animation
max_offset=1000

# prime number, sieve of Eratosthenes
# B is a list of prime number, if n is prime B[n] is set to 0 owerwise is set to 1
B = [0]*(PN+max_offset)

for x in range (2, int(np.sqrt(PN+max_offset))+1):
    if B[x] == 1:
        continue

    i = 2
    y = i*x

    while (y<PN+max_offset):
        B[y] = 1
        i += 1
        y = i*x
    print (x)

print ("The prime numbers have been calculated.")

i=0

fig = plt.figure(figsize=(10,10))
ax = plt.subplot(111)


# function to generate frame of animation
def update_frame(f):

    print (f)

    # start from number f
    start = f
    
    # numbers space to fill
    A = [[0 for x in range(N)] for x in range(N)]

    l = i = j = int (N/2)

    # red point in the middle 
    plt.scatter(i, j, 25, marker='s', hold=False, color='red')

    # start from the middle 
    if B[f]==0:
        A[i][j]=1
    f += 1
    
    # counter clockwise
    for n in range (1 , l+1):

        # move right
        for m in range (1, 2*n):
            j += 1
            if B[f]==0:
                A[i][j]=1
            f += 1

        # move up
        for m in range (1, 2*n):
            i -= 1
            if B[f]==0:
                A[i][j]=1
            f += 1

        # move left
        for m in range (1, 2*n+1):
            j -= 1
            if B[f]==0:
                A[i][j]=1
            f += 1

        # move down 
        for m in range (1, 2*n+1):
            i += 1
            if B[f]==0:
                A[i][j]=1
            f += 1
	# and back to move right

    # last line numbers line, move right
    for m in range (1, N):
        if B[f]==0:
            A[N-1][m] = 1
        f += 1


    X = []
    Y = []
    C = []


    # make lists of coordinates of points to plot
    y = N
    for row in A:
#        print (row)
        x=0
        for p in row:
            if p==1:
                X.append(x)
                Y.append(y)
                C.append('black')
            x+=1
        y -= 1

    X.append(l+1)
    Y.append(l+1)
    C.append('red')

    plt.scatter(X, Y, 16, marker='s', hold=False, color=C)
    plt.axis([1, N, 1, N])
    plt.xlabel('Ulam spiral, start number ' + str(start))





ani = animation.FuncAnimation(fig, update_frame, np.arange(1, max_offset), interval=50)
ani.save('ulam_spiral_' + str(N) + "x" + str(N) + "_form_1_to_" + str(max_offset) + ".mp4", fps=20, extra_args=['-vcodec', 'libx264'])

