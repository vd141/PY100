my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

my_list_index = 0

while my_list_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[my_list_index]):
            if my_list[my_list_index][inner_index] % 2 == 0:
                  print(my_list[my_list_index][inner_index])
            inner_index += 1
    my_list_index += 1