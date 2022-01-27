people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]
def ans(target):
    for i in people:
        if i['name'] == target:
            return print(i['age'])
        else:
            return print('해당하는 사람이 없습니다')

ans('ben')