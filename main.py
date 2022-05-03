from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def print_hi(name):
    print(f"Hi, {name}")
    
if __name__ == "__main__":
    app = Ursina()
    
    #Player Config
    player = FirstPersonController()
    
    #Environment Config
    Sky()
    #Add models to the world
    model = Entity(model="plane", color=color.green, texture="grass", collider="mesh", scale=100, position=(0,-50,0))
    #casa = Entity(model="Casa model", color=color.brown, texture="wood_tex", collider="mesh", scale=100, position=(0,50,0))
    #castillo = Entity(model="Castle model", color=color.gray, texture=["Castle Exterior Texture Bump", "Castle Exterior Texture", "Castle Interior Texture Bump", "Castle Interior Texture", "Ground and Fountain Texture Bump", "Ground and Fountain Texture", "Towers Doors and Windows Texture Bump", "Towers Doors and Windows Texture"], collider="mesh", scale=20, position=(0,-50,0))
    castillo = Entity(model="Castle model", color=color.gray, texture="Castle Exterior Texture Bump", collider="mesh", scale=2, position=(0,-50,0))
    
    #Execute app
    app.run()