document.addEventListener("DOMContentLoaded", function () {
    // Get DOM elements
    const searchInput = document.getElementById("search-input");
    const errorCode = document.getElementById("error-code");
    const errorMessage = document.getElementById("error-message");
    const homeButton = document.getElementById("home-button");
  
    // Error messages by code
    const errorMessages = {
      400: "Неправильний запит",
      401: "Необхідна авторизація",
      403: "Доступ заборонено",
      404: "Сторінку не знайдено",
      500: "Внутрішня помилка сервера",
      502: "Помилка шлюзу",
      503: "Сервіс недоступний",
      504: "Час очікування минув",
    };
  
    // Check URL for error code parameter
    function checkErrorCodeFromURL() {
      const urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get("code");
  
      if (code && errorMessages[code]) {
        updateErrorDisplay(code);
      } else {
        // Default to 404 if no valid code is provided
        updateErrorDisplay("404");
      }
    }
  
    // Update error display based on error code
    function updateErrorDisplay(code) {
      errorCode.textContent = code;
      errorMessage.textContent = errorMessages[code] || "Невідома помилка";
  
      // Update page title
      document.title = `Помилка ${code} | Ругевіт`;
    }
  
    // Handle search functionality
    searchInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
          // In a real application, this would redirect to search results
          alert(`Пошук за запитом: ${searchTerm}`);
          searchInput.value = "";
        }
      }
    });
  
    // Home button click handler
    homeButton.addEventListener("click", function () {
      // In a real application, this would redirect to the home page
      window.location.href = "/";
    });
  
    // Initialize error display based on URL
    checkErrorCodeFromURL();
  
    // Allow manual testing of different error codes via console
    window.setErrorCode = function (code) {
      if (errorMessages[code]) {
        updateErrorDisplay(code);
        // Update URL without reloading the page
        const url = new URL(window.location);
        url.searchParams.set("code", code);
        window.history.pushState({}, "", url);
      } else {
        console.error(
          "Invalid error code. Available codes:",
          Object.keys(errorMessages).join(", "),
        );
      }
    };
  });
  