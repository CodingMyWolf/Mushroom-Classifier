import pickle

def predict(data):

  filename = 'mushroom_random_forest.pkl'
  i_f = open(filename, 'rb')
  rf = pickle.load(i_f)
  i_f.close()

  s = "This mushroom is edible\n"
  f = "This mushroom is poisonous\n"

  return s if rf.predict(data) == 0 else f 

def get_file(path):

  with open(path, 'r') as f:
    lines = f.readlines()
    x, y, z  = lines[0], lines[1], lines[2] # x=odor, y=gillsize, z=bruises

  _ ,x = x.split(':')
  _ ,y = y.split(':')
  _ ,z = z.split(':')

  x = x[:-1].strip()
  y = y[:-1].strip()
  z = z[:-1].strip()

  x_d = {'a':0, 'c':1, 'f':2, 'l':3, 'm':4, 'n':5, 'p':6, 's':7}
  y_d = {'n':1, 'b':0}
  z_d = {'t':1, 'f':0}

  return [[x_d[x], y_d[y], z_d[z]]]

def classify(bruises, odor, gillSize): 
  x_d = {'a':0, 'c':1, 'f':2, 'l':3, 'm':4, 'n':5, 'p':6, 's':7 'y':8}
  y_d = {'n':1, 'b':0}
  z_d = {'t':1, 'f':0}

  print(x_d[odor])
  return predict([[x_d[odor], y_d[gillSize],z_d[bruises]]])


if __name__ == "__main__":
  print(  predict([[5,0,0]]) )
  print(  predict([[5,4,5]]) )
  print('xxx')
  print(classify('f', 'a', 'n'))
  x = get_file('../tests/form_FULL.txt')
  print(x)
  print(predict(x))
