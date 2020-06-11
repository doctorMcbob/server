"""
controller to be used in server.py
"""

def resolve(text):
    print(text)
    # example:
    # remember youtu.be/somelink tag tag tag...
    if text.startswith("remember"):
        text = text.split()
        link = text[1]
        tags = text[2:]
        with open("memories.txt", "a") as f:
            f.write(repr(link) + ":" + repr(tags))

if __name__ == """__main__""":
    resolve(input())
