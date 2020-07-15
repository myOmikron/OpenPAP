from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, FloatField, ManyToManyField


class Size(models.Model):
    size = CharField(max_length=255, unique=True)
    internal_size = IntegerField(default=0, unique=True)

    def __str__(self):
        return self.size

    def __lt__(self, other):
        return self.internal_size < other

    def __gt__(self, other):
        return self.internal_size > other

    def __eq__(self, other):
        return self.internal_size == other


class Race(models.Model):
    race = CharField(max_length=255)
    comment = CharField(max_length=255)

    def __str__(self):
        return " ".join([self.race, self.comment])


class Alignment(models.Model):
    alignment = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.alignment


class Language(models.Model):
    language = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.language


class Monster(models.Model):
    name = CharField(max_length=255, default="", unique=True)

    size = ForeignKey(Size, on_delete=CASCADE)
    race = ForeignKey(Race, on_delete=CASCADE)
    alignment = ForeignKey(Alignment, on_delete=CASCADE)

    armor_class = IntegerField(default=10)
    armor_description = CharField(max_length=255, blank=True)
    hit_points = IntegerField(default=4)
    hit_points_alt = CharField(max_length=255, blank=True)
    speed_base = IntegerField(default=30, blank=True)
    speed_alt = CharField(max_length=255, blank=True)

    strength = IntegerField(default=10)
    dexterity = IntegerField(default=10)
    constitution = IntegerField(default=10)
    intelligence = IntegerField(default=10)
    wisdom = IntegerField(default=10)
    charisma = IntegerField(default=10)

    saving_throws = {}
    skills = []
    senses = []
    languages = ManyToManyField(Language)
    challenge = FloatField(default=1)
    challenge_xp = IntegerField(default=10)
    attacks = []

    actions = []

    def __str__(self):
        return self.name
