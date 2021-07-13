from pygame.image import load

def load_sprite(name, with_alpha=True):
    path = f"space_rocks/assets/sprites/{name}.jpg"
    # This method returns a surface, which is an object used by Pygame to represent images
    loaded_sprite = load(path)

    if with_alpha:
        # convert the image to a format that better fits the screen to speed up the drawing process
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()