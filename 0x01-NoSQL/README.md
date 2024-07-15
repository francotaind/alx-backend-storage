##Mongodb

### Introduction
MongoDB is a cross-platform document-oriented database program. Classified as a
NoSQL database program, MongoDB uses JSON-like documents with optional schemas.
MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public
License (SSPL).

### Frequent MongoDB Commands
1. **Show Databases**
```bash
show dbs
```
2. **Create Database**
```bash
use mydatabase
```
3. **Drop Database**
```bash
db.dropDatabase()
```
4. **Create Collection**
```bash
db.createCollection('mycollection')
```
5. **Show Collections**
```bash
show collections
```
6. **Insert Document**
```bash
db.mycollection.insertOne({name: 'John Doe', age: 30})
```
7. **Find Document**
```bash 
db.mycollection.find()
```
8. **Update Document**
```bash
db.mycollection.updateOne({name: 'John Doe'}, {$set: {age: 35}})
```
9. **Delete Document**
```bash
db.mycollection.deleteOne({name: 'John Doe'})
```

### Conclusion
This document provided an overview of MongoDB and some of the frequent commands
