import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shay/a/vanderg0/ece569-fall2025/Lab4/install/py_joint_pub'
