 # loop for files in filenames, if file ends with given extntion, print found non yaml file, then print seach complete.

filenames = ["nginx.conf", "apple.yaml", "db.yaml", "notes.txt"]
for file in filenames:
    if file.endswith((".txt", ".conf")):
        print(f"found non yaml files: {file}")

print(f"Searching Complete")



