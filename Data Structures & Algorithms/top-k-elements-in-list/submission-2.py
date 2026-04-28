class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     
        d={}

        for i in nums:
            if i not in d:
                d[i]=1
                
            else:
                d[i]+=1

        pq=[]

        for key,f in d.items():
            heapq.heappush(pq,[f,key])

            if len(pq)>k:
                heapq.heappop(pq)       

        res=[]        

        temp=[0]*len(pq)
        index=len(pq)-1

        while pq:
            temp[index]=  heapq.heappop(pq)[1]
            index-=1

        for val in temp:
            res.append(val)

        return res              
            
              
             
             

        