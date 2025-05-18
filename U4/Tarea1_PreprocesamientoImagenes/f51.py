import fiftyone as fo
import albumentations as A
import cv2
import os

fo.config.database_validation = False

dataset_dir = r"C:\Users\luiso\OneDrive\Escritorio\Tec2025\Inteligencia_Artificial\U4\dataset_emociones"

dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    dataset_dir=dataset_dir,
    name="emociones_dataset",
    overwrite=True
)

print("Dataset cargado correctamente con", len(dataset), "imágenes")

# Borrar dataset si existe para evitar error de nombre no disponible
if fo.dataset_exists("emociones_con_albumentations"):
    fo.delete_dataset("emociones_con_albumentations")

preprocessed_dataset = fo.Dataset(name="emociones_con_albumentations")

output_dir = r"C:\Users\luiso\OneDrive\Escritorio\Tec2025\Inteligencia_Artificial\U4\albumentations_output"
os.makedirs(output_dir, exist_ok=True)

transform = A.Compose([
    A.RandomBrightnessContrast(p=0.5),
    A.HorizontalFlip(p=0.5),
    A.Rotate(limit=45, p=0.7),
    A.Resize(128, 128)
])

for sample in dataset:
    rel_path = os.path.relpath(sample.filepath, start=dataset_dir)
    new_path = os.path.join(output_dir, rel_path)
    os.makedirs(os.path.dirname(new_path), exist_ok=True)

    image = cv2.imread(sample.filepath)
    if image is None:
        print(f"No se pudo cargar la imagen: {sample.filepath}")
        continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    augmented = transform(image=image)
    transformed_image = augmented["image"]
    cv2.imwrite(new_path, cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR))

    new_sample = fo.Sample(filepath=new_path)
    if "ground_truth" in sample:
        new_sample["ground_truth"] = sample["ground_truth"]
    preprocessed_dataset.add_sample(new_sample)

print("Preprocesamiento con Albumentations completado.")

session = fo.launch_app(preprocessed_dataset)
session.wait()
