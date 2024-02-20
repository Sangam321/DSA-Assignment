class MinMovesToEqualizeDressesQ2_a:
    @staticmethod
    def min_moves_to_equalize(sewing_machines):
        total_dresses = sum(sewing_machines)
        machines_count = len(sewing_machines)

        if total_dresses % machines_count != 0:
            return -1

        target_dresses = total_dresses // machines_count
        moves = 0

        for dresses in sewing_machines:
            diff = dresses - target_dresses
            if diff > 0:
                moves += diff

        return moves

if __name__ == "__main__":
    sewing_machines = [1,2,3,4,5]
    print(MinMovesToEqualizeDressesQ2_a.min_moves_to_equalize(sewing_machines))
