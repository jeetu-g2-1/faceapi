import base64
import io
import numpy as np
from PIL import Image
import face_recognition  # CPU-friendly, uses dlib under the hood

def base64_to_image(base64_string):
    """
    Convert Base64 string to PIL Image
    """
    image_bytes = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return np.array(image)

def compute_face_distance(base64_1, base64_2):
    """
    Compute similarity distance between two faces
    """
    # Convert Base64 strings to images
    image1 = base64_to_image(base64_1)
    image2 = base64_to_image(base64_2)

    # Extract face embeddings
    encodings1 = face_recognition.face_encodings(image1)
    encodings2 = face_recognition.face_encodings(image2)

    if not encodings1 or not encodings2:
        raise ValueError("No face detected in one or both images.")

    # Take the first face found in each image
    encoding1 = encodings1[0]
    encoding2 = encodings2[0]

    # Compute Euclidean distance (smaller means more similar)
    distance = np.linalg.norm(encoding1 - encoding2)
    # Optionally convert to similarity score (0-100)
    similarity_score = max(0, 100 - distance * 100)  # simple scaling
    return distance

# -------------------- Example Usage --------------------
# if __name__ == "__main__":
#     # Replace these with your Base64 image strings
#     base64_img1 = "<BASE64_IMAGE_1>"
#     base64_img2 = "<BASE64_IMAGE_2>"

#     distance, similarity = compute_face_distance(base64_img1, base64_img2)
#     print(f"Euclidean Distance: {distance:.4f}")
#     print(f"Similarity Score: {similarity:.2f}%")