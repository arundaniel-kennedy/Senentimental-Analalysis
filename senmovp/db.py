from model import db,data

db.create_all()

glady = data("glady", 7)
ceasar = data("ceasar", 3)

db.session.add_all([glady,ceasar])

db.session.commit()

print(glady.id)
print(ceasar.id)
