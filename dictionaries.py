
countries = {'Uganda': {'country_code': 'UGA', 'country_name':'Republic of Uganda'},
            'Kenya': {'country_code': 'KEN', 'country_name':'Republic of Kenya'},
            'Congo': {'country_code': 'DRC', 'country_name':'Democratic Republic of the Congo'},
            'Burundi': {'country_code': 'BDI', 'country_name':'Republic of Burundi'},
            'Tanzania': {'country_code': 'TZA', 'country_name':'United Republic of Tanzania'},
            'South Sudan': {'country_code': 'SSD', 'country_name':'Republic of South Sudan'},
            'Rwanda': {'country_code': 'RWA', 'country_name':'Republic of Rwanda'},
            'Malawi': {'country_code': 'MWI', 'country_name':'Republic of Malawi'}}

# TO DO in the future: currencies could be added here.

markets = {'UGA': ['Kiboga',
            'Masindi',
            'Tororo',
            'Kampala',
            'Owino',
            'Busia',
            'Kabale',
            'Lira',
            'Kasese',
            'Soroti',
            'Mbale',
            'Gulu',
            'Iganga',
            'Bugiri',
            'Nakasero',
            'Nakawa',
            'Mubende',
            'Arua',
            'Kisenyi',
            'Mbarara',
            'Masaka',
            'Kapchorwa',
            'Kalerwe',
            'Luwero market',
            'Isingiro',
            'Kyankwanzi',
            'Kamwenge',
            'Kyenjonjo',
            'Kabarole',
            'Kyegegwa',
            'Rukiga'],
        'KEN': ['Eldoret',
            'Nakuru',
            'Machakos',
            'Makueni',
            'Meru',
            'Mombasa',
            'Kisumu',
            'Nairobi',
            'Kitale',
            'Isiolo',
            'Garissa',
            'Kisii',
            'Busia',
            'Embu',
            'Malindi',
            'Kajiado',
            'Bungoma',
            'Kitale',
            'Kitui',
            'Oloitoktok',
            'Wajir',
            'Oloitoktok',
            'Loitkt',
            'Kakamega',
            'Kakmega',
            'Garisa',
            'Kisii',
            'Loitoktok',
            'Kitui',
            'Kakamega',
            'Kitale ',
            'Eldoret',
            'Kitale',
            'Busia',
            'Taveta',
            'Kg'],
        'DRC': ['Kolwezi',
            'Bukavu',
            'Lubumbashi',
            'Uvira',
            'Goma',
            'Likasi',
            'Kasumbalesa'],
        'BDI': ['Bujumbura', 'Gitega', 'Ngozi', 'Kobero'],
        'TZA': ['Iringa',
            'Tunduma',
            'Dar es salaam',
            'Arusha',
            'Dodoma',
            'Mbeya',
            'Mwanza',
            'Majengo',
            'Kibaigwa',
            'Tanga/mgandini',
            'Tabora',
            'Shinyanga',
            'Singida',
            'Songea',
            'Sumbawanga',
            'Njombe',
            'Mtwara dc',
            'Morogoro urban',
            'Mwanyelwa',
            'Babati',
            'Musoma',
            'Lindi',
            'Mwanga',
            'Moshi',
            'Bukoba',
            'Geita',
            'Temeke',
            'Ilala (buguruni)',
            'Kinondoni (tandale )',
            'Kigoma'],
        'SSD': ['Juba', 'Yei'],
        'RWA': ['Rubavu',
            'Mulindi',
            'Kimironko',
            'Kamembe',
            'Ruhengeri',
            'Kimisagara',
            'Ruhuha',
            'Matimba',
            'Gichumbi',
            'Kibirizi',
            'Gicumbi',
            'Kigali',
            'Kiramuruzi',
            'Gacurabwenge',
            'Kirambo',
            'Kabaya',
            'Ziniya',
            'Nyabugogo',
            'Byumba',
            'Nyagatare',
            'Rukomo',
            'Gikongoro',
            'Busasamana',
            'Gahoromani',
            'Ndago',
            'Gahanga',
            'Nyamirambo',
            'Nyamata',
            'Base',
            'Gisenyi',
            'Ngororero',
            'Kibuye',
            'Muhanga',
            'Butare',
            'Mahoko',
            'Nkora',
            'Kibungo',
            'Kizi',
            'Ruhango',
            'Buhanda',
            'Mubyangabo',
            'Mukarange',
            'Congonil',
            'Kayenzi',
            'Gaseke',
            'Karenge',
            'Intunga',
            'Mugina',
            'Musanze',
            'Rushashi',
            'Mukamira',
            'Nyakarambi',
            'Muhondo',
            'Rwamagana',
            'Shyorongi',
            'Nyagahinga',
            'Kirambo',
            'Musha',
            'Gasarenda',
            'Gashyushya',
            'Kabarondo',
            'Karambi',
            'Kibungo',
            'Birambo',
            'Gakenke',
            'Bugarama'],
        'MWI': ['Namwera',
            'Ntcheu',
            'Mitundu',
            'Salima',
            'Nkhotakota',
            'Mponela',
            'Mvera',
            'Balaka',
            'Ntchisi',
            'Kamwendo market',
            'Nkhamenya',
            'Kasungu',
            'Liwonde',
            'Mchinji',
            'Phalombe',
            'Chimbiya',
            'Limbe market',
            'Mzuzu',
            'Mzimba',
            'Mwanza',
            'Mkando',
            'Lilongwe',
            'Madisi',
            'Ace blantyre',
            'Ace lilongwe',
            'Kamwendo']}

