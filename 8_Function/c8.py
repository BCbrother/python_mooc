#可变的关键字参数

def city_tem(**param):
    print(type(param))
    print(param)
    '''
    如何快速用最简洁的形式遍历整个字典
    '''
    for key,value in param.items():
        print(key,':',value)

d = {'Beijing':'0c','Wuhu':'4c','Shanghai':'3c'}
city_tem(**d)