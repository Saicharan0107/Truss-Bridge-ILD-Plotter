import matplotlib.pyplot as plt
import math
import numpy as np
import os

def pratt_m(height, length, n):
    # Calculate the coordinates of the joints on the bottom chord
    bj = [(i * length, 0) for i in range(n + 1)]
    # Calculate the coordinates of the joints on the top chord
    tj = [((i + 1) * length, height) for i in range(n-1)]
    # Plot the joints as points
    for i, (x, y) in enumerate(bj + tj, 1):
        plt.plot(x, y, 'ro')
    # Plot the horizontal members as lines
    for i in range(n):
        plt.plot([bj[i][0], bj[i + 1][0]],[bj[i][1], bj[i + 1][1]],'b-')
        plt.text((bj[i][0] + bj[i + 1][0]) / 2, (bj[i][1] + bj[i + 1][1]) / 2, f"{i+1}", ha='center', va='center')
    for i in range(n-2):
        plt.plot([tj[i][0], tj[i + 1][0]], [tj[i][1], tj[i + 1][1]], 'b-')
        plt.text((tj[i][0] + tj[i + 1][0]) / 2, (tj[i][1] + tj[i + 1][1]) / 2, f"{i+n+1}", ha='center', va='center')
    # Plot the diagonal members as lines
    for i in range(n-1):
        plt.plot([tj[i][0], bj[i+1][0]], [tj[0][1], bj[i+1][1]], 'b-')
        plt.text((tj[i][0] + bj[i+ 1][0]) / 2, (tj[0][1] + bj[i + 1][1]) / 2, f"{i+2*n-1}", ha='center', va='center')
        if i == 0 or i == n-2:
            plt.plot([tj[i][0], bj[i][0]], [tj[i][1], bj[i][1]], 'b-')
            plt.text((tj[i][0] + bj[i][0]) / 2, (tj[i][1] + bj[i][1]) / 2, f"{i+3*n-2}", ha='center', va='center')
            plt.plot([tj[i][0], bj[i+2][0]], [tj[0][1], bj[i+2][1]], 'b-')
            plt.text((tj[i][0] + bj[i+2][0]) / 2, (tj[0][1] + bj[i+2][1]) / 2, f"{i+3*n-1}", ha='center', va='center')
        elif i < -1+n/2:
            plt.plot([tj[i][0], bj[i+2][0]], [tj[0][1], bj[i+2][1]], 'b-')
            plt.text((tj[i][0] + bj[i+2][0]) / 2, (tj[0][1] + bj[i+2][1]) / 2, f"{i+3*n-1}", ha='center', va='center')
        elif i > -1+n/2:
            plt.plot([tj[i][0], bj[i][0]], [tj[0][1], bj[i][1]], 'b-')
            plt.text((tj[i][0] + bj[i][0]) / 2, (tj[0][1] + bj[i][1]) / 2, f"{i+3*n-2}", ha='center', va='center')
    plt.xlabel('Horizontal Distance')
    plt.ylabel('Vertical Distance')
    plt.title('Pratt Truss Bridge')
    plt.axis('equal') 
    plt.grid(True)
    plt.show()

def pratt_j(height, length, n):
    bj = [(i * length, 0) for i in range(n + 1)]
    tj = [((i + 1) * length, height) for i in range(n-1)]
    for i, (x, y) in enumerate(bj + tj, 1):
        plt.plot(x, y, 'ro')
        plt.text(x, y, f"{i}")
    for i in range(n):
        plt.plot([bj[i][0], bj[i + 1][0]],[bj[i][1], bj[i + 1][1]],'b-')
    for i in range(n-2):
        plt.plot([tj[i][0], tj[i + 1][0]], [tj[i][1], tj[i + 1][1]], 'b-')
    for i in range(n-1):
        plt.plot([tj[i][0], bj[i+1][0]], [tj[0][1], bj[i+1][1]], 'b-')
        if i == 0 or i == n-2:
            plt.plot([tj[i][0], bj[i][0]], [tj[i][1], bj[i][1]], 'b-')
            plt.plot([tj[i][0], bj[i+2][0]], [tj[0][1], bj[i+2][1]], 'b-')
        elif i < -1+n/2:
            plt.plot([tj[i][0], bj[i+2][0]], [tj[0][1], bj[i+2][1]], 'b-')
        elif i > -1+n/2:
            plt.plot([tj[i][0], bj[i][0]], [tj[0][1], bj[i][1]], 'b-')
    plt.xlabel('Horizontal Distance')
    plt.ylabel('Vertical Distance')
    plt.title('Pratt Truss Bridge')
    plt.axis('equal') 
    plt.grid(True)
    plt.show()
    
