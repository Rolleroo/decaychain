from decaychain.NuclideFormatter import NuclideFormatter
from decaychain.DecayChain import Generator


def HaflLifeSearch(Nuclide):
## Grabs the user input and renames
    user_nuclide = NuclideFormatter(Nuclide)

    # Finds the halflife using the Chain Generator Function
    chain_generator = Generator()
    nuclidess = chain_generator.nuclides_dict.get(user_nuclide)
    hl = nuclidess.halflife.value
    hl_unit = nuclidess.halflife.unit

    ## formats for return to fucntion that called it.
    half_life_result = [hl, hl_unit]
    return half_life_result