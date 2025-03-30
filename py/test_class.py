import user_pb2


class User:
  def __init__(self, id, name, age, is_active, address):
    self.id = id
    self.name = name
    self.age = age
    self.active = is_active
    self.address = address  # Expecting a dict like {"street": "...", "city": "..."}
    self.detail = {"id": self.id, "name": self.name}

  # Convert to protobuf object for serialization
  def to_proto(self):
    proto_user = user_pb2.User()
    proto_user.id = self.id
    proto_user.name = self.name
    proto_user.age = self.age
    proto_user.active = self.active
    proto_user.address.street = self.address["street"]
    proto_user.address.city = self.address["city"]
    proto_user.detail.id = self.detail["id"]
    proto_user.detail.name = self.detail["name"]
    return proto_user

  # Serialize to binary (for sending to TypeScript)
  def serialize(self):
    return self.to_proto().SerializeToString()

  # Optional: Create from protobuf (if you need to deserialize in Python)
  @classmethod
  def from_proto(cls, proto_data):
    proto_user = user_pb2.User()
    proto_user.ParseFromString(proto_data)
    address = {"street": proto_user.address.street, "city": proto_user.address.city}
    return cls(proto_user.id, proto_user.name, proto_user.age, proto_user.active, address)


if __name__ == "__main__":
  # Example usage in Python library
  address = {"street": "123 BahnhofStrasse", "city": "Zurich"}
  user = User(1, "Tom", 25, True, address)
  serialized_data = user.serialize()  # This is what you’d send to TypeScript
  print(f"Serialized data length: {len(serialized_data)} bytes")

  with open("./user.bin", "wb") as f:
    f.write(serialized_data)


