import pytest
import sys

if __name__ == "__main__":
    status = pytest.main(["./build/tests"])
    if status != 0:
        print(f"Tests failed with exit code {status} ❌")
    else:
        print("Tests passed ✅")
    sys.exit(status)