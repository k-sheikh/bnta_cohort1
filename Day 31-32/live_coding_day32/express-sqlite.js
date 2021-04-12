import express from "express";
import bodyParser from "body-parser";
import sqlite3 from "sqlite3";
import { open } from "sqlite";

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

async function createDb() {
  const openDb = await open({
    filename: "./movies.db",
    driver: sqlite3.Database,
  });
  await openDb.exec(
    "CREATE TABLE IF NOT EXISTS movies(id integer PRIMARY KEY, title text NOT NULL, director text NOT NULL)"
  );
  return openDb;
}

const db = await createDb();

// route definition
app.get("/movies", async (req, res) => {
  try {
    const movies = await db.all("SELECT * FROM movies");
    res.status(200).json(movies);
  } catch (e) {
    res.status(500).send(e);
  }
});

app.post("/movies", async (req, res) => {
  const { title, director } = req.body;
  try {
    if (
      !title ||
      !director ||
      typeof title !== "string" ||
      typeof director !== "string"
    )
      throw "Incorrect payload.";
    const result = await db.run(
      `INSERT INTO movies(title, director) VALUES(?, ?)`,
      [title, director]
    );
    const newMovie = await db.get(
      `SELECT * FROM movies where id=${result.lastID}`
    );
    res.status(201).json(newMovie);
  } catch (e) {
    res.status(500).send(e);
  }
});

app.put("/movies/:id", async (req, res) => {
  const { id } = req.params;
  const { title, director } = req.body;
  try {
    await db.run(`UPDATE movies SET title = ?, director = ? WHERE id = ${id}`, [
      title,
      director,
    ]);
    const updatedMovie = await db.get(`SELECT * FROM movies where id=${id}`);
    res.status(200).json(updatedMovie);
  } catch (e) {
    res.status(500).send(e);
  }
});

app.delete("/movies/:id", async (req, res) => {
  const { id } = req.params;
  try {
    await db.run(`DELETE FROM movies WHERE id = ${id}`);
    res.status(204).json({});
  } catch (e) {
    res.status(500).send(e);
  }
});

// start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
