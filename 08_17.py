import queue

q = queue.Queue()
def find_prime(a):
    flag = 0
    for j in range(2,int(a/2)+1):
        if(a % j == 0):
            flag = 1
            break
    return flag

def check(first, second):
    f_4 = int(first / 1000)
    f_3 = int(first % 1000 / 100)
    f_2 = int((first % 100) / 10)
    f_1 = int(first % 10)

    s_4 = int(second / 1000)
    s_3 = int(second % 1000 / 100)
    s_2 = int((second % 100) / 10)
    s_1 = int(second % 10)



    count = 0
    if(f_4 == s_4):
        count += 1

    if(f_3 == s_3):
        count += 1
    if(f_2 == s_2):
        count += 1
    if(f_1 == s_1):
        count += 1

    if(count >= 3):
        return True
    else:
        return False

first, second = map(int,input().split(' '))
prime_list = []
prime_list.append(first)
last_num = second
first_num = first

for k in range(first+1, second):
    result = find_prime(k)
    if(result == 0):
        prime_list.append(k)
prime_list.append(second)

matrix = [[first_num] for i in range(len(prime_list)+1)]
q.put((0, 0, matrix))

while(q.empty() == False):

    index_num, count, start_point = q.get()

    if(check(prime_list[index_num], last_num)):
        matrix[start_point].append(last_num)
        print(matrix[start_point])
        break

    for i in range(index_num+1, len(prime_list)):
        if(check(prime_list[index_num], prime_list[i])):
            if(index_num == 0):
                matrix[i].append(prime_list[i])
                q.put((i, count + 1, i))
            else:
                matrix[start_point].append(prime_list[i])
                q.put((i, count + 1, start_point))