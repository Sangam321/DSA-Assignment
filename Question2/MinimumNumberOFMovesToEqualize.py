def min_moves_to_equalize(sewing_machines):
    total_dresses = sum(sewing_machines)
    machines_count = len(sewing_machines)

    # If total dresses cannot be evenly distributed, return -1
    if total_dresses % machines_count != 0:
        return -1

    # Calculate the target number of dresses for each machine
    target_dresses = total_dresses // machines_count
    moves = 0

    for dresses in sewing_machines:
        # Calculate the difference between current dresses and the target
        diff = dresses - target_dresses
        if diff > 0:
            moves += diff

    return moves

if __name__ == "__main__":
    sewing_machines = [1, 0, 5]
    print(min_moves_to_equalize(sewing_machines)) 
