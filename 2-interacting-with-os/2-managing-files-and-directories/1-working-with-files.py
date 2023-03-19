import os

os.remove("novel.txt")
os.rename("first_draft.txt", "finished_draft.txt")
print(os.path.exists("finished_masterpiece.txt"))