import copy
from decaychain.DataLoader import DataLoader
from decaychain.Nuclide import Nuclide
from decaychain.MeasurementUnit import Concentration
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


class Chain():
    def __init__(self):
        self.items = []
        self.ratio = 1

    def get_nuclide_names(self):
        return [
            item.nuclide.name
            for item in self.items
        ]

class Item():
    def __init__(self, nuclide: Nuclide, ratio: float, concentration: Concentration = None):
        self.nuclide = nuclide
        self.ratio = ratio
        self.concentration = concentration

class Generator():
    def __init__(self):
        path = 'data'
        with pkg_resources.path(__package__+'.'+path, 'ICRP-07.NDX') as path2:
            path2 = path2
        loader = DataLoader(path2)
        self.nuclides_dict = loader.get_nuclides_dict()
    
    def get_for_nuclide_name(self, nuclide_name):
        chains = []

        def __process_nuclide(nuclide, chain=Chain(), ratio=1):
            item = Item(
                nuclide=nuclide,
                ratio=ratio
            )
            chain.items.append(item)

            chain.ratio = ratio * chain.ratio

            for idx, daughter_nuclide_name in enumerate(nuclide.daughter_nuclide_names):
                daughter_nuclide_ratio = nuclide.daughter_nuclide_ratios[idx]
                daughter_nuclide = self.nuclides_dict.get(daughter_nuclide_name)

                if daughter_nuclide:
                    # the daughter nuclide was found in the decay list, so continue
                    new_chain = copy.deepcopy(chain)
                    __process_nuclide(daughter_nuclide, new_chain, ratio=daughter_nuclide_ratio)
                elif idx == 0:
                    # we reached the end of the chain
                    final_chain = copy.deepcopy(chain)

                    stable_nuclide = Nuclide(
                        name=daughter_nuclide_name,
                        radioactive=False
                    )

                    final_chain.items.append(
                        Item(
                            nuclide=stable_nuclide,
                            ratio=None
                        )      
                    )

                    chains.append(final_chain)

        nuclide = self.nuclides_dict.get(nuclide_name)
        if not nuclide:
            return chains

        __process_nuclide(nuclide)

        return chains