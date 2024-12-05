from cube_module import Cube
import json

# json 파일로 딕셔너리 불러오기
with open('rank.json', 'r', encoding = 'utf-8') as file:
  rank = json.load(file)
rank = { int(k): v for k, v in rank.items() }   # 문자열로 저장되어 있는 key를 정수로 변환
with open('move.json', 'r', encoding = 'utf-8') as file:
  move = json.load(file)
move = { int(k): v for k, v in move.items() }

cube = Cube()
cube.input()
cube.print()
print(f'\nrotation : {rank[cube.getNum()]}')
print('solution : ', end = '')
while True:
  state = cube.getNum()
  print(move[state] + ' ', end = '')
  if rank[state] == 0:
    break
  match move[state]:
    case "U":
      cube.U()
    case "U'":
      cube.U_p()
    case "F":
      cube.F()
    case "F'":
      cube.F_p()
    case "R":
      cube.R()
    case "R'":
      cube.R_p()