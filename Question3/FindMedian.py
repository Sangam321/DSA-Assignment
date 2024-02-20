import heapq
class ScoreTracker:
    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
    def addScore(self,score):
        heapq.heappush(self.maxHeap,-1*score)
        if(self.maxHeap and self.minHeap and -1*self.maxHeap[0]>self.minHeap[0]):
            value=-1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,value)
        if len(self.minHeap)>len(self.maxHeap)+1:
            value=heapq.heappop(self.minHeap)
            heapq.heappush(-1*self.maxHeap,value)
        if len(self.maxHeap)>len(self.minHeap)+1:
            value=-1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,value)
    def getMedianScore(self):
        if len(self.minHeap)>len(self.maxHeap):
            return (self.minHeap[0])
        if len(self.maxHeap)>len(self.minHeap):
            return (-1*self.maxHeap[0])
        return (self.minHeap[0]+(-1*self.maxHeap[0]))/2
scoreTracker = ScoreTracker()
scoreTracker.addScore(85.5)
scoreTracker.addScore(92.3)
scoreTracker.addScore(77.8)
scoreTracker.addScore(90.1)
median1 = scoreTracker.getMedianScore()
print(f"Median 1: {median1}")
scoreTracker.addScore(81.2)
scoreTracker.addScore(88.7)
median2 = scoreTracker.getMedianScore()
print(f"Median 2: {median2}")