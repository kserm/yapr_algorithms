n = int(input())
num1_list = list(map(int, input().split()))
num2_list = list(map(int, input().split()))

num1 = ''.join(map(str, num1_list))
num2 = ''.join(map(str, num2_list))

res = int(num1) + int(num2)
res_list = list(str(res))

for i in range(len(res_list)):
    print(int(res_list[i]), end=' ')
