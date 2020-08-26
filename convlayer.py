import numpy as np

class ConvLayer:
  def __init__(self, filters, padding, stride, activation):
    self.p = padding
    self.s = stride
    self.activation = activation

    self.filtershape = filters[0].shape
    self.filterdimensions = len(self.filtershape)

    if self.filterdimensions > 3:
      except ValueError:
          print("Can't handle dimensions greater than 3")
          raise

    for filter in filters:

  def convolve_2d(self, n, f, stride=1):
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

  def convolve_3d(self, n, f, stride=1):
    (n_d, n_h, n_w) = n.shape
    (f_d, f_h, f_w) = f.shape

    a = np.zeros((n_d, int((n_w - f_w)/stride + 1), int((n_h - f_h)/stride + 1)))

    (o_d, o_h, o_w) = a.shape
    print(n.shape, f.shape)

    for i in range(o_d):
      a[i] = convolve_2d(n[i], f[i], stride)
    
    output = np.add(np.add(a[0], a[1]), a[2])

    return output
      


