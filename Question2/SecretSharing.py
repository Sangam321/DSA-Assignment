def get_individuals(n, intervals, first_person):
    knows_secret = [False] * n 
    knows_secret[first_person] = True  # Mark the first person as knowing the secret 
    for interval in intervals:
        for i in range(interval[0], interval[1] + 1):
            if knows_secret[i]:
                for j in range(interval[0], interval[1] + 1):
                    knows_secret[j] = True
                break

    result = [i for i in range(n) if knows_secret[i]]
    return result


if __name__ == "__main__":
    n = 5  # Total number of individuals
    intervals = [(0, 2), (1, 3), (2, 4)] 
    first_person = 0
    result = get_individuals(n, intervals, first_person)

    print("Individuals who will eventually know the secret:", result)
