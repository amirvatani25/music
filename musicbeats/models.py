import uuid
from users.models import Profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=290)
    singer_image=models.ImageField(upload_to='singers/',null=True,blank=True,default="profiles/user-defualt.png")
    birthday = models.CharField(max_length=11,blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True)
    pishnahadi_single = models.BooleanField(blank=True, default=False)
    pishnahadi_homepage = models.BooleanField(blank=True, default=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'خواننده'
        verbose_name_plural = 'خواننده ها'


class Album(models.Model):
    name = models.CharField(max_length=2000)
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True,blank=True)
    image = models.ImageField(upload_to='album_images/')
    pishnahadi_single = models.BooleanField(blank=True,default=False)
    pishnahadi_homepage = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField('Tag', blank=True)
    tarikh_enteshar = models.CharField(max_length=20,blank=True,null=True)
    category = models.ManyToManyField('Category', blank=True)
    total_vote = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'آلبوم'
        verbose_name_plural = 'آلبوم ها'






class Song(models.Model):
    name = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='song_images/',null=True,blank=True )
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True,blank=True)
    song128 = models.FileField(upload_to='musics/')
    song320 = models.FileField(upload_to='musics/')
    songfacp = models.FileField(upload_to='musics/')
    album = models.ForeignKey(Album,null=True,blank=True,on_delete=models.SET_NULL)
    tarikh_enteshar = models.CharField(max_length=20,blank=True,null=True)
    tags = models.ManyToManyField('Tag',blank=True)
    category = models.ManyToManyField('Category',blank=True)
    total_vote = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0 , null=True , blank=True)
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True , unique=True , editable=False)

    def count_song_of_album(album):
        return Song.objects.filter(album_id=album).count()



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'آهنگ'
        verbose_name_plural = 'آهنگ ها'
        ordering = ['total_vote']




class Review (models.Model):
    VOTE_TYPE = (
        ('up','up vote'),
        ('down' , 'down vote')
    )
    owner = models.ForeignKey(Profile , on_delete=models.CASCADE,null=True)
    song = models.ForeignKey(Song , on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True ,unique=True, editable=False)



    class Meta:
        unique_together = [['owner', 'song']]
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ['create']

    def __str__(self):
        return self.value


class Tag (models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True , unique=True , editable=False)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'



class Category (models.Model):
    name = models.CharField(max_length=190)
    category_image = models.ImageField(upload_to='category/',null=True,blank=True,default="profiles/user-defualt.png")
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'کتگوری'
        verbose_name_plural = 'کتگوری ها'



class Playlist(models.Model):
    list_name=models.CharField(max_length=100,null=True,blank=True)
    owner=models.ForeignKey(Profile, null=True, blank=True,on_delete=models.CASCADE)
    playlist_image= models.ImageField(upload_to='playlist/',null=True,blank=True,default="profiles/user-defualt.png")
    songs=models.ManyToManyField(Song,blank=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.list_name

    class Meta:
        verbose_name = 'پلی لیست'
        verbose_name_plural = 'پلی لیست ها'



class AdminPlaylist(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='adminplaylists/',null=True,blank=True,default="profiles/user-defualt.png")
    song = models.ManyToManyField(Song,blank=True,)
    album = models.ManyToManyField(Album,blank=True)
    pishnahadi_single = models.BooleanField(blank=True,default=False)
    pishnahadi_homepage = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField('Tag',blank=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'پلی‌لیست ادمین‌'
        verbose_name_plural = 'پلی‌لیست ادمین‌ها'




class Hesohal(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    hesohal_image=models.ImageField(upload_to='hesohal/',null=True,blank=True,default="profiles/user-defualt.png")
    song = models.ManyToManyField(Song,blank=True,)
    album = models.ManyToManyField(Album,blank=True)
    playlist = models.ManyToManyField(AdminPlaylist,blank=True)
    pishnahadi_single = models.BooleanField(blank=True,default=False)
    pishnahadi_homepage = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField('Tag',blank=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'حس و حال'
        verbose_name_plural = 'حس و حال ها'
