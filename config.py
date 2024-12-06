import os 

PY_ENV = os.environ.get('PY_ENV', 'local')
ip = "0.0.0.0" if (PY_ENV == 'production') else "127.0.0.1"

class Config:
    HOST_IP = ip