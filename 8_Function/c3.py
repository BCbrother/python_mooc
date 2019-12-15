def _damage(skill1,skill2):
    damage1 = skill1 *3
    damage2 = skill2 *2 + 10
    return damage1,damage2

result_Dam1,result_Dam2 = _damage(10,8)
print(result_Dam1,result_Dam2)