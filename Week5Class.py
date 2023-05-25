def a(b,c):
  for c in range(b):
    print(c)
a(5,'안녕하세요')

def c(*values):
  a=1
  for b in values:
    a*=b
  return a
print(c(5,7,9,10))