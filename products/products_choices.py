"""
Choices for fields in product and review models, products app
"""

# Choices enabling user to filter products by gender
GENDER_CHOICES = (
    ('Womens', 'W'),
    ('Mens', 'M'),
    ('Unisex', 'U'),
)
SIZE_CHOICES = (
    ('shoes', 'Shoes'),
    ('socks', 'Socks'),
    ('N/A', 'N/A'),
)

# All shoe sizes, displayed for unisex footware
# SHOE_SIZES = (
#     ('34', '34'),
#     ('35', '35'),
#     ('36', '36'),
#     ('37', '37'),
#     ('38', '38'),
#     ('39', '39'),
#     ('40', '40'),
#     ('41', '41'),
#     ('42', '42'),
#     ('43', '43'),
#     ('44', '44'),
#     ('45', '45'),
#     ('46', '46'),
#     ('47', '47'),
#     ('48', '48'),
#     ('49', '49'),
#     ('50', '50'),
# )

# # All sock sizes, displayed for unisex socks
# SOCK_SIZES = [
#     ('34-37', '34-37'),
#     ('38-41', '38-41'),
#     ('42-45', '42-45'),
#     ('46-50', '46-50'),
# ]

# Varibles so products can display relevant size type
# WOMENS_SIZES = SHOE_SIZES[:-7]
# WOMENS_SOCK_SIZES = SOCK_SIZES[:-1]
# MENS_SIZES = SHOE_SIZES[5:]
# MENS_SOCK_SIZES = SOCK_SIZES[1:]

# Add to Variable to be chosen from within the product instance

SIZES = (
    ('shoes', (
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
    )),
    ('shoes_women', (
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
    )),
    ('shoes_men', (
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
    )),
    ('socks', (
        ('34-37', '34-37'),
        ('38-41', '38-41'),
        ('42-45', '42-45'),
        ('46-50', '46-50'),
    )),
    ('socks_women', (
        ('34-37', '34-37'),
        ('38-41', '38-41'),
        ('42-45', '42-45'),
    )),
    ('socks_men', (
        ('38-41', '38-41'),
        ('42-45', '42-45'),
        ('46-50', '46-50'),
    )),
    ('N/A', 'N/A'),
)

# Choices for ratings made by users on the product detail page
RATING_CHOICES = [
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
]
