f1 = open(r".\Files Used\Article.txt", "r")
s1 = f1.read()
s1 = s1.split()
s1 = " ".join(s1)
f2 = open(r"\Files Used\Space Replace.txt", "w")
f2.write(s1)
