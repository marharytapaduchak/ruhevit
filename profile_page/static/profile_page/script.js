function activateSearch() {
    const searchBar = document.querySelector('.search-bar');
    searchBar.classList.add('active');
  
    const input = searchBar.querySelector('.search-input');
    input.focus();
  }