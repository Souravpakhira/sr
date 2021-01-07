from django.db import models

# Create your models here.


class students(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=gender_choices)
    staff = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class srs(models.Model):
    childs_name = models.ForeignKey(students, on_delete=models.CASCADE)
    childs_age_month = models.IntegerField()
    childs_age_year = models.IntegerField()
    raters_name = models.CharField(max_length=250)
    date_of_rating = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.childs_name.name


class raw_score(models.Model):
    childs_name = models.OneToOneField(srs, on_delete=models.CASCADE)
    Awr = models.IntegerField()
    Cog = models.IntegerField()
    Com = models.IntegerField()
    Mot = models.IntegerField()
    RRB = models.IntegerField()
    total_raw_score = models.IntegerField(default=0)
    total_raw_score.help_text = "Don't insert any value"

    def __str__(self):
        return f'{self.childs_name}={self.total_raw_score}'

    def save(self, *args, **kwargs):
        self.total_raw_score = self.Awr + self.Cog + self.Com + self.Mot + self.RRB
        super(raw_score, self).save(*args, **kwargs)


class t_score(models.Model):
    childs_name = models.OneToOneField(srs, on_delete=models.CASCADE)
    Awr = models.IntegerField()
    Cog = models.IntegerField()
    Com = models.IntegerField()
    Mot = models.IntegerField()
    RRB = models.IntegerField()
    total_t_score = models.IntegerField(default=0)
    total_t_score.help_text = "Don't insert any value"

    def __str__(self):
        return f'{self.childs_name}={self.total_t_score}'

    def save(self, *args, **kwargs):
        self.total_t_score = self.Awr + self.Cog + self.Com + self.Mot + self.RRB
        super(t_score, self).save(*args, **kwargs)
