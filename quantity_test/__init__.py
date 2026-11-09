"""
A test function for docs
"""

__version__ = "0.0.1"

from typing import Literal
import astropy.units as u

def test_function(
        param_a: u.Quantity,
        param_b: u.Quantity[u.m],
        param_c: u.Quantity[u.deg] | Literal["spam"],
        param_d: u.Quantity["length"],
        param_u: u.Unit,
        ):
    """
    A function.

    Parameters
    ----------
    param_a
        A

    param_b
        B

    param_c
        C

    param_d
        D
    
    param_u
        U

    """
    print("Hello")
