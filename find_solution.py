from collections import deque
import json

queue = deque()
rank = {}   # 최소 회전 수
move = {}   # 각 상황별 최적 풀이 위한 회전

def insert(cnt, state, rotation, num):
  if num not in rank:
    queue.append(num)
    rank[num] = rank[state] + 1
    move[num] = rotation
    cnt += 1
  return cnt

# BFS에 사용할 큐와 딕셔너리 선언 및 맞춰진 상태(시작 노드) 삽입
queue.append(Cube().getNum())
rank[queue[0]] = 0
move[queue[0]] = ""
cnt = 1   # rank가 0인 상태의 개수

while queue:
  iter = cnt
  cnt = 0
  for i in range(iter):
    state = queue.popleft()
    cube = Cube().set(state)
    cnt = insert(cnt, state, "U'",  cube.U().getNum())        # U
    cnt = insert(cnt, state, "U", cube.U_p().U_p().getNum())  # U'
    cnt = insert(cnt, state, "F'",  cube.U().F().getNum())    # F
    cnt = insert(cnt, state, "F", cube.F_p().F_p().getNum())  # F'
    cnt = insert(cnt, state, "R'",  cube.F().R().getNum())    # R
    cnt = insert(cnt, state, "R", cube.R_p().R_p().getNum())  # R'

# 탐색한 결과를 json 파일로 저장
# json 파일에 정확히 3,674,160 개의 key:val 쌍이 저장된 걸로 보아 모든 경우를 탐색했음을 알 수 있다.
# 최적 회전 수의 최대값이 14인걸로 보아 최적 회전 수를 올바르게 탐색했음을 알 수 있다.
with open('rank.json', 'w', encoding = 'utf-8') as file:
  json.dump(rank, file, indent = 4)
with open('move.json', 'w', encoding = 'utf-8') as file:
  json.dump(move, file, indent = 4)