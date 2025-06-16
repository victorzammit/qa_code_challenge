import subprocess

if __name__ == "__main__":
    print("Running tests...")
    with open("test_failures.log", "w") as logfile:
        result = subprocess.run(
            ["pytest", "./build/tests"],
            stdout=logfile,
            stderr=logfile
        )
    if result.returncode == 0:
        print("Tests passed ✅")
    else:
        print("Tests failed ❌ — see test_failures.log")