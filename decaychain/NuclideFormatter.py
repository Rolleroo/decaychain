import re

def NuclideFormatter(nuclide):
    ## Formats a nuclide into the correct format for ICRP-07 matching.
    user_nuclide = nuclide
    ## finds the atomic mass
    atomic_mass = int("".join(filter(str.isdigit, user_nuclide)))
    ## regular expressions to find m and find element which must be in format "Aa".
    meta_regex = r"[0-9]+[mn]"
    element_regex = r"[A-Z][a-z]*"
    meta = re.search(meta_regex,user_nuclide)
    if meta:
        meta_state = re.findall(meta_regex, user_nuclide)[0][-1]
    else:
        meta_state = ''
    element = re.findall(element_regex, user_nuclide)[0]
    element_f = element[0].upper() + element[1:].lower()
    nuclide_out = str(element_f) + "-" + str(atomic_mass) +  meta_state
    return nuclide_out
z=NuclideFormatter("Te-125n")
print(z)