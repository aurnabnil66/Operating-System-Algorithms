# Optimal Page Replacement Algorithm

import array as frameArray
def optimalPageReplecement(n, ref_String, frameSize):
    pageFaults = 0
    pageHit = 0
    pageFrame = frameArray.array("i", [-1] * frameSize)  # array("typecode", array or list)

    for i in range(0, n):
        emptyFrame = False
        for j in range(0, frameSize):
            if pageFrame[j] == -1:
               pageFrame[i] = ref_String[i]
               emptyFrame = True
               

ref_String = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
n = len(ref_String)
frameSize = 4

optimalPageReplecement(n, ref_String, frameSize)