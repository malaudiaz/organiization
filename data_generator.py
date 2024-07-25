from os import path, remove, getcwd
import random
import base64

n_members=4

def random_members():
    n_t = random.randint(1, n_members)
    members = []
    cont = 0
    while cont < n_t:
        random_member = random.randint(1, n_members)
        member_id = "members_" + str(random_member)
        if not member_id in members:
            members.append(member_id)
            cont += 1
            
    return members

def delete_file(file):
    if path.exists(file):
        remove(file)

def write_text(text, file):
    with open(file, "a") as f:
        f.write(text)

def format_random_members():
    members = random_members()
    member_string = "[(6,0,["
    for i in range(len(members)):
        member_string += "ref(\'" + members[i] + "\')"
        if i < len(members)-1:
            member_string += ","
    member_string += "])]"
    return member_string

def write_dev(line, file, model, fields, key):
    write_text(f"<record id='{key}_{line[0]}' model='{model}'>", file)
    i = 1
    for fld in fields:
        if fld != "flag":
            if fld != "members":
                write_text(f"<field name='{fld}'>{line[i]}</field>", file)
            else:
                write_text(f'<field name=\'{fld}\' eval=\"{format_random_members()}\"></field>', file)                
        else:
            image = open("images/" + line[1].strip() + ".png", "rb")
            b64_string = base64.b64encode(image.read()).decode("utf-8")
            write_text(f"<field name='{fld}'>{b64_string}</field>", file)

        i = i + 1

    write_text(f"</record>", file)


def xml_generator(source, demo_file, model, fields, key):
    delete_file(demo_file)
    write_text("<odoo><data>", demo_file)
    with open(source) as file:
        for line in file:
            line = line.split(",")
            write_dev(line, demo_file, model, fields, key)

    write_text("</data></odoo>", demo_file)


current_dir = getcwd() + "/extra-addons/organization/"

xml_generator(
    current_dir + "csv/country.csv",
    current_dir + "demo/country.xml",
    "organization.country",
    ["name", "initials"],
    "country",
)
xml_generator(
    current_dir + "csv/city.csv",
    current_dir + "demo/city.xml",
    "organization.city",
    ["name", "initials", "country_id"],
    "city",
)
xml_generator(
    current_dir + "csv/type.csv",
    current_dir + "demo/type.xml",
    "organization.type",
    ["name", "description"],
    "type",
)

xml_generator(
    current_dir + "csv/organization.csv",
    current_dir + "demo/organization.xml",
    "organization.organization",
    ["name", "initials", "type", "parent_id", "country_id", "city_id", "members"],
    "organization",
)

xml_generator(
    current_dir + "csv/members.csv",
    current_dir + "demo/members.xml",
    "organization.members",
    ["firts_name", "last_name", "phone", "email"],
    "members",
)
