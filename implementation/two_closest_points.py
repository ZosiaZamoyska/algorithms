import math

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair, min_dist

def closest_split_pair(px, py, delta, best_pair):
    mid_x = px[len(px) // 2][0]
    strip = [p for p in py if abs(p[0] - mid_x) < delta]

    min_dist = delta
    n = len(strip)
    for i in range(n):
        for j in range(i+1, min(i+7, n)):  # only check up to 7 neighbors
            p, q = strip[i], strip[j]
            dist = euclidean_distance(p, q)
            if dist < min_dist:
                min_dist = dist
                best_pair = (p, q)
    return best_pair, min_dist

def closest_pair_rec(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)

    mid = n // 2
    Qx = px[:mid]
    Rx = px[mid:]

    midpoint = px[mid][0]
    Qy = [p for p in py if p[0] <= midpoint]
    Ry = [p for p in py if p[0] > midpoint]

    (p1, q1), dist1 = closest_pair_rec(Qx, Qy)
    (p2, q2), dist2 = closest_pair_rec(Rx, Ry)

    if dist1 < dist2:
        best_pair = (p1, q1)
        delta = dist1
    else:
        best_pair = (p2, q2)
        delta = dist2

    return closest_split_pair(px, py, delta, best_pair)

def closest_pair(points):
    px = sorted(points, key=lambda x: x[0])  # sort by x
    py = sorted(points, key=lambda x: x[1])  # sort by y
    return closest_pair_rec(px, py)

# Example:
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest, dist = closest_pair(points)
print("Closest pair:", closest)
print("Distance:", dist)
