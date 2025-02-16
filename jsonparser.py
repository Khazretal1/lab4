import json 

with open('sample-data.json', 'r') as file:
    data = json.load(file)
    
output = ""

output += "Interface status\n"
output += "================================================================================\n"
output += "DN                                                 Description           Speed    MTU  \n"
output += "-------------------------------------------------- --------------------  ------  ------\n"

for imdata in data["imdata"]:
    attributes = imdata["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")

    output += dn + " " * (51 - len(dn))
    output += description + " " * (21 - len(description))
    output += speed + " " * (10 - len(speed))
    output += mtu + " " * (6 - len(mtu)) + "\n"

print(output)