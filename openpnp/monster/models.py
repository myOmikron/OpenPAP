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
    comment = CharField(max_length=255, default="")

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


class Action(models.Model):
    action = CharField(max_length=255, default="")
    description = CharField(max_length=2048, default="")

    def __str__(self):
        return self.action


class Sense(models.Model):
    sense = CharField(max_length=255, default="")

    def __str__(self):
        return self.sense


class Skill(models.Model):
    skill = CharField(max_length=255, default="")
    value = IntegerField(default=0)

    def __str__(self):
        return self.skill


class SavingThrow(models.Model):
    attribute = CharField(max_length=255, default="")
    value = IntegerField(default=0)

    def __str__(self):
        return self.attribute


class DamageImmunity(models.Model):
    damage_immunity = CharField(max_length=255, default="")

    def __str__(self):
        return self.damage_immunity


class DamageResistance(models.Model):
    damage_resistance = CharField(max_length=255, default="")

    def __str__(self):
        return self.damage_resistance


class ConditionImmunity(models.Model):
    condition_immunity = CharField(max_length=255, default="")

    def __str__(self):
        return self.condition_immunity


class Tag(models.Model):
    tag = CharField(max_length=255, default="")

    def __str__(self):
        return self.tag


class Monster(models.Model):
    name = CharField(max_length=255, default="", unique=True)

    tag = ForeignKey(Tag, on_delete=CASCADE, null=True)

    size = ForeignKey(Size, on_delete=CASCADE, null=True)
    race = ForeignKey(Race, on_delete=CASCADE, null=True)
    alignment = ForeignKey(Alignment, on_delete=CASCADE, null=True)

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

    saving_throws = ManyToManyField(SavingThrow)
    skills = ManyToManyField(Skill)
    senses = ManyToManyField(Sense)
    languages = ManyToManyField(Language)
    damage_resistances = ManyToManyField(DamageResistance)
    damage_immunities = ManyToManyField(DamageImmunity)
    condition_immunities = ManyToManyField(ConditionImmunity)
    challenge = FloatField(default=1)
    challenge_xp = IntegerField(default=10)
    attacks = []

    actions = ManyToManyField(Action)

    def __str__(self):
        return self.name
