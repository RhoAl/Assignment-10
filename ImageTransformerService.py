from PIL import Image

def transform():  
    filename = str(input("Enter the name of the image file you would like to resize: "))
    width = int(input("Enter the desired width of the photo (in pixels): "))
    height = int(input("Enter the desired height of the photo (in pixels): "))
    rotation = int(input("Enter the desired rotation of the photo (in degrees): "))
    img = Image.open(filename)

    img1 = img.resize((width, height))
    img1 = img1.rotate(rotation)

    #Integration code
    img1.show()
