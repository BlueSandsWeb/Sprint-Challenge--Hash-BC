#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


# === ALWAYS RETURN LARGER INDEX FIRST TO PASS TESTS

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length < 2:
        return None
    elif length == 2:
        if weights[1] + weights[0] == limit:
            print("RETURNING: ", )
            return [1, 0]
        else:
            return None
    else:
        # add all array items to the hash table
        for i in range(len(weights)):
            hash_table_insert(ht, weights[i], i)
        
        for item in range(0, limit+1):
            max = limit - item

            low_num = hash_table_retrieve(ht, item)
            print("LOW NUM: ", low_num)
            if low_num is not None:
                hash_table_remove(ht, item)
                high_num = hash_table_retrieve(ht, max)
                print("HIGH NUM: ", high_num)
                if high_num is not None:
                    print("RETURNING", [high_num, low_num])
                    return [high_num, low_num]
        return None




    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
