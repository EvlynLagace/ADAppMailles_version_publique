import json

from adappmailles.data.motifs_test_listes import get_motifs_test_listes

def exporter_catalogue_json(path="src/adappmailles/data/catalogue.json"):
    motifs = get_motifs_test_listes()

    data = {
        "motifs": [
            m.to_json() for m in motifs
        ]
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Catalogue exporté vers {path}")


if __name__ == "__main__":
    exporter_catalogue_json()