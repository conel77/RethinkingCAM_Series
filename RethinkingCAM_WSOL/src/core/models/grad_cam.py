import numpy as np
from src.core.models.base_cam import BaseCAM
from src.core.models.activations_and_gradients import ActivationsAndGradients
from src.core.models.model_targets import ClassifierOutputTarget

class GradCAM(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(
            GradCAM,
            self).__init__(
            model,
            target_layers,
            use_cuda,
            reshape_transform)

    def get_cam_weights(self,
                        input_tensor,
                        target_layer,
                        target_category,
                        activations,
                        grads):
        return np.mean(grads, axis=(2, 3))