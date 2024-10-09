# def solution(recording):
#     key_changes = 0
#     for i in range(1, len(recording)):
#         if recording[i].lower() != recording[i - 1].lower():
#             key_changes += 1
#
#     return key_changes
#
# print(solution(['W','w','a','a','W']))
import bisect

def solution(objects, radius):
    max_count = 0
    best_coordinate = None
    n = len(objects)
    sorted_objects = sorted(objects)

    for obj in sorted_objects:
        for c in [obj - radius, obj, obj + radius]:
            start = c - radius
            end = c + radius

            left = bisect.bisect_left(sorted_objects, start)
            right = bisect.bisect_right(sorted_objects, end)

            count = right - left

            if count > max_count:
                max_count = count
                best_coordinate = c
            elif count == max_count:
                best_coordinate = min(best_coordinate, c)
    return best_coordinate


# print(solution([-48,-43,-24,-19,-17,0,9,11,20,36], 11))
# print(solution([-63,-45,-42,-37,-35,-32,-16,2,3,10,14,32,40,53,70], 18))
print(solution([-2,4,5,6,7],1))