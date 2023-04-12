# FIFO Page Replacement Algorithm

from queue import Queue
def FIFO(n, ref_String, pageCapacity):
    pageFaults = 0
    pageHit = 0
    pageSet = set()  # it will denote the page frames
    pageQueue = Queue() # it will be used to follow the FIFO manner
    
    for i in range(0,n):
        # This if will work untill the pageSet gets full
        if(len(pageSet) < pageCapacity):
            if(ref_String[i] not in pageSet):
                pageSet.add(ref_String[i])   # New item added to pageSet
                pageQueue.put(ref_String[i]) # New item added to pageQueue
                pageFaults += 1 
            else:
                pageHit += 1
                        
        else:
            # This if will work after the pageSet gets full
            if(ref_String[i] not in pageSet):
                value = pageQueue.queue[0]  # Storing first queue element
                pageQueue.get()  # First element will get extracted
                pageSet.remove(value)  # That queue element will get removed from pageSet
                pageSet.add(ref_String[i])  # Upcoming page elememt will be added to pageSet
                pageQueue.put(ref_String[i])  # Upcoming page elememt will be added to pageQueue
                pageFaults += 1
            else:
                pageHit += 1
            
    #return pageFaults
    print("Page Fault = ",pageFaults)
    print("Page Hit = ",pageHit)  
                   

ref_String = [7,0,1,2,0,3,0,4,2,3,0,3,1,2,0]
n = len(ref_String)
frameSize = 3
    
FIFO(n, ref_String, frameSize)
