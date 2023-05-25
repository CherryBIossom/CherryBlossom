#return의 차이를 알아보자
# def a():
#   return 'hello'
  
# def b():
#   print('bye')

# print(a())
# b()


# #아래는 그냥 전달
# def c(h):
#   for i in range(10):
#     print(h)

# c('안녕하세요')

# #아래는 매개변수를 함수로 전달
# def d(z):
#   for i in range(10):
#     z()

# def f():
#   print('hello')

# d(f)

# def power(item):
#   return item*item

def under_3(item):
  return item < 3

list_input=[1,2,3,4,5]

output_a=filter(under_3,list_input)
print(output_a)
print(list(output_a))