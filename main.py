import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n))
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    xvec, yvec = pad(xvec, yvec)
    #print('   '*len(xvec), xvec, yvec)
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
    # 4 recursive calls
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    # x_L * y_L
    left_product = _quadratic_multiply(x_left, y_left)
    # x_R * y_R
    right_product = _quadratic_multiply(x_right, y_right)
    # x_L * y_R
    left_right_product = _quadratic_multiply(x_left, y_right)
    # x_R * y_L
    right_left_product = _quadratic_multiply(x_right, y_left)
    
    # O(n) addition: x_L*y_R + x_R*y_L
    middle_term = BinaryNumber(left_right_product.decimal_val +
                               right_left_product.decimal_val)
    # 2^{n/2} (x_L*y_R + x_R*y_L)
    middle_term = bit_shift(middle_term, len(xvec)//2)
    
    # 2^n (x_L * y_L)
    left_product = bit_shift(left_product, len(xvec))
    
    # O(n) addition
    return BinaryNumber(left_product.decimal_val +
                        middle_term.decimal_val +
                        right_product.decimal_val)


## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8
    assert quadratic_multiply(BinaryNumber(9), BinaryNumber(8)) == 9*8
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10

test_multiply()
#quadratic_multiply(BinaryNumber(8), BinaryNumber(9))
def subquadratic_multiply(x, y):
    return _subquadratic_multiply(x,y).decimal_val
    
def _subquadratic_multiply(x,y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    xvec, yvec = pad(xvec, yvec)
#     print('  ' * len(xvec), xvec, yvec)
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
    # 4 recursive calls
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    # x_L * y_L
    left_product = _subquadratic_multiply(x_left, y_left)
    # x_R * y_R
    right_product = _subquadratic_multiply(x_right, y_right)
    # x_L + x_R
    xsum = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    # y_L + y_R
    ysum = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
    # recursive call plus O(n) addition
    # (x_L + x_R) * (y_L + y_R) - (x_L * y_L) - (x_R * y_R)
    middle_term = BinaryNumber(_subquadratic_multiply(xsum, ysum).decimal_val -
                               left_product.decimal_val -
                               right_product.decimal_val)
    # 2^{n/2}  (x_L*y_R + x_R*y_L)
    middle_term = bit_shift(middle_term, len(xvec)//2)
    # 2^n (x_L * y_L)
    left_product = bit_shift(left_product, len(xvec))
    # O(n) addition
    ret = BinaryNumber(left_product.decimal_val + middle_term.decimal_val + right_product.decimal_val)
    return ret
    

## Feel free to add your own tests here.
def test_subquadratic_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8
    assert subquadratic_multiply(BinaryNumber(9), BinaryNumber(8)) == 9*8
    assert subquadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10

# subquadratic_multiply(BinaryNumber(8), BinaryNumber(9))
test_subquadratic_multiply()


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    ns = [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
    for n in ns:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)
    
    plt.figure()
    plt.plot(ns, [r[1] for r in res], 'o-', label='quadratic')
    plt.plot(ns, [r[2] for r in res], 'o-', label='subquadratic')
    plt.legend()
    plt.show()


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
    
compare_multiply()