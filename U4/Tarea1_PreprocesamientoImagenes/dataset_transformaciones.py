import fiftyone as fo

fo.config.database_validation = False

dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    dataset_dir=r"C:\Users\luiso\OneDrive\Escritorio\Tec2025\Inteligencia_Artificial\U4\dataset_emociones",
    name="d"
)

print("Dataset cargado correctamente con", len(dataset), "imágenes")

try:
    print("Intentando lanzar la app de FiftyOne...")
    session = fo.launch_app(dataset)
    session.wait()
except Exception as e:
    print("Error al lanzar la app:", e)