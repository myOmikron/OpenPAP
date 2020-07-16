import re

import requests
from bs4 import BeautifulSoup
from monster.models import *

root_url = "https://dnd-5e.herokuapp.com/monsters/"


def main():
    html = requests.get(root_url).text
    parsed_html = BeautifulSoup(html, features="html.parser")
    list_entries_html = parsed_html.find("ul", attrs={"id": "monsters"}).find_all("a")
    list_entries = [entry["href"] for entry in list_entries_html]
    for entry in list_entries:
        monster_html = requests.get(root_url + entry).text
        monster_parsed_html = BeautifulSoup(monster_html, features="html.parser")
        monster_box = monster_parsed_html.find("div", attrs={"class": "monster-box"})
        m_name = monster_box.find("h1").text
        if len(Monster.objects.filter(name=m_name)) == 0:
            m = Monster()
            m.name = monster_box.find("h1").text
            m.save()
        else:
            m = Monster.objects.get(name=m_name)
        print(m.name)
        p_list = monster_box.find_all("p")

        size_tmp = p_list[0].text.split(" ")[0].lower()
        m.size = Size.objects.get(size=size_tmp)

        race_temp = " ".join(p_list[0].text.split(" ")[1:]).split(",")[0]
        if "(" in race_temp:
            race_name = race_temp.split(" ")[0]
            race_comment = "".join(race_temp.split(" ")[-1][1:])
            if race_comment.endswith(")"):
                race_comment = race_comment[:-1]
            if len(Race.objects.filter(race=race_name, comment=race_comment)) == 0:
                r = Race()
                r.race = race_name
                r.comment = race_comment
                r.save()
            m.race = Race.objects.get(race=race_name, comment=race_comment)
        else:
            if len(Race.objects.filter(race=race_temp, comment="")) == 0:
                r = Race()
                r.race = race_temp
                r.save()
            m.race = Race.objects.get(race=race_temp, comment="")

        al = p_list[0].text.split(",")[-1].lower().strip()
        if len(Alignment.objects.filter(alignment=al)) == 0:
            a = Alignment()
            a.alignment = al
            a.save()
        m.alignment = Alignment.objects.get(alignment=al)
        m.armor_class = int(p_list[1].text.split(" ")[2:][0])
        m.armor_description = " ".join(p_list[1].text.split(" ")[3:]).strip("(").rstrip(")")
        m.hit_points = int(p_list[2].text.split(" ")[2:][0])
        m.hit_points_alt = " ".join(p_list[2].text.split(" ")[3:]).split("(")[1].rstrip(")")
        m.speed_base = " ".join(p_list[3].text.split(" ")[1:]).split(",")[0].split(" ")[0]
        if len(" ".join(p_list[3].text.split(" ")[1:]).split(",")) > 2:
            m.speed_alt = ", ".join(" ".join(p_list[3].text.split(" ")[1:]).split(", ")[1:])

        li_list = monster_box.find_all("li")
        m.strength = li_list[0].text.split(" ")[1]
#        m.strength_mod = int(li_list[0].text.split(" ")[2][1:-1])
        m.dexterity = li_list[1].text.split(" ")[1]
#        m.dexterity_mod = int(li_list[1].text.split(" ")[2][1:-1])
        m.constitution = li_list[2].text.split(" ")[1]
#        m.constitution_mod = int(li_list[2].text.split(" ")[2][1:-1])
        m.intelligence = li_list[3].text.split(" ")[1]
#        m.intelligence_mod = int(li_list[3].text.split(" ")[2][1:-1])
        m.wisdom = li_list[4].text.split(" ")[1]
#        m.wisdom_mod = int(li_list[4].text.split(" ")[2][1:-1])
        m.charisma = li_list[5].text.split(" ")[1]
