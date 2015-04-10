from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    imdb_id = models.CharField(max_length=9, blank=True, null=True)
    youtube_link = models.CharField(max_length=200, blank=True, null=True)
    picture = models.CharField(max_length=300, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def rating(self):
        score = 0
        ratings = Rating.objects.filter(show=self.id)
        if len(ratings) == 0:
            return "-"
        for rating in ratings:
            score += rating.score
        score /= len(ratings)
        return score

    def rating_count(self):
        return len(Rating.objects.filter(show=self.id))

    def __str__(self):
        return self.name


class Rating(models.Model):
    score_choices = (
        (0, '0 - grottig'),
        (1, '1 - schlecht'),
        (2, '2 - mittelmäßig'),
        (3, '3 - nett'),
        (4, '4 - gut'),
        (5, '5 - sehr gut'),
        (6, '6 - ausgezeichnet')
    )
    score = models.IntegerField(choices=score_choices, default=3)
    message = models.CharField(max_length=200, blank=True, null=True)
    show = models.ForeignKey(Show)

    def __str__(self):
        return self.score + " Points for show: " + self.show.name