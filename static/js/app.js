const API = '/v1/movies';
let movies = [];
let selectedId = null;

async function loadMovies() {
  const res = await fetch(API);
  movies = await res.json();
  renderList();
}

function renderList() {
  const ul = document.getElementById('movie-list');
  ul.innerHTML = '';
  movies.forEach(m => {
    const li = document.createElement('li');
    li.className = 'list-group-item' + (m._id === selectedId ? ' active' : '');
    li.textContent = `${m.title} (${m.year})`;
    li.onclick = () => selectMovie(m);
    ul.appendChild(li);
  });
}

function selectMovie(m) {
  selectedId = m._id;
  document.getElementById('movie-details').style.display = 'block';
  document.getElementById('details-title').textContent =
    m._id ? 'Детали фильма' : 'Новый фильм';
  document.getElementById('title').value = m.title || '';
  document.getElementById('director').value = m.director || '';
  document.getElementById('year').value = m.year || '';
  document.getElementById('genre').value = m.genre || '';
  document.getElementById('rating').value = m.rating || 0;
  document.getElementById('description').value = m.description || '';
  document.getElementById('btn-create').style.display = m._id ? 'none' : 'inline-block';
  document.getElementById('btn-update').style.display = m._id ? 'inline-block' : 'none';
  document.getElementById('btn-delete').style.display = m._id ? 'inline-block' : 'none';
  renderList();
}

function createNewMovie() {
  selectMovie({ title: '', director: '', year: 0, genre: '', rating: 0, description: '' });
}

function readForm() {
  return {
    title: document.getElementById('title').value,
    director: document.getElementById('director').value,
    year: parseInt(document.getElementById('year').value) || 0,
    genre: document.getElementById('genre').value,
    rating: parseFloat(document.getElementById('rating').value) || 0,
    description: document.getElementById('description').value
  };
}

async function submitCreate() {
  const res = await fetch(API, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(readForm())
  });
  const created = await res.json();
  movies.push(created);
  selectMovie(created);
}

async function submitUpdate() {
  const res = await fetch(`${API}/${selectedId}`, {
    method: 'PUT',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(readForm())
  });
  const updated = await res.json();
  const idx = movies.findIndex(m => m._id === selectedId);
  if (idx !== -1) movies[idx] = updated;
  selectMovie(updated);
}

async function submitDelete() {
  await fetch(`${API}/${selectedId}`, { method: 'DELETE' });
  movies = movies.filter(m => m._id !== selectedId);
  selectedId = null;
  document.getElementById('movie-details').style.display = 'none';
  renderList();
}

async function deleteAllMovies() {
  await fetch(API, { method: 'DELETE' });
  movies = [];
  selectedId = null;
  document.getElementById('movie-details').style.display = 'none';
  renderList();
}

loadMovies();