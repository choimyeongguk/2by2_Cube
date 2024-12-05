class Cube:
  def __init__(self):
    self.__CtoN = { 'W': 0, 'G': 1, 'R': 2, 'Y': 3, 'B': 4, 'O': 5 }
    self.__NtoC = { 0: 'W', 1: 'G', 2: 'R', 3: 'Y', 4: 'B', 5: 'O' }
    self.state = [
        [ 'W', 'W', 'W', 'W' ], # 0, White,  Up
        [ 'G', 'G', 'G', 'G' ], # 1, Green,  Front
        [ 'R', 'R', 'R', 'R' ], # 2, Red,    Right
        [ 'Y', 'Y', 'Y', 'Y' ], # 3, Yellow, Down
        [ 'B', 'B', 'B', 'B' ], # 4, Blue,   Back
        [ 'O', 'O', 'O', 'O' ]  # 5, Orange, Left
    ]

  # Print net of cube
  def print(self):
    print(f'\n    {self.state[0][0]} {self.state[0][1]}')
    print(f'    {self.state[0][3]} {self.state[0][2]}')
    for i in [ 5, 1, 2, 4 ]:
      print(f'{self.state[i][0]} {self.state[i][1]} ', end = '')
    print()
    for i in [ 5, 1, 2, 4 ]:
      print(f'{self.state[i][3]} {self.state[i][2]} ', end = '')
    print()
    print(f'    {self.state[3][0]} {self.state[3][1]}')
    print(f'    {self.state[3][3]} {self.state[3][2]}\n')
    return self

  # Input cube's color
  def input(self):
    self.state[0] = list(input('윗   면 입력 >> ').split())
    self.state[1] = list(input('앞   면 입력 >> ').split())
    self.state[2] = list(input('오른 면 입력 >> ').split())
    self.state[3] = list(input('아랫 면 입력 >> ').split())
    self.state[4] = list(input('뒷   면 입력 >> ').split())
    self.state[5] = list(input('왼   면 입력 >> ').split())
    if self.state[3][3] != 'Y' or self.state[4][2] != 'B' or self.state[5][3] != 'O':
      print('노-파-주 조각을 아래-뒤-왼쪽 자리에 위치해 주세요\n')
      self.input()
    else:
      return self

  # Convert list to integar. 120byte -> 32byte
  def getNum(self):
    ret = 0
    for i in self.state:
      for j in i:
        ret *= 6
        ret += self.__CtoN[j]
    return ret

  # Convert integar to list
  def set(self, num):
    self.state = []
    for i in range(6):
      self.state.insert(0, [])
      for j in range(4):
        self.state[0].insert(0, self.__NtoC[num % 6])
        num //= 6
    return self

  # solved -> True, not solved -> False
  def solved(self):
    if self.getNum() == 731796345686735:
      return True
    return False

  # Rotate based on args
  def rotate(self, face, clockwise, li1, li2):
    li = [ 3, 2, 1 ] if clockwise else [ 1, 2, 3 ]
    tmp = self.state[face][0]
    self.state[face][0] = self.state[face][li[0]]
    self.state[face][li[0]] = self.state[face][li[1]]
    self.state[face][li[1]] = self.state[face][li[2]]
    self.state[face][li[2]] = tmp

    for li in li2:
      tmp = self.state[li1[0]][li[0]]
      self.state[li1[0]][li[0]] = self.state[li1[1]][li[1]]
      self.state[li1[1]][li[1]] = self.state[li1[2]][li[2]]
      self.state[li1[2]][li[2]] = self.state[li1[3]][li[3]]
      self.state[li1[3]][li[3]] = tmp

  def U(self):
    self.rotate(0, True,  [ 1, 2, 4, 5 ], [[ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ]])
    return self

  def U_p(self):
    self.rotate(0, False, [ 1, 5, 4, 2 ], [[ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ]])
    return self

  def F(self):
    self.rotate(1, True,  [ 0, 5, 3, 2 ], [[ 2, 1, 0, 3 ], [ 3, 2, 1, 0 ]])
    return self

  def F_p(self):
    self.rotate(1, False, [ 0, 2, 3, 5 ], [[ 2, 3, 0, 1 ], [ 3, 0, 1, 2 ]])
    return self

  def R(self):
    self.rotate(2, True,  [ 0, 1, 3, 4 ], [[ 1, 1, 1, 3 ], [ 2, 2, 2, 0 ]])
    return self

  def R_p(self):
    self.rotate(2, False, [ 0, 4, 3, 1 ], [[ 1, 3, 1, 1 ], [ 2, 0, 2, 2 ]])
    return self