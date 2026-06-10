data = {
    'harish':{'status':True, 'python':98 , 'mysql':97 , 'flask':96},
    'sahith':{'status':True, 'python': 88, 'mysql': 87, 'flask':86},
    'vamsi':{'status':False, 'python': 68, 'mysql': 67, 'flask':66},
    'dinesh':{'status':True, 'python':48 , 'mysql':47 , 'flask':46},
    'rishi':{'status':True, 'python':38 , 'mysql':37 , 'flask':36},
    }
name = input()
if name in data:
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = total/3

        if avg > 90:
            print(f"congrats {name}, you got the first class")
        elif avg > 75:
            print(f" good {name}, keep it up")
        elif avg > 45:
            print(f"Work hard next time {name}")
        else:
            print(f"{name}, you are failed")
        

    else:
        print(f"{name} not attempted the exam.")

else:
    print(f"{name}'s data not found")
