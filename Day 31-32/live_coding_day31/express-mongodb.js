const express = require("express");
const bodyParser = require("body-parser");
const MongoClient = require("mongodb");

const app = express();
const port = 3000;
const URI =
  "mongodb+srv://<username>:<password>@cluster0.ugszg.mongodb.net/retryWrites=true&w=majority";

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

let collection;

// route definition
app.get("/movies", async (req, res) => {
  try {
    const movies = await collection.find({}).toArray();
    res.status(200).json(movies);
  } catch (e) {
    res.status(500).send(e);
  }
});

app.post("/movies", async (req, res) => {
  const { title, director } = req.body;
  try {
    const result = await collection.insertOne({ title, director });
    const newMovie = await collection.findOne({ _id: result.insertedId });
    res.status(201).json(newMovie);
  } catch (e) {
    res.status(500).send(e);
  }
});

app.put("/movies/:id", async (req, res) => {
  const { id } = req.params;
  const { title, director } = req.body;
  try {
    const result = await collection.findOneAndUpdate(
      { _id: new MongoClient.ObjectID(id) },
      { $set: { title, director } },
      { upsert: true }
    );
    const updatedMovie = await collection.findOne({
      _id: new MongoClient.ObjectID(id),
    });
    res.status(200).json(updatedMovie);
  } catch (e) {
    res.status(500).send(e);
  }
});

app.delete("/movies/:id", async (req, res) => {
  const { id } = req.params;
  try {
    await collection.deleteOne({
      _id: new MongoClient.ObjectID(id),
    });
    res.status(204).json({});
  } catch (e) {
    res.status(500).send(e);
  }
});

// start the server
app.listen(port, () => {
  MongoClient.connect(URI, (err, db) => {
    if (err) throw err;
    const database = db.db("BNTA");
    collection = database.collection("movies");
  });
  console.log(`Server running on port ${port}`);
});
