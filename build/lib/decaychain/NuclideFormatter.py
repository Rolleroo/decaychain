import re

def NuclideFormatter(nuclide):
    user_nuclide = nuclide
    atomic_mass = int("".join(filter(str.isdigit, user_nuclide)))
    meta_regex = r"[0-9]+m"
    element_regex = r"[A-Z][a-z]*"
    element = re.findall(element_regex, user_nuclide)[0]
    meta = re.search(meta_regex, user_nuclide)
    element_f = element[0].upper() + element[1:].lower()
    nuclide_out = str(element_f) + "-" + str(atomic_mass) + ('m' if meta else '')
    return nuclide_out
