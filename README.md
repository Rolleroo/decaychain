# decaychain
This package decays single or multiple radionuclides and computes the daughter radionuclides and their concentrations at a user defined time.

Currently this package has only been tested on Python 3.6 running on Linux OS.

Installation
------------

```console
$ pip install decaychain
```

Syntax for Use
--------------
Example

```console
>>> import decaychain.BatemanMulti as decay
>>> decay.bateman_multi({"U-238":1e7, "235U":1e7}, 3e9, "yr")
{'U-235': 0.3735948863819144, 'Th-231': 0.3735948863834592, 'Pa-231': 0.37361227209089354, 'Ac-227': 0.3736122836452778, 'Th-227': 0.3684561382285081, 'Ra-223': 0.37361198361845205, 'Rn-219': 0.37361198361845205, 'Po-215': 0.3736122836886527, 'Pb-211': 0.3736122836886891, 'Bi-211': 0.37361228368869126, 'Tl-207': 0.37258111378571535, 'Po-211': 0.0010311699029807882, 'Fr-223': 0.0051561454435370985, 'At-219': 3.000702007281776e-07, 'Bi-215': 3.0007020072818374e-07}
```
This decays both U-238 and U-235 at a concentration of 1e7 Bq for 3e9 years.

Syntax
```console
>>> decay.bateman_multi({dictionaryinput}, time, "time units")
```
**dicitonaryinput** = dictionary with key nuclide as string and values as nuclide concentration_

**time** = a number (float or integer)

**time units** = string e.g. ("years", "yr", "minutes", "m", "hours", "hr" etc)

The output is a dictionary in the same format at the input

The Pint module(https://pint.readthedocs.io/en/0.12/)  is used to handle time units so a variety of time units can be used.

The nuclide input is tolerant of a variety of radionuclide formats i.e. U-235, U-238, 235U etc


How it works
------------

radioactivedecay uses decay data from ICRP Publication 107 (2008) combined with a Bateman Decay solution to calculate the final concentrations of nuclides
https://journals.sagepub.com/doi/pdf/10.1177/ANIB_38_3


Limitations
-----------

The following processes are not modelled by radioactivedecay:
- ingrowth of progeny from spontaneous fission decays
- neutronics, so no modelling of induced radioactivity or fission


## Data
* decaychain
Article: https://www.icrp.org/publication.asp?id=ICRP%20Publication%20107
Supplementary Data (ZIP file): https://journals.sagepub.com/doi/suppl/10.1177/ANIB_38_3
File used: ./ICRP-07.NDX (column names as per ./UserGuide.pdf - table on page 4)

## Thanks
With particular thanks to @bjodah for use of the batemaneq module (https://github.com/bjodah/batemaneq) and Alex Malins for leading the way (https://github.com/alexmalins/radioactivedecay)
