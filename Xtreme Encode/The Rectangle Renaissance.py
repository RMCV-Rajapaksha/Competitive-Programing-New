def max_rectangular_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, heights[top_of_stack] * width)

    while stack:
        top_of_stack = stack.pop()
        width = index if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[top_of_stack] * width)

    return max_area

n = int(input())
heights = list(map(int, input().split()))
print(max_rectangular_area(heights))