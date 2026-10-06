# You can remove 'pass' when you start writing the class.
# Read README.md for exactly what each class must do.
class BusCard:
   def __init__(self, owner ):
      self.owner = owner
      self.balance = 0
      self.trips = 0

   def top_up(self,amount):
      if amount<=0:
         return False
      else:
         self.balance+=amount
         return True
   def pay(self, fare):
      if self.balance >= fare:
         self.balance-=fare
         self.trips+=1
         return True
      else:
         return False

class Student:
   def __init__(self, name):
      self.name = name
      self.grades = []
   def add_grade(self, score):
      if score>=0 and score<=100:
         self.grades.append(score)
         return True
      else:
         return False
   def average(self):
      if len(self.grades)!= 0:
         a=sum(self.grades) / len(self.grades)
         return round(a,1)
      else:
         return 0
   def highest(self):
      if len(self.grades)!= 0:
         max=0
         for i in self.grades:
            if i>max:
               max=i
         return max
      else:
         return None





class Song:
   def __init__(self, title, artist, seconds):
      self.title=title
      self.artist=artist
      self.seconds=seconds
   def length(self):
      min=str(self.seconds//60)
      sec=str(self.seconds%60)
      if len(sec)==1:
         return f"{min}:0{sec}"
      else:
         return f"{min}:{sec}"
class Playlist:
   def __init__(self,name):
      self.name=name
      self.songs=[]
   def add_song(self, Song):
      self.songs.append(Song)
   def count(self):
      return len(self.songs)
   def total_seconds(self):
      sum=0
      for i in range(len(self.songs)):
          sum+=self.songs[i].seconds
      return sum
   def longest_song(self):
      if len(self.songs)==0:
         return None
      else:
         max=0
         for i in range(len(self.songs)):
            if max< self.songs[i].seconds:
               max=self.songs[i].seconds
         for i in range(len(self.songs)):
            if self.songs[i].seconds==max:
               return self.songs[i]


   def songs_by(self, artist ):
      save = []
      for i in range(len(self.songs)):
         if self.songs[i].artist == artist:
            save.append(self.songs[i].title)
      return save
