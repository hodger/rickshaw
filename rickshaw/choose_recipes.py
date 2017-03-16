import random
natural_u238 = float()
natural_u235 = float()
low_enriched_u238 = float()
low_enriched_u235 = float()

NUCLIDES = {'natural_uranium': [{'id': 'U235', 'comp': natural_u235},
                                {'id': 'U238', 'comp': natural_u238}],
            'low_enriched_uranium': [{'id': 'U235', 'comp': low_enriched_u235},
                                     {'id': 'U238', 'comp': low_enriched_u238}],
            'used_fuel': [{'id': 'U235', 'comp': 0.00696},
                          {'id': 'U238', 'comp': 0.927},
                          {'id': 'Pu238', 'comp': 0.000255},
                          {'id': 'Pu239', 'comp': 0.00565},
                          {'id': 'Pu240', 'comp': 0.00279},
                          {'id': 'Pu241', 'comp': 0.00163},
                          {'id': 'Pu242', 'comp': 0.000822},
                          {'id': 'Am241', 'comp': 0.0000555},
                          {'id': 'Am243', 'comp': 0.000176},
                          {'id': 'Cm242', 'comp': 0.0000233},
                          {'id': 'Cm244', 'comp': 0.0000706}]
           }

NUCLIDES['natural_uranium_fuel'] = NUCLIDES['natural_uranium']
NUCLIDES['stored_used_fuel'] = NUCLIDES['used_uox'] = NUCLIDES['used_fuel']

def interpolate(upper, lower):
    U = random.uniform(0, 1.0)
    interp = (upper - lower)*U + lower
    return interp

def choose_recipes(commods):
    """Chooses the specific recipe for each commodity in the commods list

    Parameters
    ----------
        commods : list
            List of in and out commodities to be added to the archetypes in the
            input file.

    Returns
    -------
        recipes : list
            List of the assigned recipes to be added to the recipe section of
            the generated input file
    """
    low_enriched_u238 = interpolate(.97, .93)
    low_enriched_u235 = 1 - low_enriched_u238
    natural_u238 = interpolate(.999, .990)
    natural_u235 = 1 -  natural_u238
    
    recipes = []
    for commod in commods:
        recipe_dict = {}
        if commod not in NUCLIDES:
            continue
        recipe_dict['name'] = commod
        recipe_dict['basis'] = 'mass'
        recipe_dict['nuclide'] = NUCLIDES[commod]
        recipes.append(recipe_dict)
    return recipes

def generate_nuclide(commod):
    pass

