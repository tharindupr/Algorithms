for i in range(int(input())):
    N = int(input())
    bridges = {index + 1: int(connection) for index, connection in enumerate(input().split())}
    visited = set()
    component_count = 0
    towns = list(bridges.keys())
    while towns:
        current = towns[0]
        component = set()
        while current not in visited:
            towns.remove(current)
            visited.add(current)
            current = bridges[current]

        component_count += 1

    print(component_count - 1)
