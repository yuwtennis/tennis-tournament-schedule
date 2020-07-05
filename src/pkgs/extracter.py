
import pandas as pd

class Extracter:

    """
    Simple wrapper to extract schedule table using dataframe
    """
    @staticmethod
    def extract_by_df(target url):

        # Get the schedule of the tournament
        dfs = pd.read_html(url)

        return { row[0]: row[5] for index, row in dfs[target].loc[1:].iterrows() ] }

