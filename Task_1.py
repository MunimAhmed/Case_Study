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

def convert_json(filename):
  """Converts a JSON file to a standard format."""
  data = read_json(filename)
  if "class" in data:
    if data["class"] == "vehicle":
      data["object"] = "car"
    elif data["class"] == "license plate":
      data["object"] = "number"
  else:
    data["object"] = None
  write_json(filename, data)

if __name__ == "__main__":
  for filename in ["Pos_0.png.json", "Pos_10010.png.json", "Pos_10492.png.json"]:
    convert_json(filename)
