import sys, os

with open(os.path.join("./", "test1.txt"), "w") as file1:
  file1.write("FIRST TEST\n")
  file1.close()

with open(os.path.join("./", "test2.txt"), "w") as file2:
  file2.write("SECOND TEST\n")
  file2.close()
