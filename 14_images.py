from PIL import Image
imgMatrix = Image.open('14_images/word_matrix.png')
imgMask = Image.open('14_images/mask.png')
resizeMask = imgMask.resize((1015,559))
resizeMask.save("14_images/resizeMask.png", "PNG")
#resizeMask.show()

background = imgMatrix.convert("RGBA")
overlay = resizeMask.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("new.png", "PNG")

new_img.show()