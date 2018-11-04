import arcade

# Plays the Aggie War Hymn
def playWarHymn():
   # arcade.sound.load_sound("sounds\\aggieWarHymn.wav")
    arcade.sound.play_sound("sounds\\aggieWarHymn.wav")

# Plays the sound of a dog bark
def revHowdy():
    arcade.sound.play_sound("sounds\\bark.wav")

playWarHymn()
