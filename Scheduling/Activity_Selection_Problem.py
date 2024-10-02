# We have a set of n proposed activities S = {a1,a2,a3,a4,...an} with start and finish times for a
# certain lecture hall. Find the largest set of activities that can be held in the lecture hall that
# respects the start - finish times.

def activity_selection(start, finish):
    # Greedy strategy.
    # Schedule the activity which terminates first. Sort by termination times.
    #For the next event take the activity that starts after the end of the previous event
    #and terminates as early as possible
    activities = []
    for i in range(len(start)):
        activities.append([start[i],finish[i]])

    activities.sort(key=lambda x: x[1])
    print(activities)
    result = [activities[0]]
    for i in range(1,len(activities)):
        if result[-1][1] <= activities[i][0]:
            # finish time of last activity in result should be <= start time of
            # the next activity that we want to select
            result.append(activities[i])

    print(result)



start = [1,4,3,6,3,9,5,7,4]
finish = [3,9,5,10,6,10,7,8,11]
activity_selection(start, finish)