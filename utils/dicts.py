# файл dicts.py
def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение
    default.
    """
    if key not in collection.keys():
        return default
    return collection[key]


#print(get_val({"vcs": "mercurial"}, "vcs"))



#data = {"vcs": "mercurial"}
# print(get_val(data, "vcs"))
# #'mercurial'
# get_val(data, "vcs", "git")
# #'mercurial'
# data = {}
# print(get_val({}, "vcs", "git"))
# #'git'
# print(get_val({}, "vcs", "bazaar"))
# #'bazaar'