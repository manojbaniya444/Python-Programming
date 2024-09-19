import shelve

db = shelve.open("./db/persondb")
for key in db:
    print(key, "=>\n ", db[key])