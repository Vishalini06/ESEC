import sys

def main():
    # Read input
    N, P = map(int, sys.stdin.readline().split())  # Number of ingredients and packages per ingredient
    required = list(map(int, sys.stdin.readline().split()))  # Grams needed per serving

    packages = []
    for i in range(N):
        package_list = []
        quantities = list(map(int, sys.stdin.readline().split()))
        for q in quantities:
            min_val = (10 * q + 11 * required[i] - 1) // (11 * required[i])
            max_val = (10 * q) // (9 * required[i])
            if min_val <= max_val:
                package_list.append((min_val, max_val))
        package_list.sort()  # Sort by lower range
        packages.append(package_list)

    ptr = [0] * N
    kits = 0

    while True:
        # Check if any ingredient is out of packages
        if any(ptr[i] >= len(packages[i]) for i in range(N)):
            break

        # Find the max lower bound among the current package selections
        current_min = max(packages[i][ptr[i]][0] for i in range(N))

        # Check if all selected packages can form a valid kit
        if all(packages[i][ptr[i]][1] >= current_min for i in range(N)):
            kits += 1
            ptr = [ptr[i] + 1 for i in range(N)]  # Move all pointers to the next package
        else:
            # Find the minimum upper bound and move its pointer
            min_high = min(packages[i][ptr[i]][1] for i in range(N))
            for i in range(N):
                if packages[i][ptr[i]][1] == min_high:
                    ptr[i] += 1

    print(kits)

if __name__ == "__main__":
    main()