def warren_m(height, length, n):
    # Calculate the coordinates of the joints on the bottom chord
    bj = [(i * length, 0) for i in range(n + 1)]
    # Calculate the coordinates of the joints on the top chord
    tj = [((2*i + 1) * length/2, height) for i in range(n)]
    # Plot the joints as points
    for i, (x, y) in enumerate(bj + tj, 1):
        plt.plot(x, y, 'ro')
    # Plot the horizontal members as lines
    for i in range(n):
        plt.plot([bj[i][0], bj[i + 1][0]],[bj[i][1], bj[i + 1][1]],'b-')
        plt.text((bj[i][0] + bj[i + 1][0]) / 2, (bj[i][1] + bj[i + 1][1]) / 2, f"{i+1}", ha='center', va='center')
    for i in range(n-1):
        plt.plot([tj[i][0], tj[i + 1][0]], [tj[i][1], tj[i + 1][1]], 'b-')
        plt.text((tj[i][0] + tj[i + 1][0]) / 2, (tj[i][1] + tj[i + 1][1]) / 2, f"{i+n+1}", ha='center', va='center')
    # Plot the diagonal members as lines
    for i in range(n):
            plt.plot([bj[i][0], tj[i][0]], [bj[i][1], tj[i][1]], 'b-')
            plt.text((bj[i][0] + tj[i][0]) / 2, (bj[i][1] + tj[i][1]) / 2, f"{i+2*n}", ha='center', va='center')
            plt.plot([bj[i+1][0], tj[i][0]], [bj[i+1][1], tj[i][1]], 'b-')
            plt.text((bj[i+1][0] + tj[i][0]) / 2, (bj[i+1][1] + tj[i][1]) / 2, f"{i+3*n}", ha='center', va='center')
    plt.xlabel('Horizontal Distance')
    plt.ylabel('Vertical Distance')
    plt.title('warren Truss Bridge')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def howe(height, length, n):
    # Calculate the coordinates of the joints on the bottom chord
    bj = [(i * length, 0) for i in range(n + 1)]
    # Calculate the coordinates of the joints on the top chord
    tj = [((i + 1) * length, height) for i in range(n-1)]
    # Plot the joints as points
    for i, (x, y) in enumerate(bj + tj, 1):
        plt.plot(x, y, 'ro')
    # Plot the horizontal members as lines
    for i in range(n):
        plt.plot([bj[i][0], bj[i + 1][0]],[bj[i][1], bj[i + 1][1]],'b-')
        plt.text((bj[i][0] + bj[i + 1][0]) / 2, (bj[i][1] + bj[i + 1][1]) / 2, f"{i+1}", ha='center', va='center')
    for i in range(n-2):
        plt.plot([tj[i][0], tj[i + 1][0]], [tj[i][1], tj[i + 1][1]], 'b-')
        plt.text((tj[i][0] + tj[i + 1][0]) / 2, (tj[i][1] + tj[i + 1][1]) / 2, f"{i+n+1}", ha='center', va='center')
    # Plot the diagonal members as lines
    for i in range(n-1):
        plt.plot([tj[i][0], bj[i+1][0]], [tj[0][1], bj[i+1][1]], 'b-')
        plt.text((tj[i][0] + bj[i+ 1][0]) / 2, (tj[0][1] + bj[i + 1][1]) / 2, f"{i+2*n-1}", ha='center', va='center')
    for i in range(n):
        if i<=-1+n/2:      
            plt.plot([tj[i][0], bj[i][0]], [tj[i][1], bj[i][1]], 'b-')
            plt.text((tj[i][0] + bj[i][0]) / 2, (tj[i][1] + bj[i + 1][1]) / 2, f"{i+3*n-2}", ha='center', va='center')
        elif i>=-1+n/2:
            plt.plot([tj[i-1][0], bj[i+1][0]], [tj[i-1][1], bj[i+1][1]], 'b-')
            plt.text((tj[i-1][0] + bj[i+1][0]) / 2, (tj[i-1][1] + bj[i + 1][1]) / 2, f"{i+3*n-2}", ha='center', va='center')
    plt.xlabel('Horizontal Distance')
    plt.ylabel('Vertical Distance')
    plt.title('Howe Truss Bridge')
    plt.axis('equal') 
    plt.grid(True)
    plt.show()

def get_user_choice(options):
    print('Select an option:')
    for i, option in enumerate(options):
        print('{}) {}'.format(i+1, option))
    while True:
        try:
            choice = int(input('Enter your choice (1-{}): '.format(len(options))))
            if choice < 1 or choice > len(options):
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please enter a number between 1 and {}.'.format(len(options)))
    return options[choice-1]