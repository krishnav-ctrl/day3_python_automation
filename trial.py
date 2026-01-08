import os
folder_path = r"C:\Users\Parkavi.S\OneDrive\Desktop\trial"
files = os.listdir(r"C:\Users\Parkavi.S\OneDrive\Desktop\trial")
print(f"total files found:{len(files)}")
for i,filename in enumerate(files, start=1):
    if filename == "trial.py":
        continue
    old_path = os.path.join(folder_path , filename)
    name , extension= os.path.splitext(filename)
    new_name = f"file_{i}{extension}"
    new_path = os.path.join(folder_path , new_name)
    os.rename(old_path , new_path)
    print(f"done:{filename} -> {new_name}")