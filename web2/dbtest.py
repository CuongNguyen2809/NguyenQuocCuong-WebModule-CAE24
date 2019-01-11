# Update , Delete
# Atomic => id 
import mlab
from models.character import Character

mlab.connect()

character = Character.objects().with_id("5c34a8045723e92bd402f62f")
# character.update(set__rate=10, set__name="Super Super man")
# character.reload()
# print(character.rate)

character.delete()

# 1. update
# 1.1 Read document
# 1.2 Update document

# 2. Delete
# 2.1 Read document
#  2.2 Delete document
