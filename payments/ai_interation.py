from inference_sdk import InferenceHTTPClient
from numpy import average


class AiInteration:
    def ai_integration(self, image):
        CLIENT = InferenceHTTPClient(
            api_url="https://detect.roboflow.com",
            api_key="7emOY7vgz6Fz1GDR817U"
        )

        result = CLIENT.infer(image, model_id="rideit/1")

        confidences = [prediction['confidence'] for prediction in result['predictions']]
        average_confidence = average(confidences)

        return average_confidence
