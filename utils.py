import json

def desc_columns(df, dictionary_desc):
    df_temp = df
    for i, j in dictionary_desc.items():
        for k, l in j.items():
            from_value = k
            to_value   = l
            df_temp[i].replace(from_value, to_value, inplace=True)
    return df_temp

def read_json_dict(path):
    #SINASC+-+Estrutura.pdf
    with open(f"{path}", 'r', encoding='utf-8') as f:
        desc = json.load(f)
    return desc