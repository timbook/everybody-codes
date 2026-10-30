import re
import numpy as np
import pandas as pd

raw = open('data/input1.txt').read()

pattern = r'id=(\d+) quest=(\d+) part=(\d+) time=(\d+)'
data_tup = re.findall(pattern, raw)
df = pd.DataFrame(
    data_tup,
    columns=['id', 'quest', 'part', 'time']
).astype(int)

df_time = df.groupby('id', as_index=False).time.sum().sort_values('time')
df_time['rank'] = np.arange(df_time.shape[0]) + 1
df_time['checksum'] = df_time['rank'] * df_time['time']
sol = df_time.checksum.sum()
print(f'A ::: {sol}')

# ========================================================================

raw = open('data/input2.txt').read()

pattern = r'id=(\d+) quest=(\d+) part=(\d+) time=(\d+)'
data_tup = re.findall(pattern, raw)
df = pd.DataFrame(
    data_tup,
    columns=['id', 'quest', 'part', 'time']
).astype(int)

df_time_parts = (
    df
    .groupby('id')
    .agg(
        n=('part', 'count'),
        time=('time', 'sum')
    )
    .sort_values(['n', 'time'], ascending=[False, True])
)

df_time_parts['rank'] = np.arange(df_time_parts.shape[0]) + 1
df_time_parts['checksum'] = df_time_parts['rank']*df_time_parts['time']
sol = df_time_parts.checksum.sum()
print(f'B ::: {sol}')

# ========================================================================

raw = open('data/input3.txt').read()

pattern = r'id=(\d+) quest=(\d+) part=(\d+) time=(\d+)'
data_tup = re.findall(pattern, raw)
df = pd.DataFrame(
    data_tup,
    columns=['id', 'quest', 'part', 'time']
).astype(int)
df['points_avail'] = df.part.map({1: 50, 2: 100, 3: 150})
df['rolling_time'] = df.sort_values(['quest', 'part']).groupby(['id', 'quest'])['time'].cumsum()

def rank_quest_part(df):
    df_ranked = df.sort_values('time')
    df_ranked['rank'] = df.rolling_time.rank(method='min') - 1
    df_ranked['points'] = np.maximum(df_ranked['points_avail'] - df_ranked['rank'], 0)
    return df_ranked

df_res = (
    df
    .groupby(['quest', 'part'], as_index=False)
    .apply(rank_quest_part)
    .reset_index(drop=True)
    .groupby('id', as_index=False)
    .agg(points=('points', 'sum'))
    .sort_values('points', ascending=False)
)

df_res['rank'] = np.arange(df_res.shape[0]) + 1
df_res['checksum'] = df_res['rank']*df_res['points']
sol = df_res.checksum.sum()
# 5988609, but it was 5______
print(f'C ::: {sol}')
