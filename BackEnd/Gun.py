class Gun:
    """
     The Gun class represents a gun in a 2D game that can rotate based on the mouse position
    and fire lasers of different colors based on the current level.

    """
    def __init__(self, width, height, gun_images):
        """
        Initialize the gun's properties such as width, height, and gun images for each level

        :param width: The width of the screen.
        :param height: The height of the screen.
        :param gun_images: A list of images representing the gun for each level
        """
        self.width = width
        self.height = height
        self.gun_images = gun_images
        self.lasers = ['red', 'purple', 'green']

