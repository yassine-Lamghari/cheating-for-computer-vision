document.addEventListener("DOMContentLoaded", function () {
  const uploadArea = document.getElementById("upload-area");
  const fileInput = document.getElementById("file-input");
  const alertSound = document.getElementById("alert-sound");
  const notifSound = document.getElementById("notif-sound");

  // Gestion du drag and drop
  uploadArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = "#3498db";
    uploadArea.style.backgroundColor = "rgba(52, 152, 219, 0.1)";
  });

  uploadArea.addEventListener("dragleave", () => {
    uploadArea.style.borderColor = "#95a5a6";
    uploadArea.style.backgroundColor = "transparent";
  });

  uploadArea.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = "#95a5a6";
    uploadArea.style.backgroundColor = "transparent";

    if (e.dataTransfer.files.length) {
      fileInput.files = e.dataTransfer.files;
      updateFileInfo(e.dataTransfer.files[0]);
    }
  });

  uploadArea.addEventListener("click", () => {
    fileInput.click();
  });

  fileInput.addEventListener("change", () => {
    if (fileInput.files.length) {
      updateFileInfo(fileInput.files[0]);
    }
  });

  function updateFileInfo(file) {
    const uploadContent = uploadArea.querySelector(".upload-content");
    uploadContent.innerHTML = `
            <i class="upload-icon">📄</i>
            <h3>${file.name}</h3>
            <p>${(file.size / 1024 / 1024).toFixed(2)} MB</p>
        `;
  }

  // Simulation d'alerte (à remplacer par du vrai code de détection)
  function simulateAlert() {
    alertSound.play();
    showAlertNotification("Comportement suspect détecté: Smartphone");
  }

  function showAlertNotification(message) {
    const notification = document.createElement("div");
    notification.className = "alert-notification";
    notification.innerHTML = `
            <span class="alert-icon">⚠️</span>
            <span class="alert-message">${message}</span>
        `;

    document.body.appendChild(notification);

    setTimeout(() => {
      notification.classList.add("show");
    }, 100);

    setTimeout(() => {
      notification.classList.remove("show");
      setTimeout(() => {
        notification.remove();
      }, 300);
    }, 5000);
  }

  // Pour tester l'alerte
  // setTimeout(simulateAlert, 3000);
});
