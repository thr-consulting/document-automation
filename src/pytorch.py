from models.PageResult import PageResult
import torch
import torch.nn.functional as F
from torchvision import transforms
from torchvision.models import efficientnet_v2_s
from PIL import Image


def load_model(model_path, class_names, size, device):
    print('\n---')
    print(f"Device: {device}")
    print(f"MODEL_PATH: {model_path}")

    # Define transforms for the input image
    transform = transforms.Compose(
        [
            transforms.Resize((size, size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    # Load the model
    model = efficientnet_v2_s(weights=None)
    num_classes = len(class_names)
    model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.to(device)

    # Set the model to evaluation mode
    model.eval()

    print("model loaded")
    print('---\n')
    return model, transform


def predict_single_image(model, transform, image, device, class_names, page_num) -> PageResult:
    print(f"-predict page {page_num}")
    
    image = Image.fromarray(image)
    image = transform(image).unsqueeze(0)  # Add batch dimension
    image = image.to(device)

    # Predict the class
    with torch.no_grad():
        outputs = model(image)
        probabilities = F.softmax(outputs, dim=1)
        max_prob, predicted = torch.max(probabilities, 1)

    predicted_class = class_names[predicted.item()]
    predicted_score = max_prob.item()

    print(f"--{predicted_class} ({predicted_score})\n")
    return PageResult(page_num, predicted_class, predicted_score)


def predict_images(model, transform, images, device, class_names) -> list[PageResult]:
    print(f"\nsort {str(len(images))} images")
    results: list[PageResult] = []

    page_num = 1
    for img in images:
        results.append(predict_single_image(model, transform,img, device, class_names, page_num))
        page_num = page_num + 1

    return results
