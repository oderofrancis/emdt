ASCII = """\
  ______ _____  __  __ _______ 
 |  ____|  __ \|  \/  |__   __|
 | |__  | |  | | \  / |  | |   
 |  __| | |  | | |\/| |  | |   
 | |____| |__| | |  | |  | |   
 |______|_____/|_|  |_|  |_|   
                               
                               
"""

__initialized = False


def init(silent=False, force=False):
    """
<<<<<<< HEAD
    Initializes the environment with ecoscope-specific customizations.
=======
    Initializes the environment with Library-specific customizations.
>>>>>>> bb55848d6933fbdceb51e4915c5aa37f85442d5a

    Parameters
    ----------
    silent : bool, optional
        Removes console output
    force : bool, optional
        Ignores `__initialized`

    """

<<<<<<< HEAD
    global __initialized
    if __initialized and not force:
        if not silent:
            print("EDMT already initialized.")
        return

    import pandas as pd

    pd.options.plotting.backend = "plotly"

    # Enable copy-on-write for pandas. It will be the default in pandas 3.0.
    pd.options.mode.copy_on_write = True

    from tqdm.auto import tqdm

    tqdm.pandas()

    import warnings

    from shapely.errors import ShapelyDeprecationWarning

    warnings.filterwarnings(action="ignore", category=ShapelyDeprecationWarning)
    warnings.filterwarnings(action="ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", message=".*initial implementation of Parquet.*")

    import plotly.io as pio

    pio.templates.default = "seaborn"

    __initialized = True
    if not silent:
        print(ASCII)




__all__ = ["base"]
=======
    print(ASCII)
>>>>>>> bb55848d6933fbdceb51e4915c5aa37f85442d5a
