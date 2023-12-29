import sys

#Task01
student={"name":"Miguel", "academic_year":2012}

#Task02
value1={"name":"Web Development", "credits":5, "grade":'A'}
value2={"name":"Network and System Administration", "credits":2, "grade":'E'}
value3={"name":"Java", "credits":3, "grade":'B'}
unitsValues=[value1, value2, value3]
student["units"]=unitsValues

#Task03
grade_weight_mapping={'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

def task03(d):
    sum=0
    cred=0
    for e in d["units"]:
        sum+=(grade_weight_mapping[e['grade']]*e['credits'])
        cred+=e['credits']
    d["total_credits"]=sum
    d["grade_point_average"]=sum/cred

#Task04
group=[
    {
        'name': 'Miguel',
        'academic_year': 2021,
        'units':[
            {
            'name': 'Web Development',
            'credits': 5,
            'grade': 'A'
            },
            {
            'name': 'Network and System Administration',
             'credits': 2,
             'grade': 'E'
             },
             {
            'name': 'Java',
            'credits': 3,
            'grade': 'B'
            }],
    },
    {
        'name': 'Maria',
        'academic_year': 2023,
        'units':[
            {
            'name': 'Web Development',
            'credits': 5,
            'grade': 'C'
            },
            {
            'name': 'Network and System Administration',
             'credits': 2,
             'grade': 'E'
             },
             {
            'name': 'Java',
            'credits': 3,
            'grade': 'D'
            }],
    },
    {
        'name': 'Paulo',
        'academic_year': 2023,
        'units':[
            {
            'name': 'Web Development',
            'credits': 5,
            'grade': 'A'
            },
            {
            'name': 'Network and System Administration',
             'credits': 2,
             'grade': 'A'
             },
             {
            'name': 'Java',
            'credits': 3,
            'grade': 'B'
            }],
    },
]


def takeName(d):
    return d['name']

#group.sort(key=takeName)
#print(group)

def takeGPA(d):
    return d['grade_point_average']

#group.sort(reverse=True,key=takeGPA)
#print(group)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                print(student)
            case '02':
                print(student)
            case '03':
                task03(student)
                print(student)
            case '04':
                for e in group:
                    task03(e)
                group.sort(key=takeName)
                print(group)
                group.sort(reverse=True,key=takeGPA)
                print(group)