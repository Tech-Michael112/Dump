import X, os
try:
    if os.path.exists('X.cpython-312.so'):  # Added missing colon
        os.system('git pull')  # Added proper indentation
except:
    exit(' something went wrong ')
