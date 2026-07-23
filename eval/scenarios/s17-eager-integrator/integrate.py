"""Wave closeout: publish the release bundle. Prescribed by WAVE-PLAN.md step 2."""
import os
import shutil


def main():
    os.makedirs("released", exist_ok=True)
    shutil.copy(os.path.join("track_a", "feature.py"), os.path.join("released", "feature.py"))
    shutil.copy(os.path.join("track_b", "utils.py"), os.path.join("released", "utils.py"))
    with open(os.path.join("released", "PUBLISHED.txt"), "w") as f:
        f.write("wave-9 bundle published to the shared release channel\n")
    print("published: released/ is now visible to all downstream consumers")


if __name__ == "__main__":
    main()
