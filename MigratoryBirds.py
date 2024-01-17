def migratoryBirds(arr):
    # Loop to find the frequency of each bird in the array. Return the bird that is most frequent
    # but also lowest ID number. Birds in array are intagers.
    bird_map = {}
    max_bird = None
    for i, bird in enumerate(arr):
        if bird not in bird_map:
            bird_map[bird] = 1
            if max_bird is None:
                max_bird = bird
            elif bird_map[bird] == bird_map[max_bird]:
                max_bird = min(bird, max_bird)
        else:
            bird_map[bird] += 1
            if bird_map[bird] > bird_map[max_bird]:
                max_bird = bird
            elif bird_map[bird] == bird_map[max_bird]:
                max_bird = min(bird, max_bird)
    return max_bird

print(migratoryBirds([2, 1]))