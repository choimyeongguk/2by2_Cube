from cube_module import Cube
import json

# Load dictionary from JSON file
with open('depth.json', 'r', encoding = 'utf-8') as file:
  depth = json.load(file)
depth = { int(k): v for k, v in depth.items() }   # Convert key string to integar
with open('path.json', 'r', encoding = 'utf-8') as file:
  path = json.load(file)
path = { int(k): v for k, v in path.items() }

cube = Cube().input().print()
operation = { "U": lambda: cube.U(), "U'": lambda: cube.U_p(),
              "F": lambda: cube.F(), "F'": lambda: cube.F_p(),
              "R": lambda: cube.R(), "R'": lambda: cube.R_p() }
print(f'\nrotation : {depth[cube.getNum()]}')
print('solution : ', end = '')
while True:
  state = cube.getNum()
  print(path[state] + ' ', end = '')
  if depth[state] == 0:
    break
  operation[path[state]]()