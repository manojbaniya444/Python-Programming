"""Inference on saved model"""
import torchvision
import torch
from torchvision import transforms
import model_builder

# setting up device
device = "cuda" if torch.cuda.is_available() else "cpu" 

MODEL_PATH = "models/05_going_modular_script_mode_tinyvgg_model.pth"
IMAGE_PATH = "./pizza.jpeg"
class_names = ["pizza", "steak", "sushi"]

# load the model
model = model_builder.TinyVGG(
    input_shape=3,
    hidden_units=10,
    output_shape=len(class_names)
).to(device)

model.load_state_dict(
    torch.load(MODEL_PATH, map_location=torch.device(device))
)

def predict_on_custom_image(model: torch.nn.Module,
                            image_path: str,
                            class_names: list):
  # read the image in tensor and normalize it
  image = torchvision.io.read_image(image_path).type(torch.float) / 255
  # transform the image shape
  resized_image = transforms.Compose([
      transforms.Resize(size=(64,64))
  ])
  # batch
  transformed_image = resized_image(image).unsqueeze(dim=0)
  # set to device
  final_image = transformed_image.to(device)
  # pred logits
  model.eval()
  with torch.inference_mode():
   pred_logit = model(final_image)
  #  print(pred_logit)
  pred_probs = torch.softmax(pred_logit, dim=1)
  pred_class = class_names[torch.argmax(pred_probs)]

  print(f"Pred class: {pred_class}, Pred Prob: {pred_probs.max():.3f}")

if __name__ == "__main__":
  predict_on_custom_image(model=model,
                          image_path=IMAGE_PATH,
                          class_names=class_names)
