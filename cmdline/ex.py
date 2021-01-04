import sys

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-c" in opts:
    print(list(arg.capitalize() for arg in args ))
elif "-u" in opts:
    print(list(arg.upper() for arg in args ))
elif "-l" in opts:
    print(list(arg.lower() for arg in args ))
else:
    raise SystemExit(f"Usage :{sys.argv[0]} <-i| -u | -l> arguments")
