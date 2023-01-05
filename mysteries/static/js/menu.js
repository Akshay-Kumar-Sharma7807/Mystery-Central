navMenuBtn = document.getElementById("nav-menu-btn")
navMenuContent = document.getElementById("nav-menu-content")
closeBtn = document.getElementById("close-btn")

closeBtn.onclick = () => {
    navMenuContent.classList.toggle("hidden")
}

navMenuBtn.onclick = () => {
    navMenuContent.classList.toggle("hidden")
}

userMenuBtn = document.getElementById("user-menu-btn")
userMenuContent = document.getElementById("user-menu-content")

userMenuBtn.onclick = () => {
    userMenuContent.classList.toggle("hidden")
}