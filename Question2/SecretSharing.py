def get_individuals(n, intervals, first_person):
    result = set()
    known_secrets = set()
    known_secrets.add(first_person)

    for interval in intervals:
        start, end = interval

        new_individuals = set()

        for i in range(start, end + 1):
            if i in known_secrets:
                # Add individuals who receive the secret during this interval
                for j in range(n):
                    if j not in known_secrets:
                        new_individuals.add(j)

        known_secrets.update(new_individuals)

    result.update(known_secrets)
    return sorted(list(result))

if __name__ == "__main__":
    n = 5
    intervals = [[0, 2], [1, 3], [2, 4]]
    first_person = 0

    result = get_individuals(n, intervals, first_person)

    print("Individuals who will eventually know the secret:", result)
