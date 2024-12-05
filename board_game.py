from cube_module import Cube
import random
import json

# Load dictionary from JSON file
with open('depth.json', 'r', encoding = 'utf-8') as file:
  depth = json.load(file)
depth = { int(k): v for k, v in depth.items() }   # Convert key string to integar
with open('path.json', 'r', encoding = 'utf-8') as file:
  path = json.load(file)
path = { int(k): v for k, v in path.items() }

class Player():
  def __init__(self, player_number, point):
    self.num = player_number  # num of player
    self.point = point        # starting point
    self.chance = 0           # decided by dice
    self.cube = 0             # cube instance

  def operation(self, player_input):
    self.chance -= 1
    {
        "U": lambda: self.cube.U(), "U'": lambda: self.cube.U_p(),
        "F": lambda: self.cube.F(), "F'": lambda: self.cube.F_p(),
        "R": lambda: self.cube.R(), "R'": lambda: self.cube.R_p()
    }.get(player_input)()

  def play(self, cube):
    self.cube = cube.print()
    self.chance = random.randint(1, 6)
    print(f'{self.num}번 플레이어 차례 입니다.')
    print(f'주사위 눈은 {self.chance}입니다.')
    while self.chance:
      print(f'    기회가 {self.chance}번 남았습니다.')
      while True:
        player_input = input('    회전하려면 기호를, 힌트를 보려면 H를 입력하세요 >> ')
        if player_input == 'H':
          if self.point:
            print(f'        정답까지 {depth[self.cube.getNum()]} 회전 남았습니다.')
            self.point -= 1
            print(f'        포인트가 {self.point}점 남았습니다.')
          else:
            print('        포인트가 없습니다.')
        elif player_input in [ "U", "U'", "F", "F'", "R", "R'" ]:
          self.operation(player_input)
          break
        else:
          print('        잘못된 입력입니다.')
      if self.cube.solved():
        return self.cube
    print(f'{self.num}번 플레이어의 차례가 끝났습니다.')
    return self.cube
  
while True:
  cube = Cube().input()
  if cube.getNum() not in depth:
    print('잘못된 입력입니다.')
  else:
    break

num_player = int(input('플레이어 수를 입력하세요 >> '))
point = int(input('플레이어가 가질 포인트를 입력하세요 >> '))
players = [ Player(i + 1, point) for i in range(num_player) ]

flag = False
while True:
  for player in players:
    cube = player.play(cube)
    if cube.solved():
      print(f'\n<< 승자는 {player.num}번 플레이어 입니다! >>')
      flag = True
      break
  if flag:
    break