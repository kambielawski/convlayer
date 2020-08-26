import numpy as np

def scope_test():

  def do_local():
    spam = "local spam"
  
  def do_nonlocal():
    # used to rebind variables outside of the innermost scope
    # i.e. when this function runs, declaring spam to be nonlocal 
    # makes Python look outside of do_nonlocal()
    nonlocal spam
    spam = "nonlocal spam"
  
  def do_global():
    global spam
    spam = "global spam"

  spam = "test spam"
  do_local()
  print("After local assignment: ", spam)
  do_nonlocal()
  print("After nonlocal assignment: ", spam)
  do_global()
  print("After global assignment: ", spam)

def convolve_2d(n, f, stride=1):
  (n_w, n_h) = n.shape
  (f_w, f_h) = f.shape

  output = np.zeros((int((n_w - f_w)/stride + 1), int((n_h - f_h)/stride + 1)))

  (o_w, o_h) = output.shape
  
  for i in range(int(n_w/stride)):
    for j in range(int(n_h/stride)):
      sm = 0
      
      for f_i in range(f_w):
        for f_j in range(f_h):
          sm += f[f_i][f_j]*n[i*stride+f_i][j*stride+f_j]

      output[i][j] = sm

  return output

def convolve_3d(n, f, stride=1):
  (n_d, n_h, n_w) = n.shape
  (f_d, f_h, f_w) = f.shape

  a = np.zeros((n_d, int((n_w - f_w)/stride + 1), int((n_h - f_h)/stride + 1)))

  (o_d, o_h, o_w) = a.shape
  print(n.shape, f.shape)

  for i in range(o_d):
    a[i] = convolve_2d(n[i], f[i], stride)
  
  output = np.add(np.add(a[0], a[1]), a[2])

  return output



  
if __name__ == '__main__':
  n = np.ones((3,4,4))
  n[0,0,0] = 5
  f = np.array([[[2,2],[2,2]], [[2,2], [2,2]], [[2,2], [2,2]]])
  print(f.shape)
  print(convolve_3d(n, f, 2))