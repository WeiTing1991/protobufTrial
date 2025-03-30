# Protobuf

```bash
# Install protobuf
brew install protobuf
apt install protobuf-compiler

protoc --version
```

```bash
# for python

python -m venv .env
source .env/bin/activate

pip install protobuf

# to protobuff
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
