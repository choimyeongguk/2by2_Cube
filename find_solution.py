from cube_module import Cube
from collections import deque
import json

queue = deque()
depth = {}   # minimun rotation to solve
path = {}   # optimal path to solve

def insert(cnt, state, rotation, num):
  if num not in depth:
    queue.append(num)
    depth[num] = depth[state] + 1
    path[num] = rotation
    cnt += 1
  return cnt

# Initialize queue for BFS and dictionary. Insert start node(solved case)
queue.append(Cube().getNum())
depth[queue[0]] = 0
path[queue[0]] = ""
cnt = 1   # num of case depth = 0

while queue:
  iter = cnt
  cnt = 0
  for i in range(iter):
    state = queue.popleft()
    cube = Cube().set(state)
    cnt = insert(cnt, state, "U'", cube.U().getNum())          # U
    cnt = insert(cnt, state, "U",  cube.U_p().U_p().getNum())  # U'
    cnt = insert(cnt, state, "F'", cube.U().F().getNum())      # F
    cnt = insert(cnt, state, "F",  cube.F_p().F_p().getNum())  # F'
    cnt = insert(cnt, state, "R'", cube.F().R().getNum())      # R
    cnt = insert(cnt, state, "R",  cube.R_p().R_p().getNum())  # R'

# Save result as JSON
# num of key:val pair is 3,674,160 & max of depth is 14 -> searched correctly!
with open('depth.json', 'w', encoding = 'utf-8') as file:
  json.dump(depth, file, indent = 4)
with open('path.json', 'w', encoding = 'utf-8') as file:
  json.dump(path, file, indent = 4)