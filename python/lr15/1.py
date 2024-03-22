import pandas as pd

letters = set("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
alphabet = sorted(letters)
alphabet = [f"{upper}{lower}" for upper, lower in zip(alphabet[:26], alphabet[26:])]

df = pd.DataFrame(alphabet, columns=['Letter'])
print("DataFrame з даними:")
print(df)

grouped_data = df.groupby(df['Letter'].str[0])
aggregated_data = grouped_data.size()
print("\nГрупування та агрегація даних:")
print(aggregated_data)
