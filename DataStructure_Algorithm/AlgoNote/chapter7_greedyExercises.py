
# 救生艇
def numRescueBoats(self, people: list[int], limit: int) -> int:
    # 按数值排序
    people.sort()
    n = len(people)
    numBoats = 0

    # 双指针，最大值和最小值配对
    p, q = 0, n-1
    while p < q:
        # 船可以载2个人
        if people[p] + people[q] <= limit:
            numBoats += 1
            p += 1
            q -= 1
        # 船只能载1个人，先载重的
        else:
            numBoats += 1
            q -= 1
    # 边界情况，最后还剩下1个人
    if p == q:
        numBoats += 1

    return numBoats

# 卡车上的最大单元数
def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
    boxTypes.sort(key= lambda x: x[1], reverse= True)
    maxUnits = 0
    numBoxes = 0

    for box in boxTypes:
        if numBoxes + box[0] <= truckSize:
            maxUnits += box[0] * box[1]
            numBoxes += box[0]
        else:
            maxUnits += (truckSize - numBoxes) * box[1]
            numBoxes = maxUnits
            break

    return maxUnits

def findMinArrowShots(points: list[list[int]]) -> int:
    def _isOverlap_(a: list[int], b: list[int]):
        # 假设 a[0] <= b[0]
        if a[1] >= b[0]:
            return True
        else:
            return False

    points.sort(key= lambda x: x[0])
    n = len(points)
    i = 0
    cnt = 0

    while i < n:
        point = points[i]
        # 区间之间都有重叠/两两重叠
        while i < n and _isOverlap_(point, points[i]):
            point = [points[i][0], min(point[1], points[i][1])]
            i += 1
        # 射出一只箭，爆破对应的所有气球
        cnt += 1

    return cnt


points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[2,3],[3,4],[4,5]]
points = [[1,5],[2,3],[3,4],[4,5]]
points = [[1,2],[2,5],[3,5],[4,5],[5,6]]
points = [[1,10],[3,9],[4,11],[6,9],[6,7],[8,12],[9,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))
