#  using bottom up (a way to avoid recursion)
#  locate a list max_values_at_capacities
#  know the max value for each capacity
#

def max_bag_value(stone_tuples, weight_capacity):
    #list to hold max possible value at capacity
    max_val_at_capacity = [0]*(weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        # max monetary val so far
        current_max_val = 0

        for stone_weight, stone_value in stone_tuples:
            #0 weight and a +ve value means infinite value of bag
            if stone_weight == 0 and stone_value !=0:
                return float('inf')

            #checking if the current stone is less than or equal to the capacity.
            if stone_weight <= current_capacity:
                #check the value of ising the stone

                max_value_using_stone = (stone_value + max_val_at_capacity[current_capacity-stone_weight])

                #compare to the current max value to get new max value between the two

                current_max_val = max(max_value_using_stone, current_max_val)

                #store the max values at every stage  to use in calculating the remaining capacities

                max_val_at_capacity[current_capacity] = current_max_val
            return max_val_at_capacity[weight_capacity]

def knapsackDP(w, v, W): #(weight, value, W)
    n = len(v)

    if n <= 0 or W <= 0:
        return 0

    m = [[0 for x in range(W + 1)] for y in range(n + 1)]
    #  m[i][j] gives
    #  m[0][j] = 0, for all j, since if there is zero item then we can get 0 max value
    #  m[i][0] = 0, for all i, since if max weight limit is 0 then we get 0 max value

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i - 1] > j:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j],
                              m[i - 1][j - w[i - 1]] + v[i - 1])

    return m[n][W]