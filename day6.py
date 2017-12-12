input = '''10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'''
memory = [int(x) for x in input.split('\t')]


memory_status = []

def update_memoery(memory):
    highest_bank = max(memory)
    highest_index = memory.index(highest_bank)
    memory[highest_index] = 0
    i = 0
    while i < highest_bank:
        memory[(highest_index + i + 1) % len(memory)] += 1
        i += 1
    return tuple(memory)


def find_steps(memory):
    steps = 0
    memory_history = [tuple(memory)]
    #while memory not in memory_status:
    while True:
        new_memory = update_memoery(memory)
        steps += 1
        if new_memory in memory_history:
            break
        else:
            memory_history.append(new_memory)
      
    return steps
    
if __name__ == '__main__':
    print(find_steps(memory))
