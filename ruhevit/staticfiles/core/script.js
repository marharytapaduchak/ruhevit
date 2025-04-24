function openSearch() {
    console.log("Search button clicked");
    // Example: Show a hidden search bar (uncomment and modify as needed)
    // document.querySelector('.search-bar').classList.toggle('visible');
  }


  function activateSearch() {
    const searchEl = document.querySelector('.search');
    searchEl.classList.add('active');

    const input = searchEl.querySelector('.search-input');
    input.focus();
  }

//   document.addEventListener('DOMContentLoaded', () => {
//     const input = document.getElementById('search-input');
//     const resultsBox = document.getElementById('search-results');

//     // Перевіряємо, чи існують необхідні елементи
//     if (!input || !resultsBox) {
//         console.error('Елементи пошуку не знайдено на сторінці');
//         return;
//     }

//     // Додаємо обробник подій для поля вводу
//     input.addEventListener('input', function() {
//         const query = this.value.trim();

//         // Очищаємо результати, якщо запит короткий
//         if (query.length < 2) {
//             resultsBox.innerHTML = '';
//             resultsBox.style.display = 'none';
//             return;
//         }

//         // Показуємо блок результатів
//         resultsBox.style.display = 'block';

//         // Робимо запит до API
//         fetch(`/search-requests/?q=${encodeURIComponent(query)}`)
//             .then(response => {
//                 if (!response.ok) {
//                     throw new Error('Помилка в запиті до серверу');
//                 }
//                 return response.json();
//             })
//             .then(data => {
//                 resultsBox.innerHTML = '';

//                 if (data.length === 0) {
//                     const noResults = document.createElement('div');
//                     noResults.className = 'search-no-results';
//                     noResults.textContent = 'Результатів не знайдено';
//                     resultsBox.appendChild(noResults);
//                     return;
//                 }

//                 data.forEach(item => {
//                     const div = document.createElement('div');
//                     div.className = 'search-result-item';
//                     div.textContent = item.title;
//                     div.onclick = () => {
//                         window.location.href = `/request/${item.id}/`;
//                     };
//                     resultsBox.appendChild(div);
//                 });
//             })
//             .catch(error => {
//                 console.error('Помилка пошуку:', error);
//                 resultsBox.innerHTML = '<div class="search-error">Виникла помилка під час пошуку</div>';
//             });
//     });

//     // Закриваємо результати при кліку поза блоком пошуку
//     document.addEventListener('click', function(event) {
//         if (!input.contains(event.target) && !resultsBox.contains(event.target)) {
//             resultsBox.style.display = 'none';
//         }
//     });
//   });

document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("search-input");

    input.addEventListener("input", function () {
        const q = input.value.trim();
        if (q.length < 2) return;

        fetch(`/search/?q=${encodeURIComponent(q)}`)
            .then(response => response.json())
            .then(data => {
                console.log("Результати пошуку:", data);
            });
    });
});
