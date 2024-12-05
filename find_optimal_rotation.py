from cube_module import Cube
from collections import deque
import json

def insert(num, state, newCnt, queue, rank):
  if num not in rank:
    queue.append(num)
    rank[num] = rank[state] + 1
    newCnt += 1
  return newCnt

# BFS에 사용할 큐와 딕셔너리 선언 및 맞춰진 상태(시작 노드) 삽입
queue = deque()
queue.append(Cube().getNum())
rank = { queue[0]:0 }
newCnt = 1   # rank가 0인 상태의 개수

while queue:
  cnt = newCnt
  newCnt = 0
  for i in range(cnt):
    state = queue.popleft()
    cube = Cube()
    cube.set(state)

    newCnt = insert(cube.U().getNum(), state, newCnt, queue, rank)          # U
    newCnt = insert(cube.U_p().U_p().getNum(), state, newCnt, queue, rank)  # U'
    newCnt = insert(cube.U().F().getNum(), state, newCnt, queue, rank)      # F
    newCnt = insert(cube.F_p().F_p().getNum(), state, newCnt, queue, rank)  # F'
    newCnt = insert(cube.F().R().getNum(), state, newCnt, queue, rank)      # R
    newCnt = insert(cube.R_p().R_p().getNum(), state, newCnt, queue, rank)  # R'

# 탐색한 결과를 json 파일로 저장
# json 파일에 정확히 3,674,160 개의 key:val 쌍이 저장된 걸로 보아 모든 경우를 탐색했음을 알 수 있다.
# 최적 회전 수의 최대값이 14인걸로 보아 최적 회전 수를 올바르게 탐색했음을 알 수 있다.
with open('optimal_rotation_2by2Cube', 'w', encoding = 'utf-8') as file:
  json.dump(rank, file, ensure_ascii = False, indent = 4)