from scripts import get_table, get_data, save_data_to_csv

url = "https://en.wikipedia.org/wiki/ISO_4217"

table = get_table(url=url)
data = get_data(table=table)

save_data_to_csv(data=data)
