# connect data base
import mlab 
from mongoengine import Document, StringField , IntField

mlab.connect()

# define model
class Movie(Document):
    title = StringField()
    image = StringField()
    link = StringField()
    rate = IntField()


#create data
# m = Movie(title="Bi đừng sợ",
#           image="http://via.placeholder.com/200x200",
#           link= "http://via.placeholder.com/200x200",
#           rate =10)
            
# m.save()
movie_list = Movie.objects(rate__gte=7, title__icontains="ThAi") #lazy Loading
for m in movie_list:
    
    print(m.title,m.rate)