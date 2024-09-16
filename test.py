import yaml

print("Read from YAML file program.\n")
with open("test.yaml", "r") as testfile:
    yaml_data = yaml.safe_load(testfile)

for k, v in yaml_data.items():
    print(f"{k}: {v}")

print("\nThank you!")