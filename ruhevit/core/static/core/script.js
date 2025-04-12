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