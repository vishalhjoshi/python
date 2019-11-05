''' Construct programm using random function '''



import random

first_names = ['POOJA', 'KAJAL', 'PRADIP', 'AKSHAY', 'CHETAN', 'KUNJAN', 'SHUBHAM', 'SOJWAL', 'GAJANAN', 'RIZWAN', 'SUDESH', 'GAURI', 'NAMRATA', 'KIRTI', 'ARCHANA', 'MINAXI', 'PRAVIN', 'PRADIP', 'POOJA', 'ABHIJIT', 'PRIYANKA']

last_names = ['MORE', 'BHINGARE', 'KHAN', 'CHOPADE', 'BHARAMBE', 'RANE', 'CHAUDHARI', 'SARODE', 'PATIL', 'BHOLE', 'MARATHE', 'SHAIKH', 'GHOGARE', 'KOLHE', 'NHAVI', 'ZOPE', 'TANWAR', 'INGALE', 'GHULE', 'BARI', 'BHOI', 'PETHE', 'DESHMUKH', 'WANI', 'MAHAJAN', 'JAIN', 'SONAR']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Shengola', 'Lake', 'Hill']

fake_cities = ['Jamner', 'Jalgaon', "Bhusawal", 'Pachora', 'Shengola', 'Mumbai', 'Nashik', 'Chennai', 'Ahemdabad', 'Kolkata', 'New Delhi', 'Jipur', 'Luknow', 'Prayagraj', 'Wadodra', 'Madurai', 'Ranchi', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Gaziabad', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['MH', 'MP', 'UP', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'+91-{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(400000, 499999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')