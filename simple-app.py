import sys, os

args = sys.argv[1:]

if len(args) > 0:
    current_dir = os.getcwd()
    for file in args:
        full_file_path = os.path.join(current_dir, file)
        if os.path.isfile(full_file_path):
            print(f"Printing {full_file_path} file content:")
            with open(full_file_path, 'r') as f:
                print(f.read())
                f.close()
            print()
            print()
else:
    print("Files in current directory:")
    for file in os.listdir("./"):
      print(file)
