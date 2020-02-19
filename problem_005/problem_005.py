import time
def f():
    result = 1
    i = 1
    while 1:
        if result%i==0 and result%(i+1)==0 and result%(i+2)==0 and result%(i+3)==0 and result%(i+4)==0 and result%(i+5)==0 and result%(i+6)==0 and result%(i+7)==0 and result%(i+8) == 0 and result%(i+9)==0 and result%(i+10)==0 and result%(i+11)==0 and result%(i+12)==0 and result%(i+13)==0 and result%(i+14)==0 and result%(i+15)==0 and result%(i+16)==0 and result%(i+17)==0 and result%(i+18)==0 and result%(i+19)==0:
            return result
        result += 1
    return 
start = time.time()
print(f())
end = time.time()
print(end-start)