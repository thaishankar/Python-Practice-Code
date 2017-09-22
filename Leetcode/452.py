def findMinArrowShots(points):
        if len(points) == 0:
            return 0
        
        points = sorted(points, key = lambda x:x[1])

        end = points[0][1]
        arrow = 1

        for point in points:
            if point[0] > end:
                end = point[1]
                arrow += 1
        return arrow

if __name__ == '__main__':
    balloons =  [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    print findMinArrowShots(balloons)
