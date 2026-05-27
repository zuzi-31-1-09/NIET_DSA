# A mock 3x3 Grayscale Image Matrix (0 is black, 255 is white)
image = [
    [0,   128, 255],
    [255, 0,   128],
    [128, 255, 0]
]

print("Original Image Pixels:")
for row in image:
    print(row)

# AI Trick: To invert an image, subtract the current pixel from 255
inverted_image = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        inverted_image[i][j] = 255 - image[i][j]

print("\nInverted Image Pixels (Negative):")
for row in inverted_image:
    print(row)
