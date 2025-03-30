# Proto Buffer

```bash
# Install protobuf
brew install protobuf
apt install protobuf-compiler

protoc --version
```

# Python

```bash
python -m venv .env
source .env/bin/activate

pip install protobuf

# to ProtoBuf
protoc --python_out=. FILENAME.proto
```

# typescript

```bash
protoc \
--plugin="./node_modules/.bin/protoc-gen-ts_proto" \
--ts_out=./ts \
--proto_path=./proto/FILENAME.proto


# run test
npx tsc index.ts
node ./index.js

```
