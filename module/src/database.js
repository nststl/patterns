const sqlite3 = require('sqlite3').verbose();
const path = require('path');

class Database {
  constructor() {
    if (!Database.instance) {
      this.db = new sqlite3.Database(path.join(__dirname, 'books.db'), (err) => {
        if (err) {
          console.error('Помилка підключення до бази даних', err.message);
        } else {
          console.log('Підключено до бази даних');
        }
      });
      Database.instance = this;
    }
    return Database.instance;
  }

  getDb() {
    return this.db;
  }
}

module.exports = new Database();
