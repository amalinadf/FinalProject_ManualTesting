p = "postman/Assignment4_AmalinaDwiFirzanah.postman_collection.json"
s = open(p).read()

fixes = {
    '"key": "demoEmail",\n      "value": "standard_user@example.com"': '"key": "demoEmail",\n      "value": ""',
    '"key": "demoPassword",\n      "value": "script_sauce"': '"key": "demoPassword",\n      "value": ""',
}

for old, new in fixes.items():
    if old in s:
        s = s.replace(old, new)
        print("blanked:", old.splitlines()[0])
    else:
        print("skip:", old.splitlines()[0])

open(p, "w").write(s)
