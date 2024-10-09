# def solution(panel, codes):
#     results = []
#     for code in codes:
#         for i in range(1, len(code)):
#             index_str = code[:i]
#             pattern = code[i:]
#
#             index = int(index_str)
#
#             if index + len(pattern) <= len(panel) and panel[index:index + len(pattern)] == pattern:
#                 results.append(pattern)
#             else:
#                 results.append("not found")
#
#     return results

def solution(panel, codes):
    results = []

    # Iterate over each code in the codes array
    for code in codes:
        found = False

        # Try different split-cases for the code
        for i in range(1, len(code)):  # i determines where to split the index and pattern
            index_str = code[:i]  # Split: index part
            pattern = code[i:]  # Split: pattern part

            # Convert index_str to integer
            index = int(index_str)

            # Check if index + length of pattern is within panel's bounds
            if index + len(pattern) <= len(panel):
                # Check if the substring in panel matches the pattern
                if panel[index:index + len(pattern)] == pattern:
                    results.append(pattern)
                    found = True
                else:
                    results.append("not found" )
        # If no valid match was found in all split-cases, append "not found"
        if not found:
            results.append("not found")

    return results


print(solution("2311453915", ["0211","639"]))