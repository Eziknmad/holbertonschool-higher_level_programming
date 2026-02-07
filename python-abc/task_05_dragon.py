#!/usr/bin/env python3
"""
Defines mixin classes SwimMixin and FlyMixin and a Dragon class
that combines both behaviors.
"""


class SwimMixin:
    """
    Mixin that provides swimming ability.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying ability.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class combining SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Print roaring behavior.
        """
        print("The dragon roars!")
