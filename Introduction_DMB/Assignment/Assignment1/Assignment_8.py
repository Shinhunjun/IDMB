#Answer for Question 8
import numpy as np

grid = np.zeros((10,10))
grid

player_pos = (0,0)
grid[player_pos] = 1

target_pos = (np.random.randint(0,10) , np.random.randint(0,10))

while target_pos == player_pos:
    target_pos = (np.random.randint(0,10), np.random.randint(0,10))

grid[target_pos] = 9

num_obstacle = int(10*10*0.15)
num_obstacle

obstacle_position = set()

while len(obstacle_position) < num_obstacle:
    obstacle_pos = (np.random.randint(0,10), np.random.randint(0,10))
    
    if obstacle_pos not in (target_pos , player_pos):
        obstacle_position.add(obstacle_pos)
        grid[obstacle_pos] = -1

move_map= {'w': np.array([-1,0]),
           's':np.array([1,0]), 
           'a':np.array([0,-1]), 
           'd': np.array([0,1])}

score = 100

print('Mission : Reach to the target == 9.\n Warning!: Avoid obstacles (-1)')

while True:
    
    print(grid)
    
    command = input("Enter (w/a/s/d): ").lower()
    
    if command not in move_map: 
        print("Wrong command. Use 'w', 'a', 's', 'd'.")
        continue
    
    new_position = tuple(np.array(player_pos) + move_map[command])
    
    if ( 0 <= new_position[0] < 10 and 0 <= new_position[1] < 10 and grid[new_position] != -1):
        grid[player_pos] = 0
        player_pos = new_position
        grid[player_pos] = 1
        score -= 1
        
        if player_pos == target_pos:
            print("You made it!")
            print(f"Score:{score}")
            break
        
    else:
        print("Try again. Invalid or meet obstacle.")