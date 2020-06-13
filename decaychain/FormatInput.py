## For thThis function removes extra carriage returns, formats the nuclides
# and splits the input whitespace (dict divide) and \r\n (next item)

from decaychain.NuclideFormatter import NuclideFormatter

def format_input(inputs):
    outputs = {}
    ## Splits digits and text for nuclides and reassembles in format XY-123
    for nuclide, activity in inputs.items():
        nuclide_out = NuclideFormatter(nuclide)
        formatted = {str(nuclide_out): float(activity)}
        ## Adds the formatted nuclide to the outputs dictionary. Duplicates are summed.
        for k in formatted.keys():
            outputs[k] = outputs.get(k,0) + formatted[k]

    return outputs


