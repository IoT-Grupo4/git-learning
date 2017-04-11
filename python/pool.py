from multiprocessing import Pool

def squared(x):
    return x*x

if __name__ == '__main__':
  values = [2, 3, 4]
    with Pool(5) as p:
        print(p.map(squared, values ))
