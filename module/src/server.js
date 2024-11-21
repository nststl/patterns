const express = require('express');
const app = express();
const db = require('./database').getDb();

app.use(express.static('public'));

// Створення таблиці
const createTable = () => {
  const query = `CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
  )`;
  return new Promise((resolve, reject) => {
    db.run(query, function(err) {
      if (err) {
        reject('Помилка створення таблиці: ' + err.message);
      } else {
        resolve();
      }
    });
  });
};

// Очищення таблиці від старих записів
const clearTable = () => {
  return new Promise((resolve, reject) => {
    db.run('DELETE FROM books', (err) => {
      if (err) reject('Помилка очищення таблиці: ' + err.message);
      resolve();
    });
  });
};

// Вставка тестових даних
const insertTestData = async () => {
  const checkQuery = `SELECT COUNT(*) AS count FROM books WHERE title = ?`;

  // Тестові дані
  const books = [
    { title: 'Мобі Дік', author: 'Герман Мелвілл', year: 1851 },
    { title: '1984', author: 'Джордж Орвелл', year: 1949 },
    { title: 'Гаррі Поттер і філософський камінь', author: 'Дж. К. Роулінг', year: 1997 }
  ];

  // Пройдемося по кожній книзі та перевіримо наявність в базі даних
  for (const book of books) {
    try {
      const row = await new Promise((resolve, reject) => {
        db.get(checkQuery, [book.title], (err, row) => {
          if (err) {
            reject('Помилка перевірки наявності книги: ' + err.message);
          } else {
            resolve(row);
          }
        });
      });

      if (row.count === 0) {
        // Книга не знайдена, можна вставляти
        const query = `INSERT INTO books (title, author, year) VALUES (?, ?, ?)`;
        await new Promise((resolve, reject) => {
          db.run(query, [book.title, book.author, book.year], (err) => {
            if (err) {
              reject('Помилка вставки даних: ' + err.message);
            } else {
              resolve();
            }
          });
        });
      }
    } catch (err) {
      console.error(err);
    }
  }
};

// Обробка запиту до API /api/books
app.get('/api/books', (req, res) => {
  const query = 'SELECT * FROM books';
  db.all(query, [], (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json({ books: rows });
  });
});

// ініціалізація бази даних та запуск сервера
createTable()
  .then(() => clearTable())  // Очищаємо таблицю перед вставкою нових даних
  .then(() => insertTestData())  // Вставляємо тестові дані
  .then(() => {
    app.listen(3000, () => {
      console.log('Сервер запущено на порту 3000');
    });
  })
  .catch((err) => {
    console.error('Помилка ініціалізації:', err);
  });


