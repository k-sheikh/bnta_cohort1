const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

let movies = [];
const generateId = () => JSON.stringify(Date.now());

// route definition
app.get("/movies", async (req, res) => {
  res.status(200).json(movies);
});

app.post("/movies", async (req, res) => {
  const { title, director } = req.body;
  const newMovie = { id: generateId(), title, director };
  movies.push(newMovie);
  res.status(201).json(newMovie);
});

app.put("/movies/:id", (req, res) => {
  const { id } = req.params;
  movies = movies.map((movie) => {
    if (movie.id === id) {
      const updatedMovie = { ...movie, ...req.body };
      return updatedMovie;
    }
    return movie;
  });
  res.status(200).json(movies);
});

app.delete("/movies/:id", (req, res) => {
  const { id } = req.params;
  movies = movies.filter((movie) => movie.id !== id);
  res.status(204).json({});
});

// start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
