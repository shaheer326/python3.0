student_data = {
    "id1": {"name": "sara", "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "david", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "suriya", "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "micheal", "class": "V", "subject_integration": "english, math, science"}
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)


test_dict = {'I': 2, 'am': 2, 'good': 2, 'at': 2, 'coding': 1}

print("the original dictionary is: ", test_dict)

K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1

print("the frequency of K is : " + str(res))


country_code = {'Pakistan': '0090', 'Australia': '0025', 'Nepal': '0977'}

print("Country code for Pakistan -")
print(country_code.get('Pakistan', 'Not found'))

print("Country code for Japan -")
print(country_code.get('Japan', 'Not found'))