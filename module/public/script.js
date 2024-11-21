window.onload = function() {
    axios.get('/api/books')
      .then(response => {
        const books = response.data.books;
        const booksList = document.getElementById('books-list');
        
        // Очищуємо список перед додаванням нових елементів, щоб уникнути дублювання
        booksList.innerHTML = '';
  
        books.forEach(book => {
          const bookElement = document.createElement('div');
          bookElement.classList.add('book');
          
          bookElement.innerHTML = `
            <h2>${book.title}</h2>
            <p>Автор: ${book.author}</p>
            <p>Рік: ${book.year}</p>
          `;
          
          booksList.appendChild(bookElement);
        });
      })
      .catch(error => {
        console.error('Помилка при завантаженні даних:', error);
      });
  };
  