# In what countries, the currency is related to the prices.

currencies = {'UGX': ['UGA', 'KEN', 'BDI', 'RWA', 'DRC', 'TZA', 'SSD'],
             'RWF': ['RWA'],
             'TZS': ['TZA'],
             'MWK': ['MWI'],
             'KES': ['KEN', 'UGA', 'DRC', 'BDI', 'TZA', 'SSD', 'RWA']}

sources = {'EAGC-RATIN': ['KEN', 'UGA', 'DRC', 'BDI', 'TZA', 'SSD', 'RWA'],
           'Farmgain': ['UGA'],
           'MIT (Tanzania)': ['TZA'],
           'InfoTrade': ['UGA'],
           'MinAgri(RW) ESOKO': ['RWA'],
           'ACE Malawi/RATIN': ['MWI'],
           'MOA-NAFIS': ['KEN'],
           'RATIN': ['RWA']}


prod_categories = ['Cereals - Maize',
                 'Beans',
                 'Animal Products',
                 'Cereals - Other',
                 'Cereals - Rice',
                 'Seeds & Nuts',
                 'Peas',
                 'Roots & Tubers',
                 'Fruits',
                 'Other',
                 'Vegetables',
                 '',
                 'Farm Inputs',
                 'Vegetable',
                 'Farm Input',
                 'Fuel',
                 'Animal Product']

products = {'Cereals - Maize': ['Dry Maize',
                                'Maize Flour',
                                'Maize Bran',
                                'Green Maize',
                                'Maize',
                                'Imported Maize',
                                'Maize Meal',
                                'Maize Grain'],
            'Beans': ['Yellow Beans',
                                'Green Gram',
                                'White Beans',
                                'Old Beans',
                                'Soya Beans',
                                'Mixed Beans',
                                'Red Beans',
                                'Black Beans (Dolichos)',
                                'Kidney Beans',
                                'Nambale Beans',
                                'Agwedde Beans',
                                'Beans Rosecoco',
                                'Beans (K132)',
                                'Dolichos (Njahi)',
                                'Mwezi Moja',
                                'Beans Mwitemania',
                                'Beans Canadian',
                                'White beans',
                                'Soya beans',
                                'Beans',
                                'French Beans',
                                'Green Beans'],
            'Animal Products': ['Tilapia',
                                'Pork',
                                'Goat Meat',
                                'Nile Perch',
                                'Milk',
                                'Turkey',
                                'Processed Honey',
                                'Local Eggs',
                                'Local Chicken',
                                'Exotic Eggs',
                                'Exotic Chicken',
                                'Beef',
                                'Unprocessed Honey',
                                'Eggs',
                                'Sheep',
                                'Goats',
                                'Goat skin and hide',
                                'Cow hide',
                                'Sheep hide and skin',
                                'Mutton',
                                'Cow',
                                'Bull',
                                'Fresh Milk'],
            'Cereals - Other': ['Sorghum Grain',
                                'Sorghum Flour',
                                'Millet Grain',
                                'Red Sorghum',
                                'Wheat',
                                'Wheat Flour',
                                'White Sorghum',
                                'White Millet',
                                'Pearl Millet',
                                'Barley',
                                'Millet Flour',
                                'Finger Millet',
                                'Wheat Bran',
                                'Bulrush Millet',
                                'Sorghum',
                                'Millet'],
            'Cereals - Rice': ['Imported Rice',
                                'Rice',
                                'Morogoro Rice',
                                'Unprocessed/husked rice',
                                'Kilombero Rice',
                                'Mbeya Rice',
                                'Upland Rice',
                                'Kahama Rice',
                                'Super Rice',
                                'Kayiso Rice',
                                'Rice Bran',
                                'Paddy Rice',
                                'Tanzanian  Rice',
                                'Rwandan Rice',
                                'Asian Rice'],
            'Seeds & Nuts': ['Ground Nuts',
                                'Sunflower Seed',
                                'Groundnuts',
                                'Simsim',
                                'Sunflower Seed Cake'],
            'Peas': ['Green Peas',
                                'Pigeon Peas',
                                'Dry Peas',
                                'Cowpeas',
                                'Chic Pea',
                                'Fresh Peas',
                                'Peas',
                                'Cow Peas'],
            'Roots & Tubers': ['Cassava Fresh',
                                'Sun Dried Cassava',
                                'Red Irish Potatoes',
                                'Cassava Flour',
                                'White Fleshed Sweet Potatoes',
                                'White Irish Potatoes',
                                'Dry Fermented Cassava',
                                'Cassava Chips',
                                'Sweet Potatoes',
                                'Irish Potatoes',
                                'Round Potatoes',
                                'Beet Roots'],
            'Fruits': ['Cooking Bananas',
                                'Pineapples',
                                'Cavendish (Bogoya)',
                                'Apple Bananas',
                                'Avocado',
                                'Pawpaw',
                                'Limes',
                                'Mangoes Ngowe',
                                'Mangoes Local',
                                'Lemons',
                                'Oranges',
                                'Passion Fruits',
                                'Ripe Bananas',
                                'Apples',
                                'Banana Bunch',
                                'Sweet Bananas',
                                'Mandarine',
                                'Guavas',
                                'Strawberry',
                                'Guava'],
            'Other': ['Tobacco',
                                'Coffee (Robusta)',
                                'Coffee (Arabica)',
                                'Unprocessed Vanilla',
                                'Unprocessed Tea',
                                'Unprocessed Cotton'],
            'Vegetables': ['Ginger',
                                'Kales',
                                'Lettuce',
                                'Cauliflower',
                                'Brinjal/Eggplant',
                                'Capsicums',
                                'Cucumber',
                                'Chillies',
                                'Spring Onions',
                                'Onions Dry',
                                'Tomatoes',
                                'Carrots',
                                'Cabbages',
                                'Pepper',
                                'Garlic',
                                'Red Onions',
                                'Green Pepper',
                                'Leek',
                                'Pounded Cassava Leaves',
                                'White Onions',
                                'Eggplant',
                                'Celery',
                                'Pumpkins',
                                'Spinach'],
            '': ['Sunflower Seed Meal',
                                'Matooke',
                                'Sunflower',
                                'CEREAL',
                                'LEGUMES',
                                'ROOTS & TUBERS',
                                'HORTICULTURE',
                                'OTHERS'],
            'Farm Inputs': ['Ditane', 'NPK Fertilizer'],
            'Vegetable': ['Amaranth', 'Parsley'],
            'Farm Input': ['Chemical Fertilizer',
                                'Urea Fertilisers'],
            'Fuel': ['Wood Charcoal']}