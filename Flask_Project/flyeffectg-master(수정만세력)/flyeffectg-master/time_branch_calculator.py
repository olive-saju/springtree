
def get_time_branch(hour, minute):
    """
    Returns the time branch (子~亥) based on the given hour and minute.
    """
    time_branches = [
        ('子', 23, 31, 1, 30),
        ('丑', 1, 31, 3, 30),
        ('寅', 3, 31, 5, 30),
        ('卯', 5, 31, 7, 30),
        ('辰', 7, 31, 9, 30),
        ('巳', 9, 31, 11, 30),
        ('午', 11, 31, 13, 30),
        ('未', 13, 31, 15, 30),
        ('申', 15, 31, 17, 30),
        ('酉', 17, 31, 19, 30),
        ('戌', 19, 31, 21, 30),
        ('亥', 21, 31, 23, 30)
    ]

    for branch, start_hour, start_minute, end_hour, end_minute in time_branches:
        if (hour > start_hour or (hour == start_hour and minute >= start_minute)) and \
           (hour < end_hour or (hour == end_hour and minute <= end_minute)):
            return branch
    return None

def get_time_stem_branch(day_stem, time_branch):
    """
    Returns the time stem and branch based on the given day stem and time branch.
    """
    time_table = {
        '甲': ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥'],
        '乙': ['丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥'],
        '丙': ['戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥'],
        '丁': ['庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥'],
        '戊': ['壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥'],
        '己': ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥'],
        '庚': ['丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥'],
        '辛': ['戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥'],
        '壬': ['庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥'],
        '癸': ['壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']
    }

    branches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    time_index = branches.index(time_branch)
    return time_table[day_stem][time_index]

# Example Usage
# hour, minute = 4, 0
# time_branch = get_time_branch(hour, minute)
# day_stem = '癸'
# result = get_time_stem_branch(day_stem, time_branch)
# print(f"The time branch is {time_branch} and the time stem-branch is {result}")
