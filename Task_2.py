import json

def read_json(filename):
  """Reads a JSON file and returns the data as a dictionary."""
  with open(filename, "r") as f:
    data = json.load(f)
  return data

def write_json(filename, data):
  """Writes a JSON file with the given data."""
  with open(filename, "w") as f:
    json.dump(data, f, indent=2)

def combine_jsons(filenames):
  """Combines the given JSON files into a single JSON file."""
  data = {}
  for filename in filenames:
    data.update(read_json(filename))
  write_json("combined.json", data)

def change_class_names(data):
  """Changes the class names in the given data to vehicle>car, license plate >number."""
  for object in data["objects"]:
    if object["class"] == "vehicle":
      object["class"] = "car"
    elif object["class"] == "license plate":
      object["class"] = "number"

if __name__ == "__main__":
  filenames = ["Pos_0.png.json", "Pos_10010.png.json", "Pos_10492.png.json"]
  combine_jsons(filenames)
  change_class_names(read_json("combined.json"))
  write_json("combined.json", read_json("combined.json"))
