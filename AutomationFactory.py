class AutomationFactory:
    def is_bulky(self, width: float, height: float, length: float) -> bool:
        """
        Checks if the package is bulky.

        Args:
            width (float): The width of the package.
            height (float): The height of the package.
            length (float): The length of the package.

        Returns:
            bool: True if the package is bulky; False otherwise.
        """
        volume = width * height * length
        return volume >= 1000000 or width >= 150 or height >= 150 or length >= 150

    def is_heavy(self, mass: float) -> bool:
        """
        Checks if the package is heavy.

        Args:
            mass (float): The mass of the package.

        Returns:
            bool: True if the package is heavy; False otherwise.
        """
        return mass >= 20

    def sort(self, width: float, height: float, length: float, mass: float) -> str:
        """
        Sorts the package into the correct stack.

        Added another rule for REJECTED: if any parameter is negative
        or zero due to human error, the package should go into the
        REJECTED stack.

        Args:
            width (float): The width of the package.
            height (float): The height of the package.
            length (float): The length of the package.

        Returns:
            str: The stack type (REJECTED, SPECIAL, or STANDARD).
        """
        if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
            return "REJECTED"

        bulky = self.is_bulky(width=width, height=height, length=length)
        heavy = self.is_heavy(mass=mass)
        if bulky and heavy:
            return "REJECTED"
        elif bulky or heavy:
            return "SPECIAL"
        else:
            return "STANDARD"
