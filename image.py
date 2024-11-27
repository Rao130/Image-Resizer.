from PIL import Image

def resize_image(input_path, output_path, width=None, height=None, maintain_aspect_ratio=False):
    """
    Resize an image to a specified width and height.
    
    :param input_path: Path to the input image file
    :param output_path: Path to save the resized image
    :param width: Desired width of the resized image (optional if maintain_aspect_ratio is used)
    :param height: Desired height of the resized image (optional if maintain_aspect_ratio is used)
    :param maintain_aspect_ratio: Boolean to determine whether to maintain the aspect ratio (default False)
    """
    # Open the image file
    with Image.open(input_path) as img:
        if maintain_aspect_ratio:
            # Resize image while maintaining aspect ratio
            aspect_ratio = img.width / img.height
            new_height = int(width / aspect_ratio) if width else int(height * aspect_ratio)
            new_width = int(height * aspect_ratio) if height else int(width * aspect_ratio)
            img_resized = img.resize((new_width, new_height))
        else:
            # Resize image to the exact width and height
            img_resized = img.resize((width, height))
        
        # Save the resized image
        img_resized.save(output_path)
        print(f"Image saved as {output_path}")

# Example usage
input_path = "input_image.jpg"  # Path to the input image
output_path = "output_image.jpg"  # Path to save the resized image

# Resize to a specific width and height (without aspect ratio)
# width = 300, height = 200
resize_image(input_path, output_path, width=300, height=200, maintain_aspect_ratio=False)

# Resize to a specific width while maintaining the aspect ratio
# new_width = 300
resize_image(input_path, "output_image_aspect.jpg", width=300, maintain_aspect_ratio=True)

# Resize to a specific height while maintaining the aspect ratio
# new_height = 200
resize_image(input_path, "output_image_aspect_height.jpg", height=200, maintain_aspect_ratio=True)
