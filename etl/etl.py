def transform(legacy_data):
    out = {}
    for l in legacy_data.items():
        for k in l[1]:
            out = out | {k.lower():l[0]}
    return out


