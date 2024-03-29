n = int(input())
cityAStrengths = list(map(int, input().split()))
m = int(input())
cityBStrengths = list(map(int, input().split()))

def calculatorFunction():
    changes = 0

    if cityAStrengths.sort() == cityBStrengths.sort():
        return(0)

    if sum(cityAStrengths) == sum(cityBStrengths):
        cityAStrengths.sort()
        cityBStrengths.sort()

        longerCity = max(len(cityAStrengths), len(cityBStrengths))
        shorterCity = min(len(cityAStrengths), len(cityBStrengths))

        for i in range(len(longerCity)):
            sumASoFar = 0
            sumBSoFar = 0

            for i in range(len(shorterCity)):
                sumASoFar += cityAStrengths[i]
                sumBSoFar += cityBStrengths[i]

                if sumASoFar != sumBSoFar:
                    biggerSumArray = cityAStrengths if sumASoFar > sumBSoFar else cityBStrengths
                    smallerSumArray = cityBStrengths if sumASoFar < sumBSoFar else cityAStrengths

                    biggerSum = max(sumASoFar, sumBSoFar)
                    smallerSum = min(sumASoFar, sumBSoFar)



                    for f in range(i, len(longerCity)+1):
                        # if sum of elements of smallerSumArray[i] to the next or the next +1 or the next +2 ... to the end of the array equal the biggerSumArray[i] print hello

                        if sum(smallerSumArray[i:f+1]) == biggerSumArray[i]:
                            
            

        difference = longerCity - shorterCity



    else:
        return(-1)