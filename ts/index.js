"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var user_1 = require("./user");
var fs = require("fs");
var fetchData = fs.readFileSync("../user.bin");
var user = user_1.User.decode(fetchData);
console.log(user);
