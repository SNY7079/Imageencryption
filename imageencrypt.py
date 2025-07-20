import cv2
import numpy as np

def encrypt_image(image_path, operation="swap"):
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not read image from path '{image_path}'")
        return None

    if operation == "swap":
        encrypted_image = np.flip(image, axis=1)  
    elif operation == "xor":
        key = 123  
        encrypted_image = cv2.bitwise_xor(image, np.full_like(image, key))
    else:
        print(f"Error: Unsupported encryption operation '{operation}'")
        return None

    return encrypted_image

def decrypt_image(encrypted_image, operation="swap"):
    if encrypted_image is None:
        print("Error: No encrypted image provided for decryption.")
        return None

    if operation == "swap":
        decrypted_image = np.flip(encrypted_image, axis=1)  
    elif operation == "xor":
        key = 123
        decrypted_image = cv2.bitwise_xor(encrypted_image, np.full_like(encrypted_image, key))
    else:
        print(f"Error: Unsupported decryption operation '{operation}'")
        return None

    return decrypted_image
image_path = "input_image.jpg"
operation = "swap"  

encrypted_img = encrypt_image(image_path, operation)
if encrypted_img is not None:
    cv2.imwrite("encrypted_image.jpg", encrypted_img)

    decrypted_img = decrypt_image(encrypted_img, operation)
    if decrypted_img is not None:
        cv2.imwrite("decrypted_image.jpg", decrypted_img)
        print("Encryption and decryption complete!")
else:
    print("Encryption failed.")
