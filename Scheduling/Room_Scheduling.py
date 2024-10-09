#We are given start and finish times of each activity and we have to schedule all the activities.
#Schedule all the activities but use minimum number of rooms.
#

#Intuition:
# Schedule an activity in a room already used in scheduling whenever possible. Only when next activity request
# conflicts with activities in all rooms in use, increase the number of rooms by one.
# Consider the requests in the order of their start time.

# User function Template for python3

class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        # code here
        # lst = []
        # for i in range(len(arr)):
        #     lst.append((arr[i],dep[i]))

        # lst.sort(key=lambda x: x[0])
        # # print(lst)
        # m=1
        # rooms = [-1 for k in range(len(arr))]
        # rooms[0] = lst[0][1]
        # j=0
        # for i in range(1, len(lst)):
        #     while j <= m and rooms[j] > lst[i][0]:
        #         j+=1

        #     if j >= 0 and j<=m:
        #         rooms[j] = lst[i][1]
        #     else:
        #         m+=1
        #         rooms.append(lst[i][1])

        # return m

        l = 0
        e = 0
        arr.sort()
        dep.sort()
        count = 0
        maximum = 0
        while l < len(arr):
            if arr[l] <= dep[e]:
                count += 1
                l += 1
            else:
                e += 1
                count -= 1
            maximum = max(maximum, count)

        return maximum

