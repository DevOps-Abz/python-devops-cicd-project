#  Task: Log errors into a file


results = ["web01: OK", "db: ERROR", "api: OK"]
for result in results:
    if result.endswith("ERROR"):
        print(f"found files with error {result}")

print("scanning completed")
    