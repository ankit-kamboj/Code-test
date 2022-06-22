def traverse_nested_json(njson, jkey):
    return extract(njson, jkey, 0, [])
    

def extract(njson, jkey, count, newstring):
    key = jkey[count]
    if count + 1 < len(jkey):
        if key in njson.keys():
            extract(njson.get(key), jkey, count + 1, newstring)
        else:
            newstring.append(None)

    if count + 1 == len(jkey):
        newstring.append(njson.get(key, None))
    
    return newstring


json_key={"x":{"y":{"z":{"a"}}}}
traverse_nested_json(json_key, ['x','y'])
