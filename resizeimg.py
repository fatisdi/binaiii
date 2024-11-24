from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def create_images(input_image_path):
   
    img = Image.open(input_image_path)
    img = img.resize((900, 900))
    img_array = np.array(img)

   
    small_images = [np.zeros((100, 100, 3), dtype=np.uint8) for _ in range(9)]

    
    for i in range(3): 
        for j in range(3):
           
            start_x = j * 3
            start_y = i * 3
            
           
            for y in range(0, 900-2, 3): 
                for x in range(0, 900-2, 3):  
                   
                    selected_pixel = img_array[y][x]
                    
                  
                    small_images[i * 3 + j][y % 100][x % 100] = selected_pixel

   
    plt.figure(figsize=(12, 12))
    
   
    plt.subplot(4, 4, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis('off')

   
    for i in range(9):
        plt.subplot(4, 4, i + 2)
        plt.imshow(small_images[i])
        plt.title(f"Image {i + 1}")
        plt.axis('off')

    plt.show()


input_image_path = 'C:\Users\zpc\Desktop\OMA_07_Room_interiors_EF_2_0aa83fed70.png'
create_images(input_image_path)