#        m.charisma_mod = int(li_list[5].text.split(" ")[2][1:-1])

        for p_element in p_list[4:]:
            if p_element.text.startswith("Saving Throws"):
                tmp = " ".join(p_element.text.split(" ")[2:])
                if "," in tmp:
                    tmp_list = tmp.split(", ")
                    for x in [item.split(" ") for item in tmp_list]:
                        if len(SavingThrow.objects.filter(attribute=x[0], value=int(x[1]))) == 0:
                            st = SavingThrow()
                            st.attribute = x[0]
                            st.value = int(x[1])
                            st.save()
                        m.saving_throws.add(SavingThrow.objects.get(attribute=x[0], value=int(x[1])))
                else:
                    if len(SavingThrow.objects.filter(attribute=tmp.split(" ")[0], value=int(tmp.split(" ")[1]))) == 0:
                        st = SavingThrow()
                        st.attribute = tmp.split(" ")[0]
                        st.value = int(tmp.split(" ")[1])
                        st.save()
                    m.saving_throws.add(SavingThrow.objects.get(attribute=tmp.split(" ")[0], value=int(tmp.split(" ")[1])))

            elif p_element.text.startswith("Senses"):
                tmp = " ".join(p_element.text.split(" ")[1:])
                if "," in tmp:
                    for x in tmp.split(","):
                        if len(Sense.objects.filter(sense=x)) == 0:
                            s = Sense()
                            s.sense = x
                            s.save()
                        m.senses.add(Sense.objects.get(sense=x))
                else:
                    if len(Sense.objects.filter(sense=tmp)) == 0:
                        s = Sense()
                        s.sense = tmp
                        s.save()
                    m.senses.add(Sense.objects.get(sense=tmp))
            elif p_element.text.startswith("Languages"):
                tmp = " ".join(p_element.text.split(" ")[1:])
                if "," in tmp:
                    for language in tmp.split(","):
                        if len(Language.objects.filter(language=language)) == 0:
                            l = Language()
                            l.language = language
                            l.save()
                            m.languages.add(l)
                        else:
                            m.languages.add(Language.objects.get(language=language))
                else:
                    if tmp != "-":
                        if len(Language.objects.filter(language=tmp)) == 0:
                            l = Language()
                            l.language = tmp
                            l.save()
                        m.languages.add(Language.objects.get(language=tmp))
            elif p_element.text.startswith("Challenge"):
                challenge_tmp = p_element.text.split(" ")[1:]
                if challenge_tmp[0] == "1/8":
                    challenge_rating = 0.125
                elif challenge_tmp[0] == "1/4":
                    challenge_rating = 0.25
                elif challenge_tmp[0] == "1/2":
                    challenge_rating = 0.5
                else:
                    challenge_rating = challenge_tmp[0]
                m.challenge = float(challenge_rating)
                m.challenge_xp = int(challenge_tmp[1].strip("(").replace(",", ""))
            elif p_element.text.startswith("Skills"):
                tmp = " ".join(p_element.text.split(" ")[1:])
                if "," in tmp:
                    for x in [re.split(r"(?!\w)\s[+]", item) for item in tmp.split(", ")]:
                        if len(Skill.objects.filter(skill=x[0], value=int(x[1]))) == 0:
                            s = Skill()
                            s.skill = x[0]
                            s.value = int(x[1])
                            s.save()
                        m.skills.add(Skill.objects.get(skill=x[0], value=int(x[1])))
                else:
                    if len(Skill.objects.filter(skill=tmp.split(" ")[0], value=int(tmp.split(" ")[1]))) == 0:
                        s = Skill()
                        s.skill = tmp.split(" ")[0]
                        s.value = int(tmp.split(" ")[1])
                        s.save()
                    m.skills.add(Skill.objects.get(skill=tmp.split(" ")[0], value=int(tmp.split(" ")[1])))
            elif p_element.text.startswith("Damage Immunities"):
                tmp = " ".join(p_element.text.split(" ")[2:]).lower()
                if tmp.lower().startswith("one of the following: "):
                    tmp = "".join(tmp[22:])
                if ";" in tmp:
                    x = tmp.split("; ")
                    if len(DamageImmunity.objects.filter(damage_immunity=x[1])) == 0:
                        di = DamageImmunity()
                        di.damage_immunity = x[1].lower()
                        di.save()
                    m.damage_immunities.add(DamageImmunity.objects.get(damage_immunity=x[1]))
                    for y in x[0].split(", "):
                        if y.startswith("or "):
                            y = "".join(y[3:])
                        if y.startswith("and "):
                            y = "".join(y[4:])
                        if len(DamageImmunity.objects.filter(damage_immunity=y)) == 0:
                            di = DamageImmunity()
                            di.damage_immunity = y.lower()
                            di.save()
                        m.damage_immunities.add(DamageImmunity.objects.get(damage_immunity=y))
                elif "," in tmp:
                    for x in tmp.split(", "):
                        if x.startswith("or "):
                            x = "".join(x[3:])
                        if x.startswith("and "):
                            x = "".join(x[4:])
                        if len(DamageImmunity.objects.filter(damage_immunity=x)) == 0:
                            di = DamageImmunity()
                            di.damage_immunity = x.lower()
                            di.save()
                        m.damage_immunities.add(DamageImmunity.objects.get(damage_immunity=x))
                else:
                    if len(DamageImmunity.objects.filter(damage_immunity=tmp)) == 0:
                        di = DamageImmunity()
                        di.damage_immunity = tmp.lower()
                        di.save()
                    m.damage_immunities.add(DamageImmunity.objects.get(damage_immunity=tmp))
            elif p_element.text.startswith("Damage Resistances"):
                tmp = " ".join(p_element.text.split(" ")[2:]).lower()
                if tmp.lower().startswith("one of the following: "):
                    tmp = "".join(tmp[22:])
                if ";" in tmp:
                    x = tmp.split("; ")
                    if len(DamageResistance.objects.filter(damage_resistance=x[1])) == 0:
                        di = DamageResistance()
                        di.damage_resistance = x[1].lower()
                        di.save()
                    m.damage_resistances.add(DamageResistance.objects.get(damage_resistance=x[1]))
                    for y in x[0].split(", "):
                        if y.startswith("or "):
                            y = "".join(y[3:])
                        if y.startswith("and "):
                            y = "".join(y[4:])
                        if len(DamageResistance.objects.filter(damage_resistance=y)) == 0:
                            di = DamageResistance()
                            di.damage_resistance = y.lower()
                            di.save()
                        m.damage_resistances.add(DamageResistance.objects.get(damage_resistance=y))
                elif "," in tmp:
                    for x in tmp.split(", "):
                        if x.startswith("or "):
                            x = "".join(x[3:])
                        if x.startswith("and "):
                            x = "".join(x[4:])
                        if len(DamageResistance.objects.filter(damage_resistance=x)) == 0:
                            di = DamageResistance()
                            di.damage_resistance = x.lower()
                            di.save()
                        m.damage_resistances.add(DamageResistance.objects.get(damage_resistance=x))
                else:
                    if len(DamageResistance.objects.filter(damage_resistance=tmp)) == 0:
                        di = DamageResistance()
                        di.damage_resistance = tmp.lower()
                        di.save()
                    m.damage_resistances.add(DamageResistance.objects.get(damage_resistance=tmp))
            elif p_element.text.startswith("Condition Immunities"):
                tmp = " ".join(p_element.text.split(" ")[2:]).lower()
                if tmp.lower().startswith("one of the following: "):
                    tmp = "".join(tmp[22:])
                if ";" in tmp:
                    x = tmp.split("; ")
                    if len(ConditionImmunity.objects.filter(condition_immunity=x[1])) == 0:
                        di = ConditionImmunity()
                        di.condition_immunity = x[1].lower()
                        di.save()
                    m.condition_immunities.add(ConditionImmunity.objects.get(condition_immunity=x[1]))
                    for y in x[0].split(", "):
                        if y.startswith("or "):
                            y = "".join(y[3:])
                        if y.startswith("and "):
                            y = "".join(y[4:])
                        if len(ConditionImmunity.objects.filter(condition_immunity=y)) == 0:
                            di = ConditionImmunity()
                            di.condition_immunity = y.lower()
                            di.save()
                        m.condition_immunities.add(ConditionImmunity.objects.get(condition_immunity=y))
                elif "," in tmp:
                    for x in tmp.split(", "):
                        if x.startswith("or "):
                            x = "".join(x[3:])
                        if x.startswith("and "):
                            x = "".join(x[4:])
                        if len(ConditionImmunity.objects.filter(condition_immunity=x)) == 0:
                            di = ConditionImmunity()
                            di.condition_immunity = x.lower()
                            di.save()
                        m.condition_immunities.add(ConditionImmunity.objects.get(condition_immunity=x))
                else:
                    if len(ConditionImmunity.objects.filter(condition_immunity=tmp)) == 0:
                        di = ConditionImmunity()
                        di.condition_immunity = tmp.lower()
                        di.save()
                    m.condition_immunities.add(ConditionImmunity.objects.get(condition_immunity=tmp))
        m.tag = Tag.objects.get(tag="monster")
        m.save()
