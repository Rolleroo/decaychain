from decaychain.BatemanDecay import bateman_trial
from decaychain.FormatInput import format_input


    def bateman_multi(self, self.dict_input, self.user_time, self.user_tunit):
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
