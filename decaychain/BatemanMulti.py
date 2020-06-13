from decaychain.BatemanDecay import bateman_trial
from decaychain.FormatInput import format_input

class bateman_multi:
        def __init__(self, dict_input, user_time, user_tunit):
        dict_input = dict_input
        user_time = user_time
        user_tunit = user_tunit

    def bateman_multi(self, dict_input, user_time, user_tunit):
        results = {}
        formatted = format_input(dict_input)

        for nuclide, activity in formatted.items():
            user_nuclide = str(nuclide)
            user_activity = float(activity)
            result = bateman_trial(user_nuclide, user_time, user_tunit, user_activity, "Bq")
            for nuclide, value2 in result.items():
                if not results.get(nuclide):
                    results[nuclide] = 0
                results[nuclide] += float(value2)
        return results
