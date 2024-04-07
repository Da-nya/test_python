numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def checkAnswer(arr):
  values = [] # массив для чисел
  calc_signs = [] # массив для операций над числами

  # через пропуски в arr задаем числа и операции над ними
  x = numbers[0];
  for i in range(len(arr)) :
    if arr[i] == '' :
      x = x*10 + numbers[i+1]
    else:
      calc_signs.append(arr[i])
      values.append(x);
      x = numbers[i+1]
  values.append(x)

  sum = values[0]
  for i in range(len(calc_signs)) :
    if calc_signs[i] == '+' :
      sum = sum + values[i+1]
    else:
      sum = sum - values[i+1]

  if sum == 200 :
    answer = str(values[0])
    for i in range(len(calc_signs)) :
      answer = answer + ' ' + calc_signs[i] + ' ' + str(values[i+1])
    answer = answer + ' = 200'
    print(answer)
  return

# рекурсивно перебираем  все возможные варианты +, -, или пропуск
def cycle(arr, index) :
  if index >= len(numbers) - 1 :
    checkAnswer(arr)
    return

  for i in '+', "-", '' :
    arr[index] = i
    cycle(arr, index + 1)
  return

cycle(['']*9, 0)