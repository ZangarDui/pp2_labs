import re

def parse_receipt(text):
    items = []
    total_price = 0
    
    pattern = re.compile(r"(.*?)\n(\d+,\d{3}) x ([\d\s]+),?(\d{2})")
    matches = pattern.findall(text)
    
    for match in matches:
        item_name = match[0].strip()
        quantity = int(match[1].replace(',', ''))
        price = int(match[2].replace(' ', '')) * 100 + int(match[3])
        total = quantity * price / 100
        total_price += total
        items.append((item_name, quantity, price / 100, total))
    
    return items, total_price

receipt_text = """ДУБЛИКАТ
Филиал ТОО EUROPHARMA Астана
...
ИТОГО:
18 009,00
..."""  

items, total = parse_receipt(receipt_text)

print("Тауарлар:")
for item in items:
    print(f"{item[0]}: {item[1]} шт x {item[2]:.2f} = {item[3]:.2f} KZT")

print(f"\nЖалпы сомасы: {total:.2f} KZT")
