import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print("User count:", len(lst))
for i in lst:
    print("Name:", i.find('name').text)
    print("Id:", i.find('id').text)
    print("Attribute:", i.get('x'))
