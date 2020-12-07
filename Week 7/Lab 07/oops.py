def main():
  bubble = 23.14069
  y = 20.02
  printer1(y, 14.0)
  printer2(bubble)
  printer1("pierce", "franklin")
  printer1(bubble, y)
  println(5)
  
def printer1(x, y):
    print("x =", x, "and y =", y)
  
def printer2(value):
    print("The value from main is:", value)

def println(z):
    print("z =", z)
    
main()
