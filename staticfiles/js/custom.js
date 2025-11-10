
//   <button id="themeToggleBtn" class="btn btn-sm btn-outline-light" type="button">
//                         <span id="themeToggleIcon">🌙</span>
//                     </button>

let html_element = document.documentElement;
let theme_btn = document.getElementById("themeToggleBtn");
let theme_icon = document.getElementById("themeToggleIcon");
let default_theme = 'light';

console.log("theme_icon : ", theme_icon)

// set default theme
html_element.setAttribute('data-bs-theme', default_theme)

// toggle on click between dark/light theme
theme_btn.addEventListener('click', function(){
    let current_theme = html_element.getAttribute('data-bs-theme')
    let next_theme;

    if(current_theme == 'light'){
        next_theme = 'dark';
        theme_icon.textContent = "🌙"
    }else{
        next_theme = 'light'
        theme_icon.textContent = "☀️"
    }

    html_element.setAttribute('data-bs-theme', next_theme)
})