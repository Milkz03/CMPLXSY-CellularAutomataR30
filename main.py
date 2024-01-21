def stateOne(state, row, count):
  a = "1"
  b = "1"
  c = "1"
  if count == 0:
    return False
  if count == len(state[0])-1:
    return False
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c

def stateTwo(state, row, count):
  a = "1"
  b = "1"
  c = "0"
  if count == 0:
    return False
  if count == len(state[0])-1:
    return state[row][count-1] == a and state[row][count] == b
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c

def stateThree(state, row, count):
  a = "1"
  b = "0"
  c = "1"
  if count == 0:
    return False
  if count == len(state[0])-1:
    return False
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c

def stateFour(state, row, count):
  a = "1"
  b = "0"
  c = "0"
  if count == 0:
    return False
  if count == len(state[0])-1:
    return state[row][count-1] == a and state[row][count] == b
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c

def stateFive(state, row, count):
  a = "0"
  b = "1"
  c = "1"
  if count == 0:
    return state[row][count] == b and state[row][count+1] == c
  if count == len(state[0])-1:
    return False
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c

def stateSix(state, row, count):
  a = "0"
  b = "1"
  c = "0"
  if count == 0:
    return state[row][count] == b and state[row][count+1] == c
  if count == len(state[0])-1:
    return state[row][count-1] == a and state[row][count] == b
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c
  
def stateSeven(state, row, count):
  a = "0"
  b = "0"
  c = "1"
  if count == 0:
    return state[row][count] == b and state[row][count+1] == c
  if count == len(state[0])-1:
    return False
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c

def stateEight(state, row, count):
  a = "0"
  b = "0"
  c = "0"
  if count == 0:
    return state[row][count] == b and state[row][count+1] == c
  if count == len(state[0])-1:
    return state[row][count-1] == a and state[row][count] == b
  return state[row][count-1] == a and state[row][count] == b and state[row][count+1] == c


def main():
  #set up and initialize range
  cellsCol = 25
  cellsRow = 13
  state = [["0" for x in range(cellsCol)] for y in range(cellsRow)]

  #place start in the middle
  state[0][cellsCol//2] = "1"

  #change next row based on current state
  for i in range(cellsRow-1):
    for j in range(cellsCol):
      if stateOne(state, i, j):
        state[i+1][j] = "0"
      if stateTwo(state, i, j):
        state[i+1][j] = "0"
      if stateThree(state, i, j):
        state[i+1][j] = "0"
      if stateFour(state, i, j):
        state[i+1][j] = "1"
      if stateFive(state, i, j):
        state[i+1][j] = "1"
      if stateSix(state, i, j):
        state[i+1][j] = "1"
      if stateSeven(state, i, j):
        state[i+1][j] = "1"
      if stateEight(state, i, j):
        state[i+1][j] = "0"

  #print output
  for i in range(cellsRow):
    for j in range(cellsCol):
      if state[i][j] == "0":
        print(" ", end = "")
      else:
        print("X", end = "")
    print("")
  

if __name__ == "__main__":
  main()