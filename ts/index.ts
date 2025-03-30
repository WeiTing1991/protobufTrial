import { User } from "./user";
import * as fs from "fs";

const fetchData = fs.readFileSync("../user.bin");

const user = User.decode(fetchData);
console.log(user);
