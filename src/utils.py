from tqdm import tqdm
from typing import Iterable


def nice_pbar(iterable: Iterable, total: int, desc: str) -> tqdm:
    """
    Create that nice progress bar.

    Args:
        iterable (Iterable): Iterable to iterate over.
        total (int): Number of elements in iterable.
        desc (str): Brief description of the process.
    Returns:
        tqdm (tqdm.std.tqdm): The tqdm object with the _nice_ settings
    """
    return tqdm(
        iterable,
        total=total,
        desc=desc,
        ascii=True,
        bar_format='{l_bar}{bar:10}{r_bar}',
        # disable=not wandb.config.enable_tqdm
        )
