# FIFO Page Replacement Algorithm

#from queue import pageQueue
def FIFO(n, ref_string, pageCapacity):
    pageFaults = 0
    pageSet = set()
    
    for i in range(0,n):
        if(len(pageSet) < pageCapacity):
            if(ref_String[i] not in pageSet):
                pageSet.add(ref_String[i])
                pageFaults += 1         
        else:
           if(ref_String[i] not in pageSet): 


n = input("Enter number of page elements : ")
ref_String = [n]
pageCapacity = 3
FIFO(n, ref_String, pageCapacity)
