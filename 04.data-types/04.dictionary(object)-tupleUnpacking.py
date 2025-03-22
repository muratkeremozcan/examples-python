

squirrels_madison = [
	{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Sitting', 'interactions_with_humans': 'Indifferent'},
	{'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon', 'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'},
	{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Climbing, Foraging', 'interactions_with_humans': 'Indifferent'}
]
squirrels_union = (
    "Union Square Park",
    [
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Eating, Foraging",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Cinnamon",
            "activities": "Climbing, Eating",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Cinnamon",
            "highlights_in_fur_color": None,
            "activities": "Foraging",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Running, Digging",
            "interactions_with_humans": "Runs From",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Digging",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Black",
            "activities": "Climbing",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Eating, Foraging",
            "interactions_with_humans": None,
        },
    ],
)

squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union[1] which is the list of squirrels
squirrels_by_park['Union Square Park'] = squirrels_union[1]

print(squirrels_by_park)
# {
#     'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None),
#     'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'),
#     'Madison Square Park': [{
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Sitting',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': 'Cinnamon',
#         'activities': 'Foraging',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Climbing, Foraging',
#         'interactions_with_humans': 'Indifferent'
#     }],
#     'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'),
#     'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'),
#     'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'),
#     'Union Square Park': ('Union Square Park', [{
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Eating, Foraging',
#         'interactions_with_humans': None
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': 'Cinnamon',
#         'activities': 'Climbing, Eating',
#         'interactions_with_humans': None
#     }, {
#         'primary_fur_color': 'Cinnamon',
#         'highlights_in_fur_color': None,
#         'activities': 'Foraging',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Running, Digging',
#         'interactions_with_humans': 'Runs From'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Digging',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': 'Black',
#         'activities': 'Climbing',
#         'interactions_with_humans': None
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Eating, Foraging',
#         'interactions_with_humans': None
#     }]),
#     'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')
# }


# Loop over the park_name in the squirrels_by_park dictionary 
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    if isinstance(squirrels_by_park[park_name], list):
        # For parks with list of dictionary values
        print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])
    else:
        # For parks with tuple values
        print(park_name, ['N/A'])