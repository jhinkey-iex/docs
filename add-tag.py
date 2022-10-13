from pathlib import Path

def main():
    files = sorted(Path("test").rglob("*.html"))
    for fname in files:
        print(fname)
        addTag(fname)
    # fname = "developer-tools.html"
    

def addTag(fname):
    delim = "</head>"
    insert = "\n    <foo>\n      FOO\n    </foo>\n  "
    file = open(fname, "rt")
    str = file.read()
    file.close()

    head_split = str.split(delim, 1)
    new_str = head_split[0] + insert + delim + head_split[1]
    file = open(fname, "wt")
    file.write(new_str)
    file.close()

if __name__ == "__main__":
    main()