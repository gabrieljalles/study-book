const express = require("express");

const { v4: uuid } = require("uuid");

const app = express();

app.use(express.json());

const repositories = [];

app.post("/repositories", (request, response) => {
  const { title, url, techs } = request.body;

  const repository = {
    id: uuid(),
    title,
    url,
    techs,
    likes: 0
  };

  repositories.push(repository);

  return response.json(repository);
});

app.get("/repositories", (request, response) => {
  return response.json(repositories);
});

app.put("/repositories/:id", (request, response) => {

  const { id } = request.params;
  const {title, url, techs, likes} = request.body;

  const repository = repositories.find(repository => repository.id === id)

   if (!repository) {
    return response.status(404).json({error: 'repository does not exist'})
  }

  if (likes){
  }

  if (url){
    repository.url = url;
  }

  if (techs){
    repository.techs = techs;
  }

  if(title){
    repository.title = title;
  }

  return response.json(repository);
});

app.delete("/repositories/:id", (request, response) => {
  const { id } = request.params;

  const repository = repositories.some(repository => repository.id === id)
  

  if(!repository){
    return response.status(404).json({error:'repository does not exist'})
  }

  const repositoryIndex = repositories.indexOf(repository => repository.id === id)
  
  repositories.splice(repositoryIndex, 1)

  return response.status(204).json(repositories);

});


app.post("/repositories/:id/like", (request, response) => {
  const { id } = request.params;

 const repository = repositories.find(repository => repository.id === id)

 if(!repository){
  return response.status(404).json({error: 'repository not found'})
 }

 repository.likes++;

 return response.json(repository);
});

module.exports = app;
