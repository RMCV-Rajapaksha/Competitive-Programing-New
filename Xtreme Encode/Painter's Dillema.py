def painter_dilemma():
    t = int(input())
    for _ in range(t):
        n = int(input())
        colors = list(map(int, input().split()))
        brush1, brush2 = None, None
        changes = 0
        for color in colors:
            if color == brush1:
                brush1, brush2 = brush2, brush1
            elif color == brush2:
                brush1, brush2 = brush2, brush1
            else:
                changes += 1
                if brush1 is None:
                    brush1 = color
                else:
                    brush2 = color
        print(changes)

painter_dilemma()