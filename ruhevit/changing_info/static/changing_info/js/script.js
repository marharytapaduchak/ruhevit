// DOM Elements
document.addEventListener("DOMContentLoaded", function () {
    // Role selection
    const volunteerBtn = document.querySelector(".role-btn.volunteer");
    const militaryBtn = document.querySelector(".role-btn.military");
    const searchInput = document.querySelector(".search-text");
    const saveProfileBtn = document.getElementById("save-profile");
    const savePasswordBtn = document.getElementById("save-password");
  
    // Form fields
    const surnameInput = document.getElementById("surname");
    const nameInput = document.getElementById("name");
    const usernameInput = document.getElementById("username");
    const emailInput = document.getElementById("email");
    const descriptionInput = document.getElementById("description");
    const oldPasswordInput = document.getElementById("old-password");
    const newPasswordInput = document.getElementById("new-password");
  
    // Initialize role selection (default to volunteer)
    volunteerBtn.classList.add("active");
  
    // Role selection functionality
    volunteerBtn.addEventListener("click", function () {
      volunteerBtn.classList.add("active");
      militaryBtn.classList.remove("active");
      console.log("Role selected: Volunteer");
    });
  
    militaryBtn.addEventListener("click", function () {
      militaryBtn.classList.add("active");
      volunteerBtn.classList.remove("active");
      console.log("Role selected: Military");
    });
  
    // Search functionality
    searchInput.addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        performSearch(searchInput.value);
      }
    });
  
    function performSearch(query) {
      if (query.trim() === "") {
        alert("Будь ласка, введіть пошуковий запит");
        return;
      }
  
      console.log("Searching for:", query);
      // Here you would typically make an API call or perform search logic
      alert(`Пошук за запитом: ${query}`);
    }
  
    // Form validation
    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    }
  
    function validateForm() {
      let isValid = true;
  
      // Check required fields
      if (surnameInput.value.trim() === "") {
        alert("Будь ласка, введіть прізвище");
        surnameInput.focus();
        isValid = false;
      } else if (nameInput.value.trim() === "") {
        alert("Будь ласка, введіть ім'я");
        nameInput.focus();
        isValid = false;
      } else if (usernameInput.value.trim() === "") {
        alert("Будь ласка, введіть username");
        usernameInput.focus();
        isValid = false;
      } else if (emailInput.value.trim() === "") {
        alert("Будь ласка, введіть email");
        emailInput.focus();
        isValid = false;
      } else if (!validateEmail(emailInput.value.trim())) {
        alert("Будь ласка, введіть коректний email");
        emailInput.focus();
        isValid = false;
      } else if (descriptionInput.value.trim() === "") {
        alert("Будь ласка, введіть опис");
        descriptionInput.focus();
        isValid = false;
      }
  
      return isValid;
    }
  
    function validatePasswordForm() {
      let isValid = true;
  
      if (oldPasswordInput.value.trim() === "") {
        alert("Будь ласка, введіть старий пароль");
        oldPasswordInput.focus();
        isValid = false;
      } else if (newPasswordInput.value.trim() === "") {
        alert("Будь ласка, введіть новий пароль");
        newPasswordInput.focus();
        isValid = false;
      } else if (newPasswordInput.value.trim().length < 6) {
        alert("Новий пароль повинен містити щонайменше 6 символів");
        newPasswordInput.focus();
        isValid = false;
      }
  
      return isValid;
    }
  
    saveProfileBtn.addEventListener("click", function () {
      if (validateForm()) {
        // Get selected role
        const selectedRole = volunteerBtn.classList.contains("active")
          ? "Волонтер"
          : "Військовий";
  
        const profileData = {
          role: selectedRole,
          surname: surnameInput.value.trim(),
          name: nameInput.value.trim(),
          username: usernameInput.value.trim(),
          email: emailInput.value.trim(),
          description: descriptionInput.value.trim(),
        };
  
        console.log("Saving profile data:", profileData);
        alert("Профіль успішно збережено!");
      }
    });
  
    savePasswordBtn.addEventListener("click", function () {
      if (validatePasswordForm()) {
       
        const passwordData = {
          oldPassword: oldPasswordInput.value,
          newPassword: newPasswordInput.value,
        };
  
        console.log("Saving password data:", passwordData);
      
  
  
        oldPasswordInput.value = "";
        newPasswordInput.value = "";
  
        alert("Пароль успішно змінено!");
      }
    });
  
   
    const uploadPhotoBtn = document.querySelector(".upload-photo-btn");
    const deletePhotoBtn = document.querySelector(".delete-photo-btn");
    const profileImg = document.querySelector(".large-profile-img");
    const headerProfileImg = document.querySelector(".profile-img");
    let originalImageSrc = profileImg.src;
    let hasCustomImage = false;
  
    uploadPhotoBtn.addEventListener("click", function () {
      const fileInput = document.createElement("input");
      fileInput.type = "file";
      fileInput.accept = "image/jpeg, image/png, image/gif, image/webp";
  
    
      fileInput.click();
  
  
      fileInput.addEventListener("change", function () {
        if (fileInput.files && fileInput.files[0]) {
          const file = fileInput.files[0];
  
          
          if (file.size > 5 * 1024 * 1024) {
            alert("Файл занадто великий. Максимальний розмір файлу - 5MB.");
            return;
          }
  
      
          const validTypes = [
            "image/jpeg",
            "image/png",
            "image/gif",
            "image/webp",
          ];
          if (!validTypes.includes(file.type)) {
            alert(
              "Недійсний тип файлу. Будь ласка, виберіть зображення (JPEG, PNG, GIF, WEBP).",
            );
            return;
          }
  
      
          uploadPhotoBtn.textContent = "Завантаження...";
          uploadPhotoBtn.disabled = true;
          const uploadProgress = document.querySelector(".upload-progress");
          uploadProgress.style.display = "flex";
  
          const reader = new FileReader();
  
          reader.onload = function (e) {
          
            profileImg.src = e.target.result;
            headerProfileImg.src = e.target.result;
            hasCustomImage = true;
  
        
            uploadPhotoBtn.textContent = "Завантажити нове фото";
            uploadPhotoBtn.disabled = false;
            uploadProgress.style.display = "none";
  
        
            const successMessage = document.createElement("div");
            successMessage.textContent = "Фото успішно завантажено!";
            successMessage.style.color = "green";
            successMessage.style.marginTop = "10px";
            successMessage.style.fontSize = "14px";
  
          
            uploadPhotoBtn.parentNode.insertBefore(
              successMessage,
              uploadPhotoBtn.nextSibling,
            );
  
            
            setTimeout(() => {
              successMessage.remove();
            }, 3000);
  
            console.log("Photo uploaded successfully");
          };
  
          reader.onerror = function () {
            alert("Помилка при читанні файлу. Будь ласка, спробуйте ще раз.");
            uploadPhotoBtn.textContent = "Завантажити нове фото";
            uploadPhotoBtn.disabled = false;
            uploadProgress.style.display = "none";
          };
  
          reader.readAsDataURL(file);
        }
      });
    });
  

    deletePhotoBtn.addEventListener("click", function () {
      if (!hasCustomImage) {
        alert("Немає користувацького зображення для видалення.");
        return;
      }
  
    
      if (confirm("Ви впевнені, що хочете видалити фото профілю?")) {
      
        profileImg.src = originalImageSrc;
        headerProfileImg.src = originalImageSrc;
        hasCustomImage = false;
  
      
        const successMessage = document.createElement("div");
        successMessage.textContent = "Фото видалено!";
        successMessage.style.color = "green";
        successMessage.style.marginTop = "10px";
        successMessage.style.fontSize = "14px";
  
      
        deletePhotoBtn.parentNode.insertBefore(
          successMessage,
          deletePhotoBtn.nextSibling,
        );
  
    
        setTimeout(() => {
          successMessage.remove();
        }, 3000);
  
        console.log("Photo deleted");
      }
    });
  });
  