"""
Choices for fields in product model
"""

GENDER_CHOICES = (
    ('W', 'Womens'),
    ('M', 'Mens'),
    ('U', 'Unisex'),
)

SIZES = (
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
)

SOCK_SIZES = (
    ('34-37', '34-37'),
    ('38-41', '38-41'),
    ('42-45', '42-45'),
    ('46-50', '46-50'),
)

WOMENS_SIZES = SIZES[:-7]
WOMENS_SOCK_SIZES = SOCK_SIZES[:-1]

MENS_SIZES = SIZES[5:]
MENS_SOCK_SIZES = SOCK_SIZES[1:]

SIZE_CHOICES = (
    ('Sizes', SIZES),
    ('Womens Sizes', WOMENS_SIZES),
    ('Mens Sizes', MENS_SIZES),
    ('Sock Sizes', SOCK_SIZES),
    ('Womens Sock Sizes', WOMENS_SOCK_SIZES),
    ('Mens Sock Sizes', MENS_SOCK_SIZES),
    ('N/A', 'N/A'),
)

RATING_CHOICES = [
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
]
