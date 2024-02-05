if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
        
    # make a list of all the possible coordinates that can be formed
    coordinates = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1)]
    
    # now make the final list by going through each of the elements in the coordinates
    answer = [coordinate for coordinate in coordinates if sum(coordinate) != n]
    
    print(answer)
