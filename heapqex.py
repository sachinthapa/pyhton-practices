import heapq

a = [5, 6, 7, 4, 3, 2, 1]  #[2, 3, 5, 4, 6, 7] 
a2 = [3, 5, 1, 2, 6, 8, 7] # [1, 2, 3, 5, 6, 8, 7]

heapq.heapify(a)
heapq.heapify(a2)

heapq.heappop(a)
heapq.heappop(a)
heapq.heappop(a)

heapq.heappush(a,8)
heapq.heappush(a,2)
print (a,"", a2)


results="""\
Christania Williams      11.80
Marie-Josee Ta Lou       10.86
Elaine Thompson          10.71
Tori Bowie               10.83
Shelly-Ann Fraser-Pryce  10.86
English Gardner          10.94
Michelle-Lee Ahye        10.92
Dafne Schippers          10.90
"""
top_3 = heapq.nsmallest(
     3, results.splitlines(),lambda x: float(x.split()[-1])
    )

print("\n".join(top_3), end = "\n\n")


map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""

def parse_map(map):
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination

lines, origin, destination = parse_map(map)

def is_valid(lines, position):
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    if lines[y][x] == "X":
        return False
    return True

def get_neighbors(lines, current):
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position

def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path

def find_path(map):
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}
    candidates = [(0 , origin)]
    certain = set()   
    print(f"origin: {origin}")
    print(f"destination: {destination}")
    print(f"lines: {lines}")
    print(f"tentative: {tentative}", end = "\n\n")
   
    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        print(current)
        
        if current in certain:
            print(f"{current} in {certain}")
            continue
        
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)

        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))

    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        raise ValueError("no path")

def show_path(path, map):
    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + "?" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"

path = find_path(map) 
print(map)
print(show_path(path,map))











