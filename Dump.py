import X, os
try:
    if os.path.exists('X.cpython-312.so'):
        os.system('git pull')  # on
except:
    exit(' something went wrong ')
