def find_key_by_value(packages, value):
    result = []
    for key, val in packages.items():
        if value == val:
            result.append(key)
    return result

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    new_dic = {}
    for key, value in packages.items():
        new_dic[key] = []
        for v in value:
            if v in packages and v not in new_dic[key]:
                new_dic[key].append(v)
    result = []
    while new_dic:
        ready = sorted(find_key_by_value(new_dic, []))
        if len(ready) == 0:
            return []
        for i in range(len(ready)):
            key = ready[i]
            result.append(key)
            new_dic.pop(key)
            for item in new_dic.values():
                if key in item:
                    item.remove(key)
    return result

if __name__ == "__main__":
    print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
    print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
    print(package_dependency_resolver({}))
    print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
    print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))
            