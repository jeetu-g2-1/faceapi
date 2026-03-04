import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api1.authentication import APIKeyAuthentication
from api1.logic import compute_face_distance
from api1.models import FaceImageResponse

class FaceVerificationAPI(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # 1️⃣ Ensure Content-Type is JSON
        if request.content_type != "application/json":
            return Response({"message": "Content-Type must be application/json"}, status=401)

        # 2️⃣ Ensure body is valid JSON
        if not isinstance(request.data, dict):
            return Response({"message": "Invalid JSON body"}, status=400)

        # 3️⃣ Get images from request
        original_img = request.data.get("original_img_response")
        face_img = request.data.get("face_img_response")

        if not original_img or not face_img:
            return Response({"message": "Both images are required"}, status=404)

        # 4️⃣ Compute face distance
        face_result = compute_face_distance(original_img, face_img)

        # 5️⃣ Store in database
        FaceImageResponse.objects.create(
            original=original_img,
            face=face_img,
            result=face_result
        )

        # 6️⃣ Determine AWS flag (traffic light)
        if face_result <= 0.6:
            aws_flag = 1  # green → strong match
        elif face_result <= 0.7:
            aws_flag = 2  # yellow → borderline match
        else:
            aws_flag = 3  # red → fail / no match

        # 7️⃣ Return response
        return Response({
            "statusCode": 200,
            "body": {
                "distance": face_result,  # raw distance for accurate comparison
                #"aws_flag": aws_flag
            },
            "message": "Success"
        })
