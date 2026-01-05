import cv2
import os

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")
INSTAGRAM_SIZE = 1080


def add_white_border_make_square(image):
    height, width, _ = image.shape

    if width > height:
        diff = width - height
        top = diff // 2
        bottom = diff - top
        left = right = 0
    elif height > width:
        diff = height - width
        left = diff // 2
        right = diff - left
        top = bottom = 0
    else:
        top = bottom = left = right = 0

    bordered_image = cv2.copyMakeBorder(
        image,
        top,
        bottom,
        left,
        right,
        borderType=cv2.BORDER_CONSTANT,
        value=(255, 255, 255)  # white
    )

    return bordered_image


def process_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Skipping unreadable image: {image_path}")
        return

    dir_name, file_name = os.path.split(image_path)
    name, ext = os.path.splitext(file_name)

    # 1️⃣ Create square border image
    bordered_image = add_white_border_make_square(image)
    border_path = os.path.join(dir_name, f"{name}_border{ext}")
    # cv2.imwrite(border_path, bordered_image)

    # 2️⃣ Resize to Instagram 1080x1080
    instagram_image = cv2.resize(
        bordered_image,
        (INSTAGRAM_SIZE, INSTAGRAM_SIZE),
        interpolation=cv2.INTER_AREA
    )
    instagram_path = os.path.join(dir_name, f"{name}_instagram{ext}")
    cv2.imwrite(instagram_path, instagram_image)

    print(f"Processed: {file_name}")


def process_folder(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError("Invalid folder path provided.")

    for file in os.listdir(folder_path):
        if file.lower().endswith(SUPPORTED_EXTENSIONS):
            image_path = os.path.join(folder_path, file)
            process_image(image_path)
        else:
            print(f"Skipping non-image file: {file}")


if __name__ == "__main__":
    input_folder_path = r"C:\Users\sinha\OneDrive\Desktop\Photos-1-001"  # 🔁 change this
    process_folder(input_folder_path)
