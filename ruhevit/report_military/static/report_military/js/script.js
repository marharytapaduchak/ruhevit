 // Search bar functionality
 const searchInput = document.getElementById("searchInput");
 const searchField = document.getElementById("searchField");
 const searchPlaceholder = document.getElementById("searchPlaceholder");

 searchInput.addEventListener("click", function () {
   searchField.focus();
 });

 searchField.addEventListener("focus", function () {
   searchPlaceholder.style.opacity = "0";
 });

 searchField.addEventListener("blur", function () {
   if (searchField.value === "") {
     searchPlaceholder.style.opacity = "1";
   }
 });

 // Button functionality
 const contactButton = document.getElementById("contactButton");
 const confirmButton = document.getElementById("confirmButton");

 contactButton.addEventListener("click", function () {
   alert("Контактування з волонтером: Анна Шевченко");
   this.classList.add("button-active");
   setTimeout(() => {
     this.classList.remove("button-active");
   }, 200);
 });

 confirmButton.addEventListener("click", function () {
   alert("Звіт підтверджено!");
   this.classList.add("button-active");
   setTimeout(() => {
     this.classList.remove("button-active");
   }, 200);
 });