import pandas as pd
data = {
        'id': [9999999,9999998],
        'title': ['Fifty', 'Sixty'],
        'tags': ['abc', 'xyz']
    }
df_add = pd.DataFrame(data)
print(df_add)