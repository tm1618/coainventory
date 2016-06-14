## MANAGEMENT COMMAND GENERATORS ###
#
# These generators help to create the mock
# data used throughout development.


# ================================== #
#    USER / DEFENDANT INFORMATION    #
# ================================== #

import random



FIRST_NAMES = (
    'Rossie', 'Lyndsay', 'Yang', 'Rachelle', 'Felipa', 'Stephanie', 'Charlsie', 'Parthenia', 'Gigi', 'Eliz',
    'Rudolph', 'Martha', 'Delphine', 'Keri', 'Tiffaney', 'Graciela', 'Johna', 'Wally', 'Georgina', 'Stan',
    'Cinda', 'Daniel', 'Erik', 'Kelli', 'Zada', 'Lenore', 'Rachel', 'Madalyn', 'Letitia', 'Hermine', 'Christie',
    'Tresa', 'Luvenia', 'Tomiko', 'Adelaida', 'Otis', 'Clelia', 'Julieta', 'Micheal', 'Hassie', 'Lettie', 'Kerrie',
    'Yasmine', 'Brigitte', 'Wyatt', 'Karisa', 'Sharyn', 'Hui', 'Chieko', 'Mikaela',
)
LAST_NAMES = (
    'Sanchez', 'Jacobson', 'Brooks', 'Myers', 'Hunt', 'Dodson', 'Terry', 'Obrien', 'Hall', 'Chambers', 'Maldonado',
    'Reyes', 'Sharp', 'Ayers', 'Velez', 'Lucas', 'Hansen', 'Chandler', 'Nixon', 'Buchanan', 'Leonard', 'Zuniga',
    'Walton', 'Hancock', 'Burch', 'Mcgrath', 'Ballard', 'Gilbert', 'Weaver', 'Walker', 'Wood', 'Kim', 'Daniel',
    'Joyce', 'Ponce', 'Fry', 'Livingston', 'Richardson', 'Cole', 'Leon', 'Lloyd', 'Mcgee', 'Nunez', 'Valentine',
    'Juarez', 'Bates', 'Pruitt', 'Nolan', 'Hurley', 'Velasquez',
)

def random_first_name():
    return random.choice(FIRST_NAMES)


def random_initial():
    name = random.choice(FIRST_NAMES)
    initial = name[:1]
    return initial


def random_last_name():
    return random.choice(LAST_NAMES)


def create_username(first_name, last_name):
    return (first_name + last_name)


def create_email(first_name, last_name):
    initial = first_name[:1]
    return (initial + last_name + '@gmail.com')


def dob():
    return "{0}-{1}-{2}".format(random.randrange(1950, 1990),
                                random.randrange(01, 12),
                                random.randrange(01, 28))


def ssn():
    return "{0}-{1}-{2}".format(random.randrange(100, 999),
                                random.randrange(10, 99),
                                random.randrange(1000, 9999))


NOTES = [
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
    'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \
     when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
    'It is a long established fact that a reader will be distracted by the readable \
     content of a page when looking at its layout.',
    'Contrary to popular belief, Lorem Ipsum is not simply random text.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod \
     tempor incididunt ut labore et dolore magna aliqua.',
]

def random_note():
    return "{0}".format(random.choice(NOTES))


# ================================== #
#  END USER / DEFENDANT INFORMATION  #
# ================================== #

# ================================== #
#     ADDRESS / PHONE INFORMATION    #
# ================================== #

def random_phone():
    return "{0}-{1}-{2}".format(random.randrange(500, 999),
                                random.randrange(100, 999),
                                random.randrange(1000, 9999))

def random_address():
    STREET = (
        "Oxford", "Bedford", "Scrouge", "Beth", "Timberlake", "Edgewater", "Madison", "Edgewood",
        "Railroad", "Brooks", "Clearwater", "Eylewood", "Maggie",
    )
    SUFFIX = ( "Rd.", "Ave.", "St.", "Blvd.")

    numerical = random.randrange(100, 2000)
    street = random.choice(STREET)
    suffix = random.choice(SUFFIX)
    return "{0} {1} {2}".format(numerical, street, suffix)

def random_address_2():
    LOCATION_TYPE = ("Suite", "Building", "Office")
    location_type = random.choice(LOCATION_TYPE)
    number = random.randrange(1, 150)
    return "{0} #{1}".format(location_type, number)



def random_city():
    CITIES = (
        "Athens", "Ardmore", "E. Limestone", "Tanner", "Decatur", "Huntsville", "Harvest", "Toney",
    )
    city = random.choice(CITIES)
    return "{0}".format(city)



def random_zipcode():
    ZIPCODES = (
        "35739", "35773", "35611", "35612", "35613", "35758", "35802", "35757",
    )
    zipcode = random.choice(ZIPCODES)
    return "{0}".format(zipcode)


# ================================== #
#        MERCHANT INFORMATION        #
# ================================== #

MERCHANTS = [
    'Barneys', 'Belk', 'Best Buy', 'BloomingDale', 'Kohl\'s', 'Macy\'s', 'Curacao', 'Nordstrom',
    'Wal-Mart', 'Target', 'Big Lots', 'Fred\'s', 'Kmart', 'Meijer', 'Costco', 'Sam\'s', 'Century 21',
    'Harbor Freight Tools', 'Family Dollar', 'Dollar General', 'Dollar Tree', 'Deals', 'T.J. Max',
    'Stein Mart', 'Kroger', 'Publix', 'Aldi\'s', 'Save-A-Lot', 'Albertson\'s', 'Food City', 'Fairway Market',
    'Bi-Lo', 'Piggly-Wiggly', 'Hardee\'s', 'McDonald\'s', 'Taco Bell', 'Sonic Drive-In', 'L&S Foods',
]

def random_merchant_name():
    """ Go get a random Merchant name from the list"""
    merchant = random.choice(MERCHANTS)
    MERCHANTS.remove(merchant)
    return "{0}".format(merchant)


def create_witness():
    return "{0} {1}".format(random_first_name(), random_last_name())

def create_witness_email(name):
    return "{0}@examplemail.com".format(name)


# ==================================== #
#            CASE INFORMATION          #
# ==================================== #

CASE_NUMBER = [
    '0000010', '0000011', '0000012', '0000013', '0000014', '0000015', '0000016', '0000017', '0000018',
    '0000019', '0000020', '0000021', '0000022', '0000023', '0000024', '0000025', '0000026', '0000027',
    '0000028', '0000029', '0000030', '0000031', '0000032', '0000033', '0000034', '0000035', '0000036',
    '0000037', '0000038', '0000039', '0000040', '0000041', '0000042', '0000043', '0000044', '0000045',
    '0000046', '0000047', '0000048', '0000049', '0000050', '0000051', '0000052', '0000053', '0000054',
    '0000055', '0000056', '0000057', '0000058', '0000059', '0000060'
]
def create_case_number():
    """ Creates a Case number to represent the Case """
    return "{0}-{1}".format(15, random.choice(CASE_NUMBER))

def create_random_date():
    """ Creates a random date """
    return "{0}-{1}-{2}".format(2015, random.randrange(01, 12), random.randrange(01, 28))