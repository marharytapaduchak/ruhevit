document.addEventListener("DOMContentLoaded", function () {
    // Get all interactive elements
    const form = document.getElementById("reportForm");
    const submitButton = document.getElementById("submitButton");
    const messageButton = document.querySelector(
      ".user-actions .icon-button:nth-child(1)",
    );
    const notificationButton = document.querySelector(
      ".user-actions .icon-button:nth-child(2)",
    );
    const profilePhoto = document.querySelector(".profile-photo");
    const searchBar = document.querySelector(".search-bar");
    const searchInput = document.querySelector(".search-placeholder");
  
    // Handle header buttons
    messageButton.addEventListener("click", function () {
      alert("Повідомлення відкрито");
      // Here you would typically open a messages panel or navigate to messages page
    });
  
    notificationButton.addEventListener("click", function () {
      alert("Сповіщення відкрито");
      // Here you would typically open a notifications panel
    });
  
    profilePhoto.addEventListener("click", function () {
      alert("Профіль користувача відкрито");
      // Here you would typically open a profile menu or navigate to profile page
    });
  
    // Handle search functionality
    searchBar.addEventListener("click", function () {
      // Convert the placeholder to an actual input when clicked
      if (!searchBar.querySelector("input")) {
        const placeholderText = searchInput.textContent;
        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = placeholderText;
        input.className = "search-input";
  
        searchInput.style.display = "none";
        searchBar.appendChild(input);
        input.focus();
  
        // Handle search submission
        input.addEventListener("keypress", function (e) {
          if (e.key === "Enter") {
            alert(`Пошук: ${input.value}`);
            // Here you would typically perform the search
  
            // Reset the search bar
            input.remove();
            searchInput.style.display = "";
          }
        });
  
        // Handle click outside to close
        document.addEventListener("click", function closeSearch(e) {
          if (!searchBar.contains(e.target)) {
            if (searchBar.contains(input)) {
              input.remove();
              searchInput.style.display = "";
            }
            document.removeEventListener("click", closeSearch);
          }
        });
      }
    });
  
    // Get form input fields
    const reportTitle = document.getElementById("reportTitle");
    const reportText = document.getElementById("reportText");
    const titleError = document.getElementById("titleError");
    const textError = document.getElementById("textError");
  
    // Auto-resize textarea as user types
    reportText.addEventListener("input", function () {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    });
  
    // Set initial height for textarea
    setTimeout(() => {
      reportText.style.height = reportText.scrollHeight + "px";
    }, 0);
  
    // Handle form submission with validation
    form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      // Reset error messages
      titleError.textContent = "";
      textError.textContent = "";
  
      // Validate title
      if (!reportTitle.value.trim()) {
        titleError.textContent = "Будь ласка, введіть заголовок";
        reportTitle.focus();
        return;
      }
  
      if (reportTitle.value.trim().length < 5) {
        titleError.textContent = "Заголовок має містити щонайменше 5 символів";
        reportTitle.focus();
        return;
      }
  
      // Validate text
      if (!reportText.value.trim()) {
        textError.textContent = "Будь ласка, введіть текст звіту";
        reportText.focus();
        return;
      }
  
      if (reportText.value.trim().length < 20) {
        textError.textContent = "Текст звіту має містити щонайменше 20 символів";
        reportText.focus();
        return;
      }
  
      // Disable button to prevent multiple submissions
      submitButton.disabled = true;
      submitButton.textContent = "Надсилання...";
  
      // Collect form data
      const formData = {
        title: reportTitle.value,
        text: reportText.value,
        // Add other form data here
      };
  
      console.log("Submitting form data:", formData);
  
      // Simulate form submission with a timeout
      setTimeout(function () {
        // Here you would normally send the data to a server
        // For demonstration, we'll just show an alert
        alert("Звіт успішно надіслано!");
  
        // Re-enable the button
        submitButton.disabled = false;
        submitButton.textContent = "Надіслати";
  
        // Optional: reset the form
        // form.reset();
      }, 1500);
    });
  
    // Add functionality to the photo upload area
    const photoUploadArea = document.querySelector(".photo-upload-area");
    const uploadLink = document.querySelector(".upload-link");
  
    // Create a hidden file input
    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.accept = "image/*";
    fileInput.style.display = "none";
    fileInput.multiple = true;
    document.body.appendChild(fileInput);
  
    // Handle click on upload area
    photoUploadArea.addEventListener("click", function () {
      fileInput.click();
    });
  
    // Handle file selection
    fileInput.addEventListener("change", function () {
      if (fileInput.files.length > 0) {
        handleFiles(fileInput.files);
      }
    });
  
    // Handle drag and drop
    photoUploadArea.addEventListener("dragover", function (e) {
      e.preventDefault();
      photoUploadArea.classList.add("drag-over");
    });
  
    photoUploadArea.addEventListener("dragleave", function () {
      photoUploadArea.classList.remove("drag-over");
    });
  
    photoUploadArea.addEventListener("drop", function (e) {
      e.preventDefault();
      photoUploadArea.classList.remove("drag-over");
  
      if (e.dataTransfer.files.length > 0) {
        handleFiles(e.dataTransfer.files);
      }
    });
  
    // Function to handle the selected files
    function handleFiles(files) {
      // Clear previous preview if needed
      const existingPreview = document.querySelector(".photo-preview");
      if (existingPreview) {
        existingPreview.remove();
      }
  
      // Create preview container
      const previewContainer = document.createElement("div");
      previewContainer.className = "photo-preview";
  
      // Add each file as a preview
      Array.from(files).forEach((file) => {
        if (!file.type.match("image.*")) return;
  
        const reader = new FileReader();
  
        reader.onload = function (e) {
          const imgContainer = document.createElement("div");
          imgContainer.className = "preview-item";
  
          const img = document.createElement("img");
          img.src = e.target.result;
          img.className = "preview-image";
  
          const removeBtn = document.createElement("button");
          removeBtn.className = "remove-image";
          removeBtn.innerHTML = '<i class="ti ti-x"></i>';
          removeBtn.onclick = function () {
            imgContainer.remove();
          };
  
          imgContainer.appendChild(img);
          imgContainer.appendChild(removeBtn);
          previewContainer.appendChild(imgContainer);
        };
  
        reader.readAsDataURL(file);
      });
  
      // Replace upload area with preview
      photoUploadArea.style.display = "none";
      photoUploadArea.parentNode.appendChild(previewContainer);
  
      // Add button to add more photos
      const addMoreBtn = document.createElement("button");
      addMoreBtn.className = "add-more-photos";
      addMoreBtn.innerHTML = '<i class="ti ti-plus"></i> Додати ще фото';
      addMoreBtn.onclick = function () {
        photoUploadArea.style.display = "flex";
        addMoreBtn.remove();
      };
  
      previewContainer.appendChild(addMoreBtn);
    }
  });
  
  // Add keyboard navigation support
  document.addEventListener("keydown", function (e) {
    // ESC key closes any open dialogs
    if (e.key === "Escape") {
      // Close any open dialogs or menus
      const openDialogs = document.querySelectorAll(".dialog-open");
      openDialogs.forEach((dialog) => {
        dialog.classList.remove("dialog-open");
      });
    }
  
    // Tab key navigation enhancement
    if (e.key === "Tab") {
      // Add focus styles for better visibility
      document.body.classList.add("keyboard-navigation");
    }
  });
  
  // Remove keyboard navigation indicator when mouse is used
  document.addEventListener("mousedown", function () {
    document.body.classList.remove("keyboard-navigation");
  });
  