
from test_kms import test_kms_onedocker_init
from test_nsm import test_nsm_library_init

def run_tests():
    test_kms_onedocker_init()
    test_nsm_library_init()

if __name__ == "__main__":
    run_tests()

    import time

    while True:
        time.sleep(1)
        print(".", end="", flush=True)
