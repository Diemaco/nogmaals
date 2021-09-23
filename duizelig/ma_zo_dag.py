dagen = [
    'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zonderdag'
]

dag = input("Kies een dag (ma,di,wo,do,vr,za,zo)")

for i in dagen:
    print(i)
    if i.startswith(dag):
        break
