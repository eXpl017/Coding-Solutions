def jobscheduling(arr):
       arr.sort(key = lambda x : x[1])
       print(arr)
       dl = 1
       max_ = -1
       maxprofit = []
       maxprofit.append(arr[0][1])
       for i in range(1, len(arr)):
              if arr[i][1] == arr[i-1][1]:
                     if arr[i][2] > maxprofit[-1]:
                            maxprofit[-1] = arr[i][2]
                            print(maxprofit,end='\n')
              else:
                     maxprofit.append(arr[i][2])
                     print(maxprofit,end='\n')    

arr = [[1,2,100],[2,1,19],[3,2,27],[4,1,25],[5,1,15]]
print("max profit: ")
jobscheduling(arr